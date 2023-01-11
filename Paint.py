from tkinter import *
from tkinter import colorchooser,filedialog,messagebox,Scale
from PIL import ImageGrab

window = Tk()
window.state("zoomed")
window.title("Paint Application")

# Default Settings
pen_color = "black"
eraser_color = "white"

# Canvas
canvas = Canvas(window, bg="white", bd=5, relief=GROOVE, height=650, width=1520)
canvas.place(x=0,y=100)

# Functions

def canvas_color():
    global eraser_color
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color=color[1]   # sets the eraser to have the same color as the background

def save():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
    x = window.winfo_rootx() + canvas.winfo_x()
    y = window.winfo_rooty() + canvas.winfo_y()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Paint Notification", "Image saved as" + str(file_name))

def eraser():
    global pen_color
    pen_color = eraser_color

def clear():
    canvas.delete("all")

def paint(event):
    x1,y1 = (event.x-2),(event.y-2)
    x2,y2 = (event.x+2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=pen_color,outline=pen_color,width=pen_size.get())

canvas.bind("<B1-Motion>", paint)

def select_color(col):
    global pen_color
    pen_color = col

# Frame
color_frame = LabelFrame(window, text="Colors", relief=RIDGE, bg="white", width=500, font=("arial", 15, "bold"))
color_frame.place(x=10, y=10, width=425, height=60)

tool_frame = LabelFrame(window, text="Tools", relief=RIDGE, bg="white", width=500, font=("arial", 15, "bold"))
tool_frame.place(x=434, y=10, width=198, height=60)

pen_size = LabelFrame(window, text="Size", relief=RIDGE, bg="white", width=500, font=("arial", 15, "bold"))
pen_size.place(x=630, y=10, width=225, height=70)

# Colors
colors = [
    "#FF0000",  # RED
    "#800080",  # PURPLE
    "#FFC0CB",  # PINK
    "#FFA500",  # ORANGE
    "#FFFF00",  # YELLOW
    "#008000",  # GREEN
    "#0000FF",  # BLUE
    "#85C1E9",  # SKY BLUE
    "#800000",  # BROWN
    "#FFFFFF",  # WHITE
    "#000000",  # BLACK
    "#808080",  # GREY
]
# Colors Button
i = j = 0
for color in colors:
    Button(color_frame, bd=3, bg=color, relief=RIDGE, width=3, command=lambda col=color:select_color(col)).grid(row=j, column=i, padx=1)
    i += 1

# Tools Button
canvas_color_b1 = Button(tool_frame, text="Canvas", bd=4, bg="white", relief=RIDGE, command=canvas_color)
canvas_color_b1.grid(row=0, column=0, padx=2)

save_b2 = Button(tool_frame, text="Save", bd=4, bg="white", relief=RIDGE, command=save)
save_b2.grid(row=0, column=1,)

eraser_b3 = Button(tool_frame, text="Eraser", bd=4, bg="white", relief=RIDGE, command=eraser)
eraser_b3.grid(row=0, column=2,padx=2)

clear_b4 = Button(tool_frame, text="Clear", bd=4, bg="white", relief=RIDGE, command=clear)
clear_b4.grid(row=0, column=3,padx=2)


# Pen and Eraser Size
pen_size = Scale(pen_size, orient=HORIZONTAL, from_=0, to=100, length=170)
pen_size.set(1)
pen_size.grid(row=0, column=0)

window.mainloop()
