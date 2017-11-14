import microbit
while True:
    if microbit.pin0.is_touched():
        microbit.display.show("T")
        microbit.sleep(500)
        microbit.display.clear()