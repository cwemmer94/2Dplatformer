from pyray import *
from raylib.defines import KEY_LEFT, KEY_RIGHT, KEY_UP


class Player:
    xpos = 0
    ypos = 0
    velx = 0
    vely = 0
    speed = 5

    def compose(self):
        pass
    def update(self,delta):
        #gravity
        if self.ypos < 400 - 50:
            self.vely += 5
        else:
            self.vely = 0
            self.ypos = 400 - 50

        #movement
        if is_key_down(KEY_LEFT):
            self.velx = -500
        elif is_key_down(KEY_RIGHT):
            self.velx = 500
        else:
            self.velx = 0

        #jump
        if is_key_down(KEY_UP) and self.ypos == 400 - 50:
            self.vely = -300
        #move and slide
        self.xpos += self.velx * delta
        self.ypos += self.vely * delta
    def render(self):
        draw_rectangle(int(self.xpos), int(self.ypos), 50,50,WHITE)
    def dispose(self):
        pass