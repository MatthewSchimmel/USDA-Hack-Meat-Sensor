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
