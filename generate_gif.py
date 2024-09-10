# Generate a gif file - 18/09/2023 - Cécilia - LIENSs
# LAUNCHED Visual study code Version: 1.77.0 from ANACONDA NAVIGATOR
# Version : 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  1 2023, 18:18:15) [MSC v.1916 64 bit (AMD64)]
# python --version
# conda --version
# example : Pampas submersion images
from PIL import Image
import os

# Set the folder path containing your image files
input_folder = 'C:/Users/xxxx/cropped_images'

# List to store image files
image_files = []

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        try:
            # Open the image file
            img = Image.open(os.path.join(input_folder, filename))
            image_files.append(img)
            print(f'Added {filename}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

# Sort the image files by filename
image_files.sort(key=lambda x: x.filename)

# Set the path for the output GIF
output_gif = 'output_duration500.gif'

# Save the sorted images as a GIF
if image_files:
    image_files[0].save(
        os.path.join(input_folder, output_gif),
        save_all=True,
        append_images=image_files[1:],
        duration=500,  # Duration between frames in milliseconds
        loop=0  # 0 means loop indefinitely, set to a different number to loop a specific number of times
    )
    print(f'GIF saved as {os.path.join(input_folder, output_gif)}')
else:
    print('No images found for GIF creation.')

print('GIF creation completed.')
