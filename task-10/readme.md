### How It Works
#### OpenCV for Image Processing and Dot Detection
**OpenCV** (Open Source Computer Vision Library) is a powerful tool used for image processing and computer vision tasks. In this project, OpenCV is utilized to detect the position of colored dots within the images.

1. **Image Loading and Conversion:**
   - **OpenCV** loads each image from the `assets` folder.
   - The images are then converted from color (BGR) to grayscale. Grayscale simplifies the processing by reducing the image to a single intensity channel instead of three color channels (BGR).

   ```python
   image = cv2.imread(image_path)
   gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   ```

2. **Thresholding and Binary Image Creation:**
   - Thresholding converts the grayscale image into a binary image, where the dot becomes white, and the background turns black. This step isolates the dot from the background, making it easier to detect.

   ```python
   _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)
   ```

3. **Contour Detection:**
   - OpenCV’s contour detection algorithm is applied to the binary image to identify the outline of the dot. The center of the largest contour is considered the location of the dot.

   ```python
   contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   ```

4. **Moment Calculation:**
   - The moments of the contour (a mathematical representation of its shape) are calculated to find the exact coordinates (centroid) of the dot.

   ```python
   M = cv2.moments(contour)
   cX = int(M["m10"] / M["m00"])
   cY = int(M["m01"] / M["m00"])
   ```

5. **Color Extraction:**
   - The color of the dot is extracted by accessing the pixel value at the dot's coordinates in the original color image.

   ```python
   color = image[cY, cX].tolist()
   ```

#### Pillow for Image Drawing and Line Connection
**Pillow** (Python Imaging Library) is used for manipulating images, including drawing shapes and lines. In this project, Pillow is employed to draw lines between the detected dots to reveal the hidden pattern.

1. **Creating a Blank Canvas:**
   - A blank image (canvas) is created where the lines connecting the dots will be drawn.

   ```python
   final_image = Image.new("RGB", (512, 512), "white")
   ```

2. **Drawing Lines Between Dots:**
   - Pillow’s `ImageDraw` module is used to draw lines on the canvas. The script iterates through the detected dots and draws a line from each dot to the next one in sequence. The color of each line is determined by the starting dot’s color.

   ```python
   draw.line([current_dot["coords"], next_dot["coords"]], fill=current_dot["color"], width=2)
   ```

3. **Handling Line Breaks:**
   - If a fully white image is encountered (indicating a line break), the script skips drawing a line, thereby preserving the intended breaks in the pattern.

#### Implementation Summary
- **OpenCV** handles the heavy lifting of detecting the exact position and color of each dot in the images. It processes the images by converting them to grayscale, applying thresholding, and detecting contours.
- **Pillow** then takes the extracted information (coordinates and colors) and draws lines between the dots on a new image, creating the final stitched pattern.


