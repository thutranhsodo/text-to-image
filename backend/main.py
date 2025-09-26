from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from huggingface_hub import InferenceClient
from io import BytesIO
from PIL import Image
import base64
import os

app = FastAPI()

api_key = os.getenv("API_KEY")
client = InferenceClient(api_key=api_key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_image(prompt: str = Form(...)):
    try:
        image: Image.Image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-dev"
        )

        # Chuyển ảnh sang base64 để gửi qua HTTP
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return JSONResponse(content={"image": f"data:image/png;base64,{img_str}"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
