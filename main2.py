#Take user input (0/1/2/3/4) using a while loop to determine which manipulation options (2/3/4) they want to apply.
#If the user enters 0, the program exits
#if the user enters 1, show the original image*
#if the user enters 2/3/4, perform the manipulation, then show the result image*
#if the user enters something other than the expected input (e.g., 5), display the message 
# “Sorry, I don’t understand 5” and take the user input again.



import cmpt120imageProj as lib
import cmpt120imageManip as res

img = lib.getImage("week9-photo.jpg")

#input_message = "Press 0 to Exit\nPress 1 to show the original image\nPress 2 to Invert the colours\nPress 3 to Cover bottom Half in black\nPress 4 to flip image horizontally\n"

input_message = "0: exit\n1: Show orig\n2: Invert\n5: RR\n6: RB\n7: RG\n8: CTG\n9:AS\n10:DB\n11:IB\n"

ans = int(input(input_message))

while(ans != 0):
    if ans == 1:
        img = lib.getImage("week9-photo.jpg")
        lib.showImage(img, "Original Image")

    elif ans == 2:
        new_img = img
        new_img = res.invert(new_img)
        lib.showImage(new_img, "Inverted Image")


    elif ans == 3:
        new_img = res.flipVertical(img)
        lib.showImage(new_img, "Flipped Vertical")

    elif ans == 4:
        new_img = res.flipHorizontal(img)
        lib.showImage(new_img, "Flipped Horizontal")

    elif ans == 5:
        new_img = res.removeRed(img)
        lib.showImage(new_img, "Red Removed")

    elif ans == 6:
        new_img = res.removeBlue(img)
        lib.showImage(new_img, "Blue Removed")

    elif ans == 7:
        new_img = res.removeGreen(img)
        lib.showImage(new_img, "Green Removed")

    elif ans == 8:
        new_img = res.convToGrayscale(img)
        lib.showImage(new_img, "Grayscale")

    elif ans == 9:
        new_img = res.applySepia(img)
        lib.showImage(new_img, "Sepia")

    elif ans == 10:
        new_img = res.decreaseBrightness(img)
        lib.showImage(new_img, "Decreased Brightness")
    elif ans == 11:
        new_img = res.increaseBrightness(img)
        lib.showImage(new_img, "Increased Brightness")
    else:
        print("Sorry, your input is invalid.")

    ans = int(input(input_message))