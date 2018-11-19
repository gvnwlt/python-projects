import tkinter 
import tkinter.messagebox

### create window object -- liken to jframe ###
# window size (w x h)
window = tkinter.Tk()
window.title("Tkinter Lib Template")
window.geometry("400x400")

### text in window ### 
# label = tkinter.Label(window, text = "Hellow World!").pack()

### buttons and widgets ###
# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# now, create some widgets in the top_frame and bottom_frame
# btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack()# 'fg - foreground' is used to color the contents
# btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()# 'text' is used to write the text on the Button
# btn3 = tkinter.Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
# btn4 = tkinter.Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

### file menu ###
def function():
    pass

# creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu) # it intializes a new su menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
file_menu.add_command(label = "New file.....", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator() # it adds a line after the 'Open files' option
file_menu.add_command(label = "Exit", command = window.quit)

# creting another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)
### File menu end ###

### simple alert box and response input ###
#tkinter.messagebox.showinfo("Alert Message", "This is just an alert message!")
#response = tkinter.messagebox.askquestion("Simple Question", "1 for YES 0 for NO")
#if response == 1:
#    tkinter.Label(window, text = "response = YES").pack()
#else:
#    tkinter.Label(window, text = "response = NO").pack()

# render image
window.mainloop()