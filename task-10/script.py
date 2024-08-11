import os
import cv2
from PIL import Image, ImageDraw

# Define the path to the folder containing the images
assets_folder = r"C:\Users\ARJUN\OneDrive\Desktop\amfoss-tasks\task-10\assets"

# Get a sorted list of all image files in the folder
image_files = sorted([f for f in os.listdir(assets_folder) if f.endswith('.png') or f.endswith('.jpg')])

# Initialize an empty list to store the dot information
dots_info = []

# Loop through each image file to detect the dot and record its coordinates and color
for image_file in image_files:
    image_path = os.path.join(assets_folder, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error loading image {image_file}")
        continue

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to create a binary image
    _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)

    # Find contours (which will be the dot) in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get the largest contour (the dot)
        contour = max(contours, key=cv2.contourArea)

        # Get the coordinates of the center of the dot
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            # Get the color of the dot (assuming it's the color of the contour area)
            color = image[cY, cX].tolist()

            # Record the coordinates and color
            dots_info.append({"coords": (cX, cY), "color": tuple(color), "filename": image_file})
        else:
            # Handle the case of white image (no dot)
            dots_info.append({"coords": None, "color": None, "filename": image_file})
    else:
        # Handle the case of white image (no dot)
        dots_info.append({"coords": None, "color": None, "filename": image_file})

# Create a new image with the same dimensions as the original images to draw the lines
final_image = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(final_image)

# Draw lines between the dots
for i in range(len(dots_info) - 1):
    current_dot = dots_info[i]
    next_dot = dots_info[i + 1]

    # Skip if the current or next image is a white image (line break)
    if current_dot["coords"] is None or next_dot["coords"] is None:
        continue

    # Draw a line from the current dot to the next dot with the color of the current dot
    draw.line([current_dot["coords"], next_dot["coords"]], fill=current_dot["color"], width=2)

# Save the final image
final_image.save("stitched_image.png")
print("Stitched image saved as stitched_image.png")
