import cmpt120imageProj

img = cmpt120imageProj.getImage("week9-photo.jpg")

def flipHorizontal(image):
    height = len(image[0])
    width = len(image)
    for y in range(height):
        for x in range(width // 2):
            temp = image[x][y]
            image[x][y] = image[width - x - 1][y]
            image[width - x - 1][y] = temp
    return (image)

newImg = flipHorizontal(img)

cmpt120imageProj.showImage(newImg, "flipped")