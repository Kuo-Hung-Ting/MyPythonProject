"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage

window = GWindow(width=800, height=400)
def main():
    """
    TODO:
    """
    background = GRect(800,400)
    background.filled = True
    background.color = 'red'
    background.fill_color = 'red'
    window.add(background)
    head = GOval(100, 50)
    head.filled = True
    head.color = 'white'
    head.fill_color = 'white'
    window.add(head, x=200-head.width/2, y=50-head.height/2)
    eye_l = GOval(20,20)
    eye_l.filled = True
    eye_l.color = 'black'
    eye_l.fill_color = 'black'
    window.add(eye_l, x=180-eye_l.width/2, y=50-eye_l.height/2)
    eye_r = GOval(20, 20)
    eye_r.filled = True
    eye_r.color = 'black'
    eye_r.fill_color = 'black'
    window.add(eye_r, x=220 - eye_r.width / 2, y=50 - eye_r.height / 2)
    nose = GRect(43, 5)
    nose.filled = True
    nose.color = 'black'
    nose.fill_color = 'black'
    window.add(nose, x=200-nose.width/2, y=50-nose.height/2)
    body = GOval(130,160)
    body.filled = True
    body.color = 'white'
    body.fill_color = 'white'
    window.add(body, x=200 - body.width / 2, y=140 - body.height / 2)
    left_feet = GOval(60, 120)
    left_feet.filled = True
    left_feet.color = 'white'
    left_feet.fill_color = 'white'
    window.add(left_feet, x=170 - left_feet.width / 2, y=220 - left_feet.height / 2)
    right_feet = GOval(60, 120)
    right_feet.filled = True
    right_feet.color = 'white'
    right_feet.fill_color = 'white'
    window.add(right_feet, x=230 - right_feet.width / 2, y=220 - right_feet.height / 2)
    left_arm = GOval(60, 120)
    left_arm.filled = True
    left_arm.color = 'white'
    left_arm.fill_color = 'white'
    window.add(left_arm, x=140 - left_arm.width / 2, y=160 - left_arm.height / 2)
    right_arm = GOval(60, 120)
    right_arm.filled = True
    right_arm.color = 'white'
    right_arm.fill_color = 'white'
    window.add(right_arm, x=260 - right_arm.width / 2, y=160 - right_arm.height / 2)
    quoted = GImage("quote.png")
    window.add(quoted, x=330, y=2)
    print("Title: Baymax \n\nBaymax is a healthcare companion that can\nhelp you fix your feelings!")



if __name__ == '__main__':
    main()
