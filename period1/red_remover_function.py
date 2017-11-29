# red remover function
# this version works on the textbook

import image

def red_remover(original_image, window):
    width = original_image.getWidth()
    height = original_image.getHeight()
    new_image = image.EmptyImage(width, height)
    
    for x in range(width):
        for y in range(height):
            this_pixel = original_image.getPixel(x, y)

            new_red = 0
            new_green = this_pixel.getGreen()
            new_blue = this_pixel.getBlue()

            new_pixel = image.Pixel(new_red, new_green, new_blue)

            new_image.setPixel(x, y, new_pixel)  
        #comment out the line below to stop animating this
        new_image.draw(window)
    return new_image


img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())

converted_img = red_remover(img, win)
converted_img.draw(win)
