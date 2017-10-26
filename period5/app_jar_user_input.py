from appJar import gui

#gui stands for Graphical User Interface
app = gui()

first_name = app.textBox("First", "Please enter your first name:")
last_name = app.textBox("Last", "Please enter your last name:")

print("Hi there, " + first_name + " " + last_name + "!")