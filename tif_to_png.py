
from PIL import Image
import os

def tif_to_png_converter(input_file):
    # Open the TIF image
    tif_image = Image.open(input_file)
    
    # Get the file name and directory
    file_name, _ = os.path.splitext(input_file)
    output_file = file_name + ".png"
    
    # Convert and save as PNG in the same directory
    tif_image.save(output_file, "PNG")
    print(f"Converted {input_file} to {output_file}")

# # Provide the path to the TIF image file
# input_file = "image_one.tif"

# # Call the function
# tif_to_png(input_file)