# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import numpy

# Basic Functions:

def invertImage(image):
    # code
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return image

def flipVertical(image):
    height = len(image[0])
    width = len(image)
    for x in range(width):
        for y in range(height//2):
            temp = image[x][y]
            image[x][y] = image[x][height-y-1]
            image[x][height-y-1] = temp
    return (image)


def flipHorizontal(image):
    height = len(image[0])
    width = len(image)
    for y in range(height):
        for x in range(width // 2):
            temp = image[x][y]
            image[x][y] = image[width - x - 1][y]
            image[width - x - 1][y] = temp
    return (image)

# Intermediate Functions

def removeRed(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[0] = 0
    return image

def removeGreen(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[1] = 0
    return image

def removeBlue(image):
    for pixelRow in image:
        for pixel in pixelRow:
            pixel[2] = 0
    return image

def convToGrayscale(image):
    for pixelRow in image:
        for pixel in pixelRow:
            sumAvg = int((pixel[0]+pixel[1]+pixel[2])/3)
            for i in range(3):
                pixel[i] = sumAvg
    return image

def applySepia(image):
    for pixelRow in image:
        for pixel in pixelRow:
            SepiaRed = int((pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189))
            SepiaGreen = int((pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168))
            SepiaBlue = int((pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131))

            if(SepiaRed > 255):
                SepiaRed = 255
            if(SepiaGreen > 255):
                SepiaGreen = 255
            if(SepiaBlue > 255):
                SepiaBlue = 255

            pixel[0] = SepiaRed
            pixel[1] = SepiaGreen
            pixel[2] = SepiaBlue
    return image

def decreaseBrightness(image):
    for pixelRow in image:
        for pixel in pixelRow:
            for i in range(3):
                if pixel[i]>=10:
                    pixel[i] = pixel[i]-10
    return image

def increaseBrightness(image):
    for pixelRow in image:
        for pixel in pixelRow:
            for i in range(3):
                if pixel[i]<=245:
                    pixel[i] = pixel[i] + 10
    return image

# Advanced Functions
def rotateLeft(image):
    #code
    new_image = image

def rotateRight(image):
    #code
    a = "test"

def pixelate(image):
    redTotal = 0
    greenTotal = 0
    blueTotal = 0
    height = len(image[0]) - len(image[0])%4
    width = len(image) - len(image)%4
    for y in range(0, height, 4):
        for x in range(0, width, 4):
            for i in range(4):
                for j in range(4):
                    redTotal += image[x+i][y+j][0]
                    greenTotal += image[x+i][y+j][1]
                    blueTotal += image[x+i][y+j][2]
            for i in range(4):
                for j in range(4):
                    image[x+i][y+j][0] = int(redTotal/16)
                    image[x+i][y+j][1] = int(greenTotal/16)
                    image[x+i][y+j][2] = int(blueTotal/16)
            redTotal = 0
            greenTotal = 0
            blueTotal = 0

    return (image)

def binarize(image):
    #code
    a = "test"