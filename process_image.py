from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import KDTree

from tif_to_png import tif_to_png_converter

def create_image_two(image_path):
    # Open the input image and convert it to a NumPy array
    img = Image.open(image_path)
    img_array = np.array(img.convert('RGB'))
    
    # Perform KMeans clustering to identify the largest grouping of red meat pixels
    kmeans = KMeans(n_clusters=2, random_state=0).fit(img_array.reshape(-1, 3))
    labels = kmeans.labels_
    
    # Reshape labels to match the original shape of img_array
    labels_reshaped = labels.reshape(img_array.shape[:2])
    
    # Use the reshaped labels to create a boolean mask for red meat pixels
    red_meat_mask = labels_reshaped == 0
    
    # Use the mask to select red meat pixels
    red_meat_pixels = img_array[red_meat_mask]
    
    # Convert red_meat_pixels to a 2D array of shape (n, 3) where n is the number of red meat pixels
    red_meat_pixels_2d = red_meat_pixels.reshape(-1, 3)

    # Build a KDTree from the red meat pixels
    tree = KDTree(red_meat_pixels_2d)

    # Calculate the distance to the nearest red meat pixel for each pixel in img_array
    distances, _ = tree.query(img_array.reshape(-1, 3))
    distances = distances.reshape(img_array.shape[:2])
    
    # Calculate the optimal threshold dynamically based on the distribution of distances
    # For example, you might choose the 90th percentile as the threshold
    threshold = np.percentile(distances, 90)
    
    # Create a mask for pixels close to the red meat area using the dynamic threshold
    close_to_red_meat_mask = distances < threshold
    
    # Create a mask for white pixels
    white_pixels_mask = np.all(img_array < 100, axis=-1)
    
    # Combine the masks to identify intermuscular fat pixels
    intermuscular_fat_mask = white_pixels_mask & close_to_red_meat_mask
    
    # Apply the masks to categorize pixels
    img_array[intermuscular_fat_mask] = [0, 255, 0] # Green for intermuscular fat
    img_array[~intermuscular_fat_mask & white_pixels_mask] = [0, 0, 0] # Black for background
    img_array[~intermuscular_fat_mask & ~white_pixels_mask] = [255, 0, 0] # Red for red meat
    
    # Color the background black [remember, the dimensions are 768x572]
    img_array[1, 0] = [0, 0, 0]
    img_array[767, 0] = [0, 0, 0]
    #TODO: spread out from there(infect the other cells)

    # Convert the processed array back to an image
    img_three = Image.fromarray(img_array)
    
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
