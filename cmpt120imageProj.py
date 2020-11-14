'''

The User Interface controls how information is being presented to the user,
and how the program receives and processes user input.
It uses some of the functions provided in the cmpt120imageProject module.
The most notable ones are:

getImage – loads an image from the computer into the program as a 2D R/G/B array
saveImage – saves an image represented as a 2D R/G/B array to the computer
showInterface – displays the image represented as a 2D R/G/B array to a window (user interface),
together with the caption and the instruction text
At any point in time the user interface shows all possible options the user can choose from.
There are two parts in the options:

The “system” options – these options include Quit, Open Image, Save Current Image, and Reload
Original Image. They are always available to the user and are selected by the characters Q/O/S/R.

The “manipulation” options – these options vary depending on which mode the user is at:
Basic, Intermediate, and Advanced. See below for which options are available to the user.
They are selected by numbers.

'''
import cmpt120imageManip


# system options: Quit, Open Save Current Image, Reload
def sys_Quit(loopVar):
    loopVar = False
    return loopVar

def sys_OpenImage(image, title):
    cmpt120imageManip.showImage(image, title)

def sys_SaveCurrentImage(image, title):
    cmpt120imageManip.saveImage(image, title)

def sys_ReloadOriginalImage(original, manipulated):
    manipulated = cmpt120imageManip.getImage(original)
    return manipulated
