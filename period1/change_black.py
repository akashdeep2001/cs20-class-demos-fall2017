# remove sky

import cImage as image

img = image.Image("moon.jpg")
width = img.getWidth()
height = img.getHeight()

win = image.ImageWin("Goodnight Moon", width, height)

img.draw(win)

for y in range(height):
    for x in range(width):
        this_pixel = img.getPixel(x, y)
        
        r = this_pixel.getRed()
        g = this_pixel.getGreen()
        b = this_pixel.getBlue()
        
        if r+g+b < 50:
            new_red = 255
            new_green = 255
            new_blue = 255
        else:
            new_red = this_pixel.getRed()
            new_green = this_pixel.getGreen()
            new_blue = this_pixel.getBlue()
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        
        img.setPixel(x, y, new_pixel)        
    
    # if you don't want it to animate, unindent this line below:
    img.draw(win)

