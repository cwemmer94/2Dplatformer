from pyray import *

from player import Player


def main():
    init_window(800, 600, "Game")
    set_target_fps(60)
    player = Player()

    player.compose()
    while not window_should_close():
        #update
        player.update(get_frame_time())

        #Render code
        begin_drawing()
        clear_background(SKYBLUE)
        draw_rectangle(0,400,800,200,GREEN)
        player.render()
        draw_fps(10,10)
        end_drawing()
    player.dispose()
    close_window()

if __name__ == "__main__":
    main()