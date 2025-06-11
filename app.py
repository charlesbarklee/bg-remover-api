from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from rembg import remove
from io import BytesIO

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    output_image = BytesIO(output_data)
    output_image.name = "output.png"
    return FileResponse(output_image, media_type="image/png", filename="output.png")
