import microbit

# using the \ character at the end of a string tells Python to
# keep looking for more of the string on the next line, and
# concatenates the strings automatically for you

my_image = "03030:" \
           "05050:" \
           "07070:" \
           "09090:" \
           "00000"

boat = microbit.Image(my_image)
microbit.display.show(boat)