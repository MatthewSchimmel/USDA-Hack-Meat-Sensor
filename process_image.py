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
    
    # Color the background black [remember, the dimensions are 768x572] & [row, col]
    for i in range(img.size[0]):  # For all pixels in range (width)
        pixels_two[i, 0] = (0, 150, 0) #the top row
        pixels_two[i, img.size[1] - 1] = (0, 150, 0) # Green
    for i in range(img.size[1]):  # For all pixels in range (width)
        pixels_two[1, i] = (0, 150, 0) #the top row
        pixels_two[img.size[0] - 1, i] = (0, 150, 0) # Green
    
    #spread out from there(infect the other cells) DOWN AND RIGHTdirection
    for i in range(img.size[0] - 1):  # Width
        for j in range(img.size[1] - 1):  # Height
            if pixels_two[i, j] == (0, 150, 0): # if the pixel equals green 
                if pixels_two[i, j + 1] == (0, 0, 0): # if the pixel to the bottom of it is black
                    pixels_two[i, j + 1] = (0, 150, 0) # set botton pixel to green
                if pixels_two[i + 1, j] == (0, 0, 0): #if the pixel to the right of it is black
                    pixels_two[i + 1, j] = (0, 150, 0) # set botton pixel to green
    
    #spread out from there(infect the other cells) UP AND LEFT direction
    for i in range(img.size[0] - 1):  # Width
        for j in range(img.size[1] - 1):  # Height
            if pixels_two[i, j] == (0, 150, 0): # if the pixel equals green 
                if pixels_two[i, j - 1] == (0, 0, 0): # if the pixel above is black
                    pixels_two[i, j - 1] = (0, 150, 0)
                if pixels_two[i - 1, j] == (0, 0, 0): #if the pixel to the left of it is black
                    pixels_two[i - 1, j] = (0, 150, 0)

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