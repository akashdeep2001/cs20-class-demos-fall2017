# red remover

import cImage as image

img = image.Image("luther.jpg")
width = img.getWidth()
height = img.getHeight()

win = image.ImageWin("Red is Gone", width, height)

img.draw(win)

for y in range(height):
    for x in range(width):
        this_pixel = img.getPixel(x, y)
        
        if x > width/2 and y > height/2:
            new_red = 0
            new_green = this_pixel.getGreen()
            new_blue = this_pixel.getBlue()
        else:
            average = (this_pixel.getRed() + this_pixel.getGreen() + this_pixel.getBlue())/3
            new_red = int(average)
            new_green = int(average)
            new_blue = int(average)
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        
        img.setPixel(x, y, new_pixel)        
    
    # if you don't want it to animate, unindent this line below:
    img.draw(win)
