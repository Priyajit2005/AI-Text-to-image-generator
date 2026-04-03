import base64
from openai import OpenAI


def generate_image_openai(api_key, prompt, size="1024x1024", quality="medium"):
    """
    Generates an image using OpenAI image generation model.
    Returns: (image_bytes, error_message)
    """
    try:
        client = OpenAI(api_key=api_key)

        response = client.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size=size,
            quality=quality
        )

        image_base64 = response.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        return image_bytes, None

    except Exception as e:
        return None, f"Image generation failed: {str(e)}"