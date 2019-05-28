'''Procedure'''
#1-4    N/A
#5      use %run ../mask.py to run mask.py
#       round_corners_of_all_images(directory=None)
#       get_images(directory=None)
#       round_corners_one_image(original_image, percent_of_side=.3)
#6      The function went through all the images and rounded the corners of all 
#       the images and counts out what number it son using print
#7a     2, First is a image name with its path and the second calculates how
#       much to round the corners
#       Argument 1:a image name with its path
#       Argument  2:the ratio of circle size to picture to increace or decreace 
#       the roundedness of the corner
#       Return value: A picture file in the modified folder with corners rounded
#7b     purple
#7c     purple mask, cuts out the corners from the mask to make rounded edges
#7d     256
#7e     33-38 makes the two rectangles whereas the next couplre of lines are 
#       creating the circles for rounded corners
#7f     The image is black
#7g     (any number, any number, any number, 255)
#8a     1 or 0
#8b     40 file names and 40 names of the saved file directory
#8c     os.getcwd()
#       os.listdir(directory)
#       os.path.join(directory, entry)
#8d     Return a string representing the current working directory.
#       Return a list containing the names of the entries in the directory given
#       by path. The list is in arbitrary order. It does not include the special
#       entries '.' and '..' even if they are present in the directory.
#8e     