from PIL import Image
from scipy import ndimage
from skimage import measure, segmentation, color
from scipy.ndimage import distance_transform_edt

import numpy as np

from tif_to_png import tif_to_png_converter

def create_image_two(image_path):
    # Open the input image
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img_gray = img.convert('L')
    
    # Convert the image to a NumPy array
    img_array = np.array(img_gray)
    
    # Threshold for considering a color as red
    red_threshold = 100 # Adjust this threshold as needed
    
    # Apply a threshold to the grayscale image to create a binary image
    binary_img = img_array > red_threshold
    
    # Label connected components in the binary image
    labels = measure.label(binary_img)
    
    # Find the largest connected component (assuming it represents the red meat)
    largest_component = labels == np.argmax(np.bincount(labels.flat)[1:]) + 1
    
    distance_transform = distance_transform_edt(~binary_img)
    # Create a new image to store the results
    img_two = Image.new("RGB", img.size)
    pixels_two = img_two.load()
    
    # Define a distance threshold for considering a pixel as intermuscular fat
    fat_distance_threshold = 5 # Adjust this threshold as needed
    print("--- CHECKPOINT ---")

# Iterate through each pixel
    for i in range(img.size[0]): # Width
        for j in range(img.size[1]): # Height
            # If the pixel is part of the largest component, set it to red
            if largest_component[i, j]:
                pixels_two[i, j] = (255, 0, 0) # Red
            else:
                # If the pixel is close to the largest component, set it to white (intermuscular fat)
                if distance_transform[i, j] <= fat_distance_threshold:
                    pixels_two[i, j] = (255, 255, 255) # White
                else:
                    pixels_two[i, j] = (0, 0, 0) # Black (background)
    # Save the resulting image
    img_two.save("image_two.png")
    
    # Display the image
    img_two.show()

# Convert TIF image to PNG
tif_to_png_converter("image_one.tif")

# Provide the path to the converted PNG image
input_image_path = "image_one.png"

# Call the function with the input image path
create_image_two(input_image_path)
