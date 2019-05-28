'''Procedure'''
#1-12 N/A
#13     matplotlib.pyplot(plt) - This is used for managing different files
#       numpy (np) - good at being able to measure and dectect values nessecary 
#       to manipulate an image
#       PIL - can convert an image to raw and easily manipulatable data values
#15a    Line 19 calls the function plt.subplots from the plt library. The 
#       function is being called with 2 argument(s): (1, 2). The function
#       returns 1 object(s), which is/are being assigned to ax.
#15b    Line 23 calls imshow() on ax[1]
#       Line 24 calls set_xticks() on ax[1]
#       Line 25 calls set_xlim() on ax[1]
#       Line 26 calls set_ylim() on ax[1]
#       Line 27 calls savefig() on fig
#15c    (1162, 966)
#16ai   upper left(702, 937), bottom right(794, 1017), width = 92, height = 80
#17a    Line 30 uses the join() method from the os.path module. It is being 
#       passed 2 arguments. The value it returns is being assigned to the 
#       variable earth_file.
#17b    In line 31 the open() function of the PIL.Image module returns a new 
#       PIL.Image object, which is being assigned to the variable earth_img.
#17c    One to use it as a tuple and one to show the tuple is part of a resize
#17d    They are used t define the top left corner or bottom right of the 
#       bounding box
#17e(33)Line 33 calls the function subplots from the plt library with 2 
#       argument(s): (1, 2). The function returns 1 object(s), which is/are 
#       being assigned to axes2.
#17e(34)Line 34 calls the method imshow on the object axes2[0] with 1 
#       argument(s): earth_img. 
#17e(35)Line 35 calls the method imshow on the object axes2[1] with 1 
#       argument(s): earth_small.
#17e(36)Line 35 calls the method savefig on the object fig2 with 1 
#       argument(s): 'resize_earth'.
#17fi   reseize to (pixelx, pixely)
#17fii  100, 100?
#17 fiiiinterpolation
#17g    new_width, new_height
#17h    first was original file size the seccond is the scaled down version and 
#       the last one is the original images y
#17i    the second one has smaller numbers and more jagged edges
#18     I think it avg out the R,G,B, and alpha values of a set amount of pixels
#       individually depending on how much space the new pixel takes up of the
#       old img
#19a    15667200, 40000
#19b    done
#19c    206000, 18300kb
#19d    backround compression can give an area of pixels with range for one color
#19e    it outputs as raw values
#19f    they cant read ech other and it is converted to the parent image type
#19g    pastes in order to appear on another image
#20     done

'''Conclusion Questions'''
#1      The major classes used in this lesson is from the PIL library with the 
#       major method used in this lesson being paste and resize used for making 
#       the earth a smaller file and paste allowing us to place an image within 
#       an image
#2      Replacing eyes with earth = make a copy of the image earth called small 
#       earth with a file size of 100 x 100 pixels. Next paste the image as 
#       specified coordinates in relation to the eyes in order to overlay the 
#       earth on her eyes.
