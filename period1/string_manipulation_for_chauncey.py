x_cor = 3
bottom_row_string = ""
for i in range(5):
    if i == x_cor:
        bottom_row_string = bottom_row_string + "9"
    else:
        bottom_row_string = bottom_row_string + "0"

print(bottom_row_string)