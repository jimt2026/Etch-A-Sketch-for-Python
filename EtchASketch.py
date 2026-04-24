#EtchASketch.py

from tkinter import *

print("W, A, S, D to draw. C to clear canvas.")

canvas_height = 600
canvas_width = 600
canvas_colour = "black"

window = Tk()
window.title("Canvas")
canvas = Canvas(bg=canvas_colour, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()

p1_x = int(canvas_width/2)
p1_y = int(canvas_height)
p1_colour = "green"
line_width = 5
line_length = 5

def p1_move_N(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y-line_length, fill=p1_colour, width=line_width)
    p1_y = p1_y - line_length

def p1_move_S(event):
    global p1_y
    canvas.create_line(p1_x, p1_y, p1_x, p1_y+line_length, fill=p1_colour, width=line_width)
    p1_y = p1_y + line_length

def p1_move_E(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x+line_length, p1_y, fill=p1_colour, width=line_width)
    p1_x = p1_x + line_length

def p1_move_W(event):
    global p1_x
    canvas.create_line(p1_x, p1_y, p1_x-line_length, p1_y, fill=p1_colour, width=line_width)
    p1_x = p1_x - line_length

def clear_canvas(event):
    canvas.delete("all")

canvas.bind_all('<w>', p1_move_N)
canvas.bind_all('<s>', p1_move_S)
canvas.bind_all('<d>', p1_move_E)
canvas.bind_all('<a>', p1_move_W)
canvas.bind_all('<c>', clear_canvas)

window.mainloop()