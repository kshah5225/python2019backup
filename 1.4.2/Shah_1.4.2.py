'''Procedure'''
#1-3 N/A
'''Part I: for loops, range(), and help()'''
#4 you would use C:/Users/Student login/Desktop/nice.jpg
#5 ../Student login/Desktop/nice.jpg
#6 absolute and you dont need to be in a particular directory for this to work
#  In cloud nine it us unix based so you dont use c:/ and uou yse just /
#7 
'''The old code didnt work and gave an display error because cloud 9 is non gui
we no longer use fig.show and we use matplotlib.use('Agg') which makes it work
in an non-gui enviorment'''
# I dont see it in my folder because it saves into my overall folder
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''''''''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/women_plot')'''

#7a (275,400)

'''
JDoe_JSmith_1_4_2: Read and show an image.
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/filename')
#saves above plot as caat1-a_plot in 1.4.2
'''

#7b (60,40)

'''Part III: Objects and Methods'''

#8aFigure, AxesSubplot
#8bsavefig, fig, 'women plot', filename
#9aimshow, ax[0]
#9bi
'''
''''''Read the image data''''''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/two women')
#saves above plot as caat1-a_plot in 1.4.2

#9bii
''''''Read the image data''''''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/five_cats')'''
#saves above plot as caat1-a_plot in 1.4.2

#11a IDK
'''Read the image data'''
'''# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
'''
'''Show the image data'''
'''# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img,)
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(35, 49)
ax[0].set_ylim(80, 70)
ax[0].set_xticks([36,38,40,42,44])
ax[1].set_xlim(45, 55)
ax[1].set_ylim(80, 76)
ax[1].set_xticks([46,48,50,52,54])
#ax[1].minorticks_off()
ax[2].set_xlim(25, 65)
ax[2].set_ylim(80, 79)
ax[2].set_xticks([56,58,60,62,64])
#ax[2].minorticks_off()

# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/experiment')
#saves above plot as cat1-a_plot in 1.4.2
'''

#11b
'''Read the image data'''
'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

''''''Show the image data''''''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(35, 45)
ax[0].set_ylim(80, 70)
ax[0].set_xticks([36,38,40,42,44])
#ax[0].minorticks_off()
ax[1].set_xlim(45, 55)
ax[1].set_ylim(80, 70)
ax[1].set_xticks([46,48,50,52,54])
#ax[1].minorticks_off()
ax[2].set_xlim(55, 65)
ax[2].set_ylim(80, 70)
ax[2].set_xticks([56,58,60,62,64])
#ax[2].minorticks_off()

# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/three closeup')
#saves above plot as cat1-a_plot in 1.4.2
'''
#12 There is a way to set and convert units found :
#   https://matplotlib.org/api/axes_api.html#axis-scales

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img, interpolation='none')
ax[1].plot(39, 50, 'ro')
ax[1].plot(118, 44, 'ro')

# Show the figure on the screen
# fig.show()
fig.savefig('1.4.2/crazy_mice.png')
#saves above plot as cat1-a_plot in 1.4.2

