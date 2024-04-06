
# USDA-Hack-Meat-Sensor
How we're going to do it:
1. Convert the image to an HSV file (a set of color values)
2. find the particular color value of each pixel
3. determine where the whole grouping of red
4. determine where the white is in the red


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
