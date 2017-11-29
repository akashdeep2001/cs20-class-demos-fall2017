# import the module so we can access images
import cImage as image

# open an image (needs to be in the same folder as this file)
cat = image.Image("cat.jpg")

# figure out how large the image is
width = cat.getWidth()
height = cat.getHeight()

# make a window to draw on
the_window = image.ImageWin("Funny looking cat", width, height)

# use a nested for loop to look at every pixel in the image
for y in range(height):
    for x in range(width):
    
        # get the current pixel
        this_pixel = cat.getPixel(x, y)
        
        # red -> green value
        # green -> blue value
        # blue -> red value
        
        # access the amount of red, green and blue for this pixel
        r = this_pixel.getRed()
        g = this_pixel.getGreen()
        b = this_pixel.getBlue()
        
        new_r = int(r*.393 + g*.769 + b*.189)
        new_g = int(r*.349 + g*.686 + b*.168)
        new_b = int(r*.272 + g*.534 + b*.131)

        # create a new pixel with changed values
        new_pixel = image.Pixel(new_r, new_g, new_b)
        
        # reassign the pixel value in the image to be the changed version
        cat.setPixel(x, y, new_pixel)

    # draw the changed image to the window
    cat.draw(the_window)
