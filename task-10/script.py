import os
import cv2
from PIL import Image, ImageDraw


assets_folder = r"~/Documents/amfoss-tasks/task-10/assets"


def collect_images(folder_path):
    files_in_directory = os.listdir(folder_path)
    image_file_list = []
    for file_name in files_in_directory:
        if file_name.endswith('.png') or file_name.endswith('.jpg'):
            image_file_list.append(file_name)
    return sorted(image_file_list)


image_files = collect_images(assets_folder)


def load_and_process_image(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            return largest_contour, image
        else:
            return None, None
    else:
        return None, None


dots_info = []

for image_file in image_files:
    image_path = os.path.join(assets_folder, image_file)
    contour, image = load_and_process_image(image_path)

    if contour is not None and image is not None:
        moments = cv2.moments(contour)
        if moments["m00"] != 0:
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])
            pixel_color = image[cY, cX]
            pixel_color_as_list = pixel_color.tolist()
            dot_data = {"coords": (cX, cY), "color": tuple(pixel_color_as_list), "filename": image_file}
            dots_info.append(dot_data)
        else:
            dots_info.append({"coords": None, "color": None, "filename": image_file})
    else:
        dots_info.append({"coords": None, "color": None, "filename": image_file})


def create_blank_image(width, height, background_color="white"):
    img = Image.new("RGB", (width, height), background_color)
    return img


def draw_line_on_image(draw_object, start_coords, end_coords, color_tuple, thickness):
    if start_coords is not None and end_coords is not None:
        draw_object.line([start_coords, end_coords], fill=color_tuple, width=thickness)


final_image_width = 512
final_image_height = 512
background = "white"
final_image = create_blank_image(final_image_width, final_image_height, background)

drawer = ImageDraw.Draw(final_image)

for i in range(0, len(dots_info) - 1):
    first_dot = dots_info[i]
    second_dot = dots_info[i + 1]
    if first_dot["coords"] is not None and second_dot["coords"] is not None:
        first_dot_color = first_dot["color"]
        first_dot_coords = first_dot["coords"]
        second_dot_coords = second_dot["coords"]
        draw_line_on_image(drawer, first_dot_coords, second_dot_coords, first_dot_color, 2)


output_image_path = "stitched_image.png"


def save_final_image(image_obj, save_path):
    image_obj.save(save_path)


save_final_image(final_image, output_image_path)

print(f"Stitched image saved as {output_image_path}")
