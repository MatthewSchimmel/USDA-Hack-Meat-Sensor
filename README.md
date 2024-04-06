
# USDA-Hack-Meat-Sensor
How the program works:
1. The file is converted into a .png
2. The rgb values are determined for each pixel
3. threshold values are set to determine if each pixel is closer in color to meat or fat/background
4. A two-color mockup is made
5. A new color is created on the borders of the image that slowly seeps into all similar coloring of the image [to designate background and outside fat]
6. The remaining inside coloring is inside fat
todo (easy!)
7. calculate the ratios or red to black (inside fat)
8. assign a score accordingly
9. update the excel spreatsheet like a .csv file


## About the project:
#### Three primary quality designations:
- Prime - best
- Choice - middle
- Select - lowest

#### How to grade:
- Marbling
  - Intramuscular fat
    - Amount
    - Texture
    - Distribution
   
#### Resources:
- 1400 images
- marbling score goes from 100-1100
- additional 500 images for validation of accuracy and consistency
  - 300-399 - select ~15%
  - 400-499 - low choice ~ 50%
  - 500-699 - upper 2/3rds choice ~ 35%
  - 700+ - prime ~ 19%
