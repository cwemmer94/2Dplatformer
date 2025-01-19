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
        #gravity ground
        if self.ypos < 400 - 50:
            self.vely += 15
        else:
            self.vely = 0
            self.ypos = 400 - 50

        #gravity on platform
        if self.ypos == 300 and self.xpos == 400:
            pass
        else:
            self.vely = 0
            self.ypos == 300 and self.xpos == 400

        #movement
        if is_key_down(KEY_LEFT):
            self.velx = -350
        elif is_key_down(KEY_RIGHT):
            self.velx = 350
        else:
            self.velx = 0


        #jump
        if is_key_down(KEY_UP) and self.ypos == 400 - 50:
            self.vely = -500
        #move and slide
        self.xpos += self.velx * delta
        self.ypos += self.vely * delta
    def render(self):
        draw_rectangle(int(self.xpos), int(self.ypos), 50,70,WHITE)
    def dispose(self):
        pass