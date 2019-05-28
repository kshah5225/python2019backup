from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw
import numpy as np
from PIL import ImageOps, Image

def RGB_Manuel_Filter_one_image(original_image = 'None', Redness = 0, Greeness = 90, Blueness = 0, Border_size = 200, border_color = 'red', pick_mask = '../new_peace.png'):
    '''This Function takes the input image and adjusts its RGB values and then
    make that an image then we apply a mask on the image while pasting it onto 
    the original image making an color adjusted peace sign version of the 
    picture. after that we add a border of a specified amount of pixels and of 
    a specified color and lastly we add our logo on the top right corner of the 
    frame/border. This Function takes up to 7 arguements where the first one is 
    the files location and the file as a string(file must be written as a string
    path). The second arguement is how much redness will be added to the the 
    pixels in the peace sign as an integer. The third arguement is how much 
    greeness will be added to the the pixels in the peace sign as an integer. 
    The fourth arguement is how much blueness will be added to the the pixels in 
    the peace sign as an integer. The Fifth arguement will be entered as an 
    integer which is thw width and height of the border from the pictures edges 
    in pixels. The sixth arguement is entered as a string with the word name of 
    the color but only works with common color names. the seventh and final 
    arguement is the image of the mask you would like to use and this is the 
    image that wil have altered color spaces on the final image. This arguement 
    must be entered as a string filepath to the image with black to represent 
    the color-shift sections and transparancy to represent the untouched 
    sections'''

    directory = os.path.dirname(os.path.abspath(__file__)) + '/Project_Images'
    img_pil = original_image
    img = np.asarray(img_pil).copy()
    height = len(img)
    width = len(img[0])
    image_pixel_count = height * width
    for r in range(height):
        for c in range(width):
            if ((img[r][c][0]) > (255-Redness)):
                img[r][c][0] = 255
            else:
                img[r][c][0] = (img[r][c][0]) + Redness
                
            if ((img[r][c][1]) > (255-Greeness)):
                img[r][c][1] = 255
            else:
                img[r][c][1] = (img[r][c][1]) + Greeness
                
            if ((img[r][c][2]) > (255-Blueness)):
                img[r][c][2] = 255
            else:
                img[r][c][2] = (img[r][c][2]) + Blueness

    unbordered_img_pil = PIL.Image.fromarray(img)
    Logo_pil = PIL.Image.open('../Logo.PNG')
    peace_mask = PIL.Image.open(pick_mask).resize(original_image.size)
    original_image.paste(unbordered_img_pil, (0,0), mask=peace_mask)
    bordered_image = ImageOps.expand(original_image, border=Border_size, fill=border_color)
    bordered_image.paste(Logo_pil, (0, 0))
    return bordered_image
    

def edit_all_images(Redness = 0, Greeness = 90, Blueness = 0, Border_size = 200, border_color = 'red', pick_mask = '../new_peace.png'):
    """This Function runs the edit one function for every picture in the 
    Project_Images folder and places the final image in the modified images 
    folder. This Function takes up to 6 arguements where the first one is how 
    much redness will be added to the the pixels in the peace sign, represented
    as an integer. The second arguement is how much greeness will be added to 
    the the pixels in the peace sign as an integer. The third arguement is how 
    much blueness will be added to the the pixels in the peace sign as an 
    integer. The Fourh arguement will be entered as an integer which is thw 
    width and height of the border from the pictures edges in pixels. The fifth 
    arguement is entered as a string with the word name of the color but only 
    works with common color names. the sixth and final arguement is the image of
    the mask you would like to use and this is the image that wil have altered 
    color spaces on the final image. This arguement must be entered as a string 
    filepath to the image with black to represent the color-shift sections and 
    transparancy to represent the untouched sections"""
    
    directory = os.getcwd()
        
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)
    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        curr_image = image_list[n]
        Filtered_image = RGB_Manuel_Filter_one_image(curr_image, Redness, Greeness, Blueness, Border_size, border_color, pick_mask = '../new_peace.png') 
        new_image_filename = os.path.join(new_directory, filename + '.jpg')
        print(new_image_filename)
        Filtered_image.save(new_image_filename)


def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    Note:This Docstring was made by others
    """
    
    if directory == None:
        directory = os.getcwd()
        
    image_list = []
    file_list = []
    
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    return image_list, file_list


print('How much would you like to increase the redness by?(enter a number from 0-255)')
Redness_increase = int(raw_input(''))
print('How much would you like to increase the greeness by?(enter a number from 0-255)')
Greenness_increase = int(raw_input(''))
print('How much would you like to increase the Blueness by?(enter a number from 0-255)')
Blueness_increase = int(raw_input(''))
print('How Thick(in pixles) would you like your border to be?(enter a positive number')
Border_thickness = int(raw_input(''))
print('What color do you want your border to be?(preferably enter a word)')
Border_color = raw_input('')
print('Would you like to use a custom watermark image?, If yes you must use a \
true transparency image(using custom image is highly unreccomended unless you \
know what you are doing. Y/N)')
picked_mask_y_n = raw_input('')
if (picked_mask_y_n=='Y'):
    print('Please type out the what the picture is called, includiong where it \
    is in the file tree')
    picked_mask = raw_input('')
else:
    picked_mask = '../new_peace.png'
edit_all_images(Redness_increase, Greenness_increase, Blueness_increase, Border_thickness, Border_color, picked_mask)