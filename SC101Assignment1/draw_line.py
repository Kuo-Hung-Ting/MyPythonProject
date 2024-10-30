"""
File: 
Name:郭紘廷
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


line = False
SIZE = 5
circle_x = 0
circle_y = 0

window = GWindow(800, 500, title='draw_line.py')

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global line, circle_x, circle_y
    if line == False:
        pen_stroke = GOval(SIZE, SIZE)
        pen_stroke.filled = False
        pen_stroke.color = 'black'
        window.add(pen_stroke, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        circle_x = mouse.x
        circle_y = mouse.y
        line = True
    else:
        pen_stroke = GLine(circle_x, circle_y, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
        pen_stroke.filled = False
        pen_stroke.color = 'black'
        maybe_mole = window.get_object_at(circle_x, circle_y)
        window.remove(maybe_mole)
        window.add(pen_stroke)
        line = False



if __name__ == "__main__":
    main()
