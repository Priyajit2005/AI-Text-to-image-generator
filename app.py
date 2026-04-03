import streamlit as st
from image_generator import generate_image_openai
from utils import build_styled_prompt, get_download_file_name

st.set_page_config(page_title="AI Text-to-Image Generator", layout="wide")

st.title("🎨 AI Text-to-Image Generator")
st.write("Generate images from text prompts with style selection.")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")

    style = st.selectbox(
        "Select Style",
        ["Realistic", "Cartoon", "Anime", "Sketch", "Oil Painting", "3D Render"]
    )

    size = st.selectbox(
        "Select Image Size",
        ["1024x1024", "1536x1024", "1024x1536"]
    )

    quality = st.selectbox(
        "Select Quality",
        ["low", "medium", "high"],
        index=1
    )

prompt = st.text_area(
    "Enter your image prompt",
    placeholder="Example: A futuristic city at sunset with flying cars",
    height=150
)

generate_btn = st.button("Generate Image")

if "image_bytes" not in st.session_state:
    st.session_state.image_bytes = None

if "final_prompt" not in st.session_state:
    st.session_state.final_prompt = ""

if generate_btn:
    if not api_key.strip():
        st.error("Please enter your OpenAI API key.")
    elif not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        final_prompt = build_styled_prompt(prompt, style)
        st.session_state.final_prompt = final_prompt

        with st.spinner("Generating image..."):
            image_bytes, error = generate_image_openai(
                api_key=api_key,
                prompt=final_prompt,
                size=size,
                quality=quality
            )

        if error:
            st.error(error)
        else:
            st.session_state.image_bytes = image_bytes
            st.success("Image generated successfully.")

if st.session_state.final_prompt:
    with st.expander("Final Prompt Used"):
        st.write(st.session_state.final_prompt)

if st.session_state.image_bytes:
    st.subheader("Generated Image")
    st.image(st.session_state.image_bytes, use_container_width=True)

    file_name = get_download_file_name("generated_image", "png")
    st.download_button(
        label="Download Image",
        data=st.session_state.image_bytes,
        file_name=file_name,
        mime="image/png"
    )