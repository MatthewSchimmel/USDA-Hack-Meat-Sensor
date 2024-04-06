from PIL import Image
from tif_to_png import tif_to_png_converter

def create_image_two(image_path):
    # Open the input image
    img = Image.open(image_path)
    
    # Create a blank image of the same size
    img_two = Image.new("RGB", img.size)
    
    # Load pixel data
    pixels = img.load()
    pixels_two = img_two.load()
    
    # Threshold for considering a color as red
    red_threshold = 100  # Adjust this threshold as needed
    
    # Iterate through each pixel
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
            # Get the RGB values of the pixel
            r, g, b = pixels[i, j]
            
            # If the pixel is similar to red, set it to red
            if r > red_threshold and g < red_threshold and b < red_threshold:
                pixels_two[i, j] = (255, 0, 0)  # Red
            else:
                pixels_two[i, j] = (0, 0, 0)  # Black (non-red pixels)
    
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

#TODO: this one is working fine. But gotta improve the sensitivity to any red color.



