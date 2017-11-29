# red remover

import cImage as image

img = image.Image("luther.jpg")
width = img.getWidth()
height = img.getHeight()

win = image.ImageWin("Red is Gone", width, height)

img.draw(win)

for x in range(width):
    for y in range(height):
        this_pixel = img.getPixel(x, y)
        
        new_red = 0
        new_green = this_pixel.getGreen()
        new_blue = this_pixel.getBlue()
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        
        img.setPixel(x, y, new_pixel)        
    
    # if you don't want it to animate, unindent this line below:
    img.draw(win)
