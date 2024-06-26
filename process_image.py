import os
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
                pixels_two[i, j] = (255, 255, 255)  # Green (non-red pixels)
    print("Two-Tone Color Grading Complete")

    # Color the outline black [remember, the dimensions are 768x572] & [row, col]
    for i in range(img.size[0]):  # For all pixels in range (width)
        pixels_two[i, 0] = (0, 0, 0) #the top row
        pixels_two[i, img.size[1] - 1] = (0, 0, 0) # the bottom row
    for i in range(img.size[1]):  # For all pixels in range (width)
        pixels_two[0, i] = (0, 0, 0) #the leftmost column
        pixels_two[img.size[0] - 1, i] = (0, 0, 0) # the rightmost column

    for x in range(64):#64 iterations should be enough to get decent accuracy
        for i in range(img.size[0] - 1):  # Width
            for j in range(img.size[1] - 1):  # Height
                if pixels_two[i, j] == (255, 255, 255): # if the pixel equals green 
                    #checks the neighboring cells in all eight directions around it for black
                    if pixels_two[i + 1, j + 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i + 1, j] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i + 1, j - 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i, j + 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i, j] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i, j - 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i - 1, j + 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i - 1, j] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
                    elif pixels_two[i - 1, j - 1] == (0, 0, 0):
                        pixels_two[i, j] = (0, 0, 0)
    
    print("Three-Tone Color Grading Complete")
    # Save the resulting image
    filename = "out" + image_path
    img_two.save(filename)
        
    # Display the image
    #img_two.show()


# Convert TIF image to PNG
tif_to_png_converter("sample1.tif")
tif_to_png_converter("sample2.tif")
tif_to_png_converter("sample3.tif")

create_image_two("sample1.png")
create_image_two("sample2.png")
create_image_two("sample3.png")
