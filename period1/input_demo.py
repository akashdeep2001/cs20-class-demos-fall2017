from appJar import gui

#I'm not describing this properly just yet...
app = gui()

first_name = app.textBox("First", "What's your first name?")
last_name = app.textBox("Name", "What's your last name?")

print('''Hi there, ''' + first_name + " " + last_name + "!")

