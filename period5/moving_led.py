import microbit

def make_image(led_location):
    """Takes in a location for which pixel should be turned on on the bottom row.
        Returns a micro:bit Image object to display.
        Note that the location of the pixels should be one of:
            01234"""
    upper_portion_of_grid = "00000:00000:00000:00000:"
    possible_bottom_row_values = ["90000", "09000", "00900", "00090", "00009"]
    image_string = upper_portion_of_grid + possible_bottom_row_values[led_location]

    # to understand what this function is doing, uncomment the print statement below
    # print(image_string)

    return microbit.Image(image_string)

x_cor = 2
current_image = make_image(x_cor)
microbit.display.show(current_image)

while True:
    if microbit.button_a.is_pressed():
        if x_cor > 0:
            x_cor -= 1
            print(x_cor)
            current_image = make_image(x_cor)
            microbit.display.show(current_image)
            microbit.sleep(250)

    if microbit.button_b.is_pressed():
        if x_cor < 4:
            x_cor += 1
            print(x_cor)
            current_image = make_image(x_cor)
            microbit.display.show(current_image)
            microbit.sleep(250)
