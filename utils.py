from datetime import datetime


STYLE_MAP = {
    "Realistic": "photorealistic, ultra-detailed, realistic lighting",
    "Cartoon": "cartoon style, colorful, vibrant illustration",
    "Anime": "anime style, highly detailed, cinematic illustration",
    "Sketch": "pencil sketch, hand-drawn, monochrome",
    "Oil Painting": "oil painting style, artistic brush strokes, textured canvas look",
    "3D Render": "3D render, highly detailed, studio lighting"
}


def build_styled_prompt(user_prompt, style):
    style_text = STYLE_MAP.get(style, "")
    return f"{user_prompt}, {style_text}"


def get_download_file_name(base_name="image", extension="png"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.{extension}"