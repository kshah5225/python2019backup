'''Procedure'''
#1-3 N/A
'''Part I: Using Arrays of Pixels'''
#4 an list is a type of array but not every array is a list.
#5 len(img[0])      len(img[1])     img[4][10][0]       img[24][49][0]
#from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import PIL


'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
            
height = len(img)
width = len(img[0])
for r in range(418, 470):
    for c in range(125, 160):
        if sum(img[r][c])>420: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,0] # R + B = magenta

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 127, 127, 0] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 126] # magenta, alpha=255
    return image



# Show the image data in a subplot
if __name__ == "__main__":
    image2 = make_mask(1080*4,1920*4,50*8)
    
ax[0].imshow(img, interpolation='none')
ax[1].imshow(image2, interpolation='none')
# Saves the figure
fig.savefig('1.4.3/woman and mask')