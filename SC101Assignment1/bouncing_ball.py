"""
File: 
Name:郭紘廷
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
click = True
count = 0
oval = GOval(SIZE, SIZE)
cur_y = window.height-START_Y

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    oval.filled = True
    oval.color = 'black'
    oval.fill_color = 'black'
    window.add(oval, START_X, START_Y)
    onmouseclicked(start)


def start(event):
    global click, cur_y, count
    if click and count < 3:
        cur_y = window.height - START_Y
        vy = 0
        click = False
        while oval.x < window.width:
            while oval.y < window.height:
                vy += GRAVITY
                oval.move(VX, vy)
                pause(DELAY)
            vy = -vy
            cur_y *= REDUCE
            while oval.y > window.height-cur_y:
                vy += GRAVITY
                oval.move(VX, vy)
                pause(DELAY)
            vy = -vy
        count += 1
        oval.x = START_X
        oval.y = START_Y
        click = True



if __name__ == "__main__":
    main()
