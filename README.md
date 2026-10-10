Image Enhancement with OpenCV

A beginner-friendly Computer Vision project that improves image brightness and contrast using OpenCV and provides an interactive web interface built with Streamlit.

Features
Command-Line Version
Load an image from a file.
Adjust brightness and contrast.
Reduce image noise.
Save the enhanced image.
Generate a side-by-side comparison of the original and enhanced images.
Interactive Web App
Upload JPG, JPEG, or PNG images.
Adjust brightness using a slider.
Adjust contrast using a slider.
Preview the original and enhanced images side by side.
Download the enhanced image as a PNG file.
Technologies Used
Python
OpenCV
NumPy
Streamlit
Project Files
enhance_image.py — Command-line image enhancement script.
app.py — Interactive Streamlit web application.
input.jpg — Sample input image.
enhanced.jpg — Enhanced sample image.
comparison.jpg — Original and enhanced image comparison.
requirements.txt — Python dependencies.
Installation
1. Clone the repository
git clone https://github.com/RicelB/image-enhancement-opencv.git
cd image-enhancement-opencv
2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install the dependencies
python -m pip install -r requirements.txt
How to Run
Option 1: Command-Line Version

Run the image enhancement script:

python enhance_image.py

The script processes input.jpg and generates the enhanced image and comparison image.

Option 2: Interactive Web App

Start the Streamlit application:

python -m streamlit run app.py

Open the local URL displayed in your terminal, usually http://localhost:8501.

Upload an image, adjust the brightness and contrast sliders, and download the enhanced result.

Results

The command-line version generates a side-by-side comparison:




Learning Objectives

This project demonstrates practical applications of Computer Vision, including image loading, brightness and contrast adjustment, noise reduction, image processing, and interactive visualization.

Future Improvements
Add image sharpening and additional enhancement filters.
Implement before-and-after comparison controls.
Explore AI-based image restoration and enhancement models.
Evaluate image quality using objective metrics.
Limitations

The current enhancement methods use traditional image-processing techniques. Results depend on the input image and selected settings. The interactive web app currently focuses on brightness and contrast adjustment, while noise reduction is included in the command-line version.



GitHub: RicelB