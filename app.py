import cv2
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Interactive Image Enhancement",
    page_icon="🖼️",
    layout="wide",
)

st.title("Interactive Image Enhancement")
st.write(
    "Upload a photo and adjust its brightness and contrast "
    "to see the results in real time."
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    file_bytes = np.frombuffer(
        uploaded_file.getvalue(),
        dtype=np.uint8,
    )
    original = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if original is None:
        st.error("Could not read this image. Please try another.")
        st.stop()

    st.sidebar.header("Enhancement Controls")

    brightness = st.sidebar.slider(
        "Brightness",
        min_value=-100,
        max_value=100,
        value=0,
        step=5,
    )

    contrast = st.sidebar.slider(
        "Contrast",
        min_value=0.5,
        max_value=3.0,
        value=1.0,
        step=0.1,
    )

    enhanced = cv2.convertScaleAbs(
        original,
        alpha=contrast,
        beta=brightness,
    )

    original_rgb = cv2.cvtColor(
        original, cv2.COLOR_BGR2RGB
    )
    enhanced_rgb = cv2.cvtColor(
        enhanced, cv2.COLOR_BGR2RGB
    )

    left, right = st.columns(2)

    with left:
        st.subheader("Original Image")
        st.image(original_rgb, width="stretch")

    with right:
        st.subheader("Enhanced Image")
        st.image(enhanced_rgb, width="stretch")

    st.write(f"Brightness: {brightness}")
    st.write(f"Contrast: {contrast:.1f}")

    success, encoded = cv2.imencode(".png", enhanced)

    if success:
        st.download_button(
            label="Download Enhanced Image",
            data=encoded.tobytes(),
            file_name="enhanced_image.png",
            mime="image/png",
        )
else:
    st.info("Upload an image to begin.")