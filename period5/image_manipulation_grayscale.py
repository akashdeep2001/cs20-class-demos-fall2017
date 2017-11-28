import cImage as image

img = image.Image("morgan.jpg")
win = image.ImageWin("Grayscale", img.getWidth(), img.getHeight())
img.draw(win)

for col in range(img.getWidth()):
    for row in range(img.getHeight()):
        p = img.getPixel(col, row)

        average = int( (p.getRed() + p.getGreen() + p.getBlue())/3 )
        
        new_red = average
        new_green = average
        new_blue = average

        new_pixel = image.Pixel(new_red, new_green, new_blue)

        img.setPixel(col, row, new_pixel)

    # redrawing the image after each row allows us to see how the image is being changed
    # you can move this outside the for loop if you don't want to watch the process
    img.draw(win)

img.save("morgan-grayscale.jpg")