import os
from huggingface_hub import InferenceClient

api_key = os.getenv("API_KEY")
client = InferenceClient(api_key=api_key)

image = client.text_to_image(
    prompt="A serene lake surrounded by mountains at sunset, photorealistic style",
    model="black-forest-labs/FLUX.1-Krea-dev"
)

# Save the generated image
image.save("image/generated_image.png")