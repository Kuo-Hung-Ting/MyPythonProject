"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.lives = 0
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width - paddle_width) / 2, y=window_height - paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width - self.ball.width) / 2, y=(window_height - self.ball.height) / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.run = True
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)
        # Draw bricks
        for i in range(2):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = 'red'
                self.window.add(self.bricks, x=j * brick_width + (j - 1) * brick_spacing,
                                y=i * brick_height + (i - 1) * brick_spacing + brick_offset)
        for i in range(2):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = 'orange'
                self.window.add(self.bricks, x=j * brick_width + (j - 1) * brick_spacing,
                                y=(i+2) * brick_height + (i + 1) * brick_spacing + brick_offset)
        for i in range(2):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = 'yellow'
                self.window.add(self.bricks, x=j * brick_width + (j - 1) * brick_spacing,
                                y=(i+4) * brick_height + (i + 3) * brick_spacing + brick_offset)
        for i in range(2):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = 'green'
                self.window.add(self.bricks, x=j * brick_width + (j - 1) * brick_spacing,
                                y=(i+6) * brick_height + (i + 5) * brick_spacing + brick_offset)
        for i in range(2):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                self.bricks.fill_color = 'blue'
                self.window.add(self.bricks, x=j * brick_width + (j - 1) * brick_spacing,
                                y=(i+8) * brick_height + (i + 7) * brick_spacing + brick_offset)



    def paddle_move(self, event):
        if event.x - self.paddle.width < 0:
            self.paddle.x = 0
        elif event.x + self.paddle.width/2 > self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x - self.paddle.width / 2


    def ball_move(self, event):
        # window_width = BRICK_COLS * (BRICK_WIDTH + BRICK_SPACING) - BRICK_SPACING
        # window_height = BRICK_OFFSET + 3 * (BRICK_ROWS * (BRICK_HEIGHT + BRICK_SPACING) - BRICK_SPACING)
        if self.__dx == 0 and self.__dy == 0:
            self.run = True
        if self.run:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.run = False
            self.lives += 1



    def get_dx(self):
        window_width = BRICK_COLS * (BRICK_WIDTH + BRICK_SPACING) - BRICK_SPACING
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        if self.ball.y + self.ball.height >= self.window.height:
            self.__dx = 0
            self.ball.x = (window_width - self.ball.width) / 2


        return self.__dx
    def get_run(self):
        return self.run
    def get_dy(self):
        window_height = BRICK_OFFSET + 3 * (BRICK_ROWS * (BRICK_HEIGHT + BRICK_SPACING) - BRICK_SPACING)
        # or self.ball.y + self.ball.height >= self.window.height
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        if self.ball.y + self.ball.height >= self.window.height:
            self.ball.y = (window_height - self.ball.height) / 2
            self.__dy = 0

        return self.__dy

    def hit_dy(self):
        self.__dy = -self.__dy
        return self.__dy

    def hit_dx(self):
        self.__dx = -self.__dx
        return self.__dx

    def ball_radius(self):
        return BALL_RADIUS

    def total(self):
        return BRICK_COLS*BRICK_ROWS

    def live(self):
        return self.lives