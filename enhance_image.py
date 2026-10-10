import cv2
import numpy as np
from pathlib import Path

input_path = Path("input.jpg")
output_path = Path("enhanced.jpg")
comparison_path = Path("comparison.jpg")

# Load original image
original = cv2.imread(str(input_path))

if original is None:
    raise FileNotFoundError("Could not find input.jpg")

# Adjust brightness and contrast
enhanced = cv2.convertScaleAbs(
    original,
    alpha=1.3,
    beta=30
)

# Reduce color noise
enhanced = cv2.fastNlMeansDenoisingColored(
    enhanced, None, 5, 5, 7, 21
)

# Save enhanced image
cv2.imwrite(str(output_path), enhanced)

# Create a side-by-side comparison
comparison = np.hstack((original, enhanced))
cv2.imwrite(str(comparison_path), comparison)

print("Image enhancement completed!")
print(f"Original dimensions: {original.shape[1]} x {original.shape[0]}")
print(f"Enhanced image: {output_path}")
print(f"Comparison image: {comparison_path}")