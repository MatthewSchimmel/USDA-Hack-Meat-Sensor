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
    # TODO: These values are example thresholds and may need adjustment based on the dataset
    background_lower = np.array([0, 0, 0])#black
    background_upper = np.array([180, 50, 50])#light red
    
    meat_lower = np.array([150, 100, 80])# light organge
    meat_upper = np.array([255, 0, 0])# true red
    
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

# Step 5: Segment and Identify the Largest Grouping of Red Meat Pixels
# This step involves segmenting the image to identify the largest grouping of red meat pixels.
# Uses the "measure.label" function from "scikit-image" library to label connected variables.
def segment_and_inspect_for_fat(combined_mask, fat_lower, fat_upper):
    # Label connected components
    labels = measure.label(combined_mask, connectivity=2, background=0)
    
    # Find the largest label (grouping of red meat pixels)
    largest_label = np.argmax(np.bincount(labels.flat)[1:]) + 1
    
    # Create a mask for the largest grouping
    largest_grouping_mask = np.zeros_like(combined_mask)
    largest_grouping_mask[labels == largest_label] = 255
    
    # Apply the fat color threshold to the largest grouping mask to identify fat pixels
    fat_mask = cv2.inRange(largest_grouping_mask, fat_lower, fat_upper)
    
    return fat_mask

# Step 6: Apply the Mask to the Original Image
def apply_mask_to_image(image, largest_grouping_mask):
    # Apply the mask to the original image
    segmented_image = cv2.bitwise_and(image, image, mask=largest_grouping_mask)
    
    return segmented_image

def main(image_path):
    # Load and preprocess the image
    hsv_image = load_and_preprocess_image(image_path)
    
    # Define color thresholds
    background_lower, background_upper, meat_lower, meat_upper, fat_lower, fat_upper = define_color_thresholds()
    
    # Classify pixels
    combined_mask = classify_pixels(hsv_image, background_lower, background_upper, meat_lower, meat_upper, fat_lower, fat_upper)
    
    # Segment and inspect the largest grouping of red meat pixels for fat
    fat_mask = segment_and_inspect_for_fat(combined_mask, fat_lower, fat_upper)
    
    # Apply the fat mask to the original image
    segmented_image = apply_mask_to_image(cv2.imread(image_path), fat_mask)
    
    # Display the segmented image
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    main(image_path)
