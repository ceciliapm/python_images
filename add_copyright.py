from PIL import Image, ImageDraw, ImageFont
import os

# Input folder containing images
input_folder = 'C:/Users/cpignonm/ownCloud/tests_python/copyright_image/Thierry'

# Output folder to save the edited images
output_folder = 'C:/Users/cpignonm/ownCloud/tests_python/copyright_image/copyright_add/Thierry'

# Text to add to the images
text_to_add = "© LIENSs - T. GUYOT"

# Font settings
font_size = 36
font_color = (0, 0, 0)
font_path = "C:/Windows/Fonts/Arial/ariali.ttf"  

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # Open the image
        image = Image.open(os.path.join(input_folder, filename))
        
        # Create a drawing context
        draw = ImageDraw.Draw(image)
        
        # Load the specified font
        font = ImageFont.truetype(font_path, font_size)
        
        # Calculate text size and position
        text_width, text_height = draw.textsize(text_to_add, font)
        x = (image.width - text_width) // 1
        y = image.height - text_height - 10  # Adjust the vertical position
        
        # Add text to the image using textbbox
        text_bbox = draw.textbbox((x, y), text_to_add, font=font)
        draw.text((x, y), text_to_add, font=font, fill=font_color)
        
        # Save the edited image to the output folder
        output_path = os.path.join(output_folder, filename)
        image.save(output_path)
        
        # Close the image
        image.close()

print("Text added to images in the folder.")
