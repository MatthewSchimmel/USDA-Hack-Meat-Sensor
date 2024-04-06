import cv2
import numpy as np
from skimage import measure

#Step 2: Load and Preprocess the Image
def load_and_preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    return hsv_image

# Step 3: Define Color Thresholds
def define_color_thresholds():
    # Define color ranges for background, meat, and intermuscular fat
    # These values are example thresholds and may need adjustment based on the dataset
    background_lower = np.array([0, 0, 0])
    background_upper = np.array([180, 255, 255])
    
    meat_lower = np.array([0, 100, 100])
    meat_upper = np.array([10, 255, 255])
    
    fat_lower = np.array([11, 100, 100])
    fat_upper = np.array([180, 255, 255])
    
    return background_lower, background_upper, meat_lower, meat_upper, fat_lower, fat_upper

#Step 4: Classify Pixels
def classify_pixels(hsv_image, background_lower, background_upper, meat_lower, meat_upper, fat_lower, fat_upper):
    # Create masks for each category
    background_mask = cv2.inRange(hsv_image, background_lower, background_upper)
    meat_mask = cv2.inRange(hsv_image, meat_lower, meat_upper)
    fat_mask = cv2.inRange(hsv_image, fat_lower, fat_upper)
    
    # Combine masks
    combined_mask = cv2.addWeighted(background_mask, 1, meat_mask, 1, 0)
    combined_mask = cv2.addWeighted(combined_mask, 1, fat_mask, 1, 0)
    
    return combined_mask
