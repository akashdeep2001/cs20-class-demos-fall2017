import microbit

list_of_images = [microbit.Image.RABBIT, microbit.Image.COW, microbit.Image.DUCK]

while True:
    for this_image in list_of_images:
        microbit.display.show(this_image)
        microbit.sleep(250)
    