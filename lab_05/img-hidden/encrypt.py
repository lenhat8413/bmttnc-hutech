import os
from PIL import Image

def encode_image(image_path, message):
    image = Image.open(image_path)
    width, height = image.size
    pixel_index =0
    binary_message = '' .join(format(ord(char),'08b')for char in message)
    binary_message += '1111111111111110'# End of message delimiter

    data_index = 0
    for row in range(height):
        for col in range (width):
            pixel =list (img.getpixel((col,row)))

            for color_channel

    encoded_image.save('encoded_' + os.path.basename(imagepath))