import microbit

arrow_image_list = [microbit.Image.ARROW_N, microbit.Image.ARROW_NE, microbit.Image.ARROW_E, microbit.Image.ARROW_SE, microbit.Image.ARROW_S, microbit.Image.ARROW_SW, microbit.Image.ARROW_W, microbit.Image.ARROW_NW, microbit.Image.SURPRISED]

while True:
    for this_image in arrow_image_list:
        microbit.display.show(this_image)
        microbit.sleep(250)
