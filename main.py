# 屏幕尺寸      height, width

SCREEN_SIZE = (10, 32)
# 0 ↑ 1 ↓ 2 ← 3 →
# 默认蛇向上移动
SNAKE_DIRECTION = 0
# 屏幕数据缓存
SCREEN_BUFFER = None
GAME_START = True

def init_screen():
    global SCREEN_BUFFER
    SCREEN_BUFFER = [["□" for _ in range(SCREEN_SIZE[1])] for _ in range(SCREEN_SIZE[0])]


def show_buffer():

    output_string = ""
    for y in range(SCREEN_SIZE[0]):
        for x in range(SCREEN_SIZE[1]):
            output_string += SCREEN_BUFFER[y][x]
        output_string += "\n"
    print(output_string, flush=True)

import keyboard
import time
if __name__ == "__main__":
    init_screen()
    while GAME_START:
        show_buffer()
        if keyboard.press("esc"):
            GAME_START = False
        time.sleep(1)