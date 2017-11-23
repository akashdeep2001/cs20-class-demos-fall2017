import microbit

count = 0

while True:
    if microbit.button_a.was_pressed():
        count = count + 1
        print(count)