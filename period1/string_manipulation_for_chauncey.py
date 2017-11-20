import microbit
import time

def build_bottom_row(x_cor):
    bottom_row_string = ""
    for i in range(5):
        if i == x_cor:
            bottom_row_string = bottom_row_string + "9"
        else:
            bottom_row_string = bottom_row_string + "0"
    return bottom_row_string

def build_image(x_cor):
    image_string = ""
    for row in range(4):
        image_string = image_string + "00000:"
    last_row = build_bottom_row(x_cor)
    image_string = image_string + last_row
    return image_string

x_cor = 3
the_image = build_image(x_cor)

while True:
    if microbit.button_a.is_pressed():
        x_cor -= 1
        the_image = build_image(x_cor)
        mb_image = microbit.Image(the_image)
        microbit.display.show(mb_image)
        time.sleep(0.5)
        
    if microbit.button_b.is_pressed():
        x_cor += 1
        the_image = build_image(x_cor)
        mb_image = microbit.Image(the_image)
        microbit.display.show(mb_image)
        time.sleep(0.5)
    