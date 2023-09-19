# To crop images - 18/09/2023 - Cécilia - LIENSs
# LAUNCHED Visual study code Version: 1.77.0 from ANACONDA NAVIGATOR
# Version : 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  1 2023, 18:18:15) [MSC v.1916 64 bit (AMD64)]
# python --version
# conda --version
# example : Pampas submersion images

# Launch library and module
from PIL import Image
import os

# Set the input and output folder paths
input_folder = 'C:/Users/cpignonm/ownCloud/tests_python/crop_image/anim_12h_15min'
output_folder = 'C:/Users/cpignonm/ownCloud/tests_python/crop_image/anim_12h_15min/cropped_images/'

# Check the output folder 
os.makedirs(output_folder, exist_ok=True)

# Define the cropping coordinates (left, upper, right, lower)
crop_box = (400, 100, 1850, 1500)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        try:
            # Open the image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Crop the image using the specified coordinates
                cropped_img = img.crop(crop_box)

                # Save the cropped image to the output folder
                output_path = os.path.join(output_folder, filename)
                cropped_img.save(output_path)

                print(f'Cropped and saved {filename} to {output_path}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

print('Cropping completed.')