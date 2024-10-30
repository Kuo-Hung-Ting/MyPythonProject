"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 3  # Number of attempts
BALL_RADIUS = 10


def main():
    global dx, dy
    graphics = BreakoutGraphics()
    total = graphics.total()
    # Add the animation loop here!
    while True:
        if total == 0:
            dx = 0
            dy = 0
            break
        lives = graphics.live()
        if NUM_LIVES - lives <= 0:
            dx = 0
            dy = 0
            break
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        hit = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        if hit is not None:
            if hit is not graphics.paddle:
                graphics.window.remove(hit)
                dx = graphics.hit_dx()
                dy = graphics.hit_dy()
                total -= 1
            else:
                dy = graphics.hit_dy()
        elif graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius(), graphics.ball.y) is not None:
            hit = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius(), graphics.ball.y)
            if hit is not graphics.paddle:
                graphics.window.remove(hit)
                dx = graphics.hit_dx()
                dy = graphics.hit_dy()
                total -= 1
            else:
                dy = graphics.hit_dy()
        elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius()) is not None:
            hit = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius())
            if hit is not graphics.paddle:
                graphics.window.remove(hit)
                dx = graphics.hit_dx()
                dy = graphics.hit_dy()
                total -= 1
            else:
                dy = graphics.hit_dy()
        elif graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius(),
                                           graphics.ball.y + 2 * graphics.ball_radius()) is not None:
            hit = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius(),
                                                graphics.ball.y + 2 * graphics.ball_radius())
            if hit is not graphics.paddle:
                graphics.window.remove(hit)
                dx = graphics.hit_dx()
                dy = graphics.hit_dy()
                total -= 1
            else:
                dy = graphics.hit_dy()

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
