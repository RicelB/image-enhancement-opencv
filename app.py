import cv2
import numpy as np
import streamlit as st
from streamlit_image_comparison import image_comparison
def calculate_image_statistics(image):
    """Calculate basic brightness and intensity statistics."""

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate average brightness
    mean_brightness = np.mean(grayscale)

    # Calculate intensity standard deviation
    intensity_std = np.std(grayscale)

    # Get image dimensions
    height, width = grayscale.shape

    return {
        "Mean Brightness": round(float(mean_brightness), 2),
        "Intensity Standard Deviation": round(float(intensity_std), 2),
        "Width": width,
        "Height": height,
    }

# Page configuration
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

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:

    file_bytes = np.frombuffer(
        uploaded_file.getvalue(),
        dtype=np.uint8,
    )

    original = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR,
    )

    if original is None:
        st.error("Could not read this image. Please try another.")
        st.stop()

    # Sidebar controls
    st.sidebar.header("Enhancement Controls")

    filter_option = st.sidebar.selectbox(
        "Choose an Enhancement Filter",
        [
            "None",
            "Sharpening",
            "Denoising",
            "Gaussian Blur",
        ],
    )

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

    # Apply enhancement
    enhanced = cv2.convertScaleAbs(
        original,
        alpha=contrast,
        beta=brightness,
    )

    # Apply selected filter
    if filter_option == "Sharpening":
        sharpening_kernel = np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ])
        enhanced = cv2.filter2D(
            enhanced,
            -1,
            sharpening_kernel,
        )

    elif filter_option == "Denoising":
        enhanced = cv2.fastNlMeansDenoisingColored(
            enhanced,
            None,
            10,
            10,
            7,
            21,
        )

    elif filter_option == "Gaussian Blur":
        enhanced = cv2.GaussianBlur(
            enhanced,
            (5, 5),
            0,
        )

    # Convert BGR to RGB
    original_rgb = cv2.cvtColor(
        original,
        cv2.COLOR_BGR2RGB,
    )

    enhanced_rgb = cv2.cvtColor(
        enhanced,
        cv2.COLOR_BGR2RGB,
    )

    # Display original and enhanced images
    left, right = st.columns(2)

    with left:
        st.subheader("Original Image")
        st.image(original_rgb, width="stretch")

    with right:
        st.subheader("Enhanced Image")
        st.image(enhanced_rgb, width="stretch")

    # Interactive comparison slider
    st.divider()

    st.subheader("Interactive Before-and-After Comparison")

    st.write(
        "Drag the slider left or right to compare "
        "the original and enhanced images."
    )

    image_comparison(
        img1=original_rgb,
        img2=enhanced_rgb,
        label1="Original",
        label2="Enhanced",
        width=700,
        starting_position=50,
        show_labels=True,
        make_responsive=True,
    )
     # Display image statistics
    st.divider()
    st.subheader("Image Statistics")

    # Convert RGB images to BGR for the statistics function
    original_bgr = cv2.cvtColor(original_rgb, cv2.COLOR_RGB2BGR)
    enhanced_bgr = cv2.cvtColor(enhanced_rgb, cv2.COLOR_RGB2BGR)

    # Calculate statistics
    original_stats = calculate_image_statistics(original_bgr)
    enhanced_stats = calculate_image_statistics(enhanced_bgr)

    # Display statistics side by side
    stats_left, stats_right = st.columns(2)

    with stats_left:
        st.markdown("### Original Image")
        st.write(f"Mean Brightness: {original_stats['Mean Brightness']}")
        st.write(
            "Intensity Standard Deviation: "
            f"{original_stats['Intensity Standard Deviation']}"
        )
        st.write(
            f"Dimensions: {original_stats['Width']} × "
            f"{original_stats['Height']} pixels"
        )

    with stats_right:
        st.markdown("### Enhanced Image")
        st.write(f"Mean Brightness: {enhanced_stats['Mean Brightness']}")
        st.write(
            "Intensity Standard Deviation: "
            f"{enhanced_stats['Intensity Standard Deviation']}"
        )
        st.write(
            f"Dimensions: {enhanced_stats['Width']} × "
            f"{enhanced_stats['Height']} pixels"
        )

    # Display adjustment values
    st.write(f"Brightness: {brightness}")
    st.write(f"Contrast: {contrast:.1f}")

    # Download enhanced image
    success, encoded = cv2.imencode(
        ".png",
        enhanced,
    )

    if success:
        st.download_button(
            label="Download Enhanced Image",
            data=encoded.tobytes(),
            file_name="enhanced_image.png",
            mime="image/png",
        )

else:
    st.info("Upload an image to begin.")