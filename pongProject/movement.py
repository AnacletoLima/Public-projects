from turtle import Screen
from paddle import Paddle


class Movement:
    def __init__(self):
        self.keys_pressed = set()
        self.actions = dict(
            rpu=lambda: self.r_paddle.move_up(),
            rpd=lambda: self.r_paddle.move_down(),
            lpu=lambda: self.l_paddle.move_up(),
            lpd=lambda: self.l_paddle.move_down(),
        )

        self.screen = Screen()

        self.screen.tracer(0)

        self.frame_delay_ms = 1000 // 30  # default for turtle is 10 in _CFG["delay"]

        self.r_paddle = Paddle(350, 0)
        self.l_paddle = Paddle(-350, 0)

        self.screen.listen()

        self.screen.onkeypress(lambda: self.keys_pressed.add("rpu"), "Up")
        self.screen.onkeypress(lambda: self.keys_pressed.add("rpd"), "Down")
        self.screen.onkeypress(lambda: self.keys_pressed.add("lpu"), "w")
        self.screen.onkeypress(lambda: self.keys_pressed.add("lpd"), "s")

        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("rpu"), "Up")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("rpd"), "Down")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("lpu"), "w")
        self.screen.onkeyrelease(lambda: self.keys_pressed.remove("lpd"), "s")

    def tick(self):
        for action in self.keys_pressed:
            self.actions[action]()
        self.screen.update()
        self.screen.ontimer(self.tick, self.frame_delay_ms)
