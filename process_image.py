from PIL import Image
from tif_to_png import tif_to_png_converter

def create_image_two(image_path):
    # Open the input image
    img = Image.open(image_path)
    
    # Create a blank image of the same size
    img_three = Image.new("RGB", img.size)
    
    # Load pixel data
    pixels = img.load()
    pixels_three = img_three.load()
    
    # Thresholds for color categories
    red_threshold = 100 # Adjust this threshold as needed for meat
    fat_threshold = 150 # Adjust this threshold as needed for intermuscular fat
    
    # Iterate through each pixel
    for i in range(img.size[0]): # Width
        for j in range(img.size[1]): # Height
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            
            # If the pixel is similar to red, set it to red
            if r > red_threshold and g < red_threshold and b < red_threshold:
                pixels_three[i, j] = (255, 0, 0)
            # If the pixel is similar to fat, set it to green (intermuscular fat)
            elif r > fat_threshold and g < fat_threshold and b < fat_threshold:
                pixels_three[i, j] = (0, 255, 0)
            else: # else the pixel is background, set it to black
                pixels_three[i, j] = (0, 0, 0)
    
    # Save the resulting image
    img_three.save("image_three.png")
    
    # Display the image
    img_three.show()

# Convert TIF image to PNG
tif_to_png_converter("image_one.tif")

# Provide the path to the converted PNG image
input_image_path = "image_one.png"

# Call the function with the input image path
create_image_two(input_image_path)