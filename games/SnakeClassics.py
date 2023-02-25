import random
import threading
import time
from queue import Queue

from pynput import keyboard


class SnakeBody:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Game(threading.Thread):
    direction = ''
    _dir = 'Key.right'
    snake = []
    foodX = 0
    foodY = 0
    snake_length = 3
    score = 0
    game_status = True

    def __init__(self, width, height):
        threading.Thread.__init__(self)
        self.width = width
        self.height = height

    def _draw(self):
        box = ''
        food = '\033[0;31m██\33[0m'
        wall = '\033[0;96m██\33[0m'
        body = '\033[0;32m██\33[0m'
        for i in range(0, self.height + 1):
            for j in range(0, self.width + 1):
                if i == 0 or i == self.height or j == 0 or \
                        j == self.width or \
                        (j == self.foodX and i == self.foodY):
                    if j == self.foodX and i == self.foodY:
                        box = box + food
                    else:
                        box = box + wall
                elif self.is_snake_part(i, j):
                    box = box + body
                else:
                    box = box + '  '

            box = box + '\n'
        print(box)

    def is_snake_part(self, i, j):
        for snake_body in self.snake:
            if j == snake_body.x and i == snake_body.y:
                return True
        return False

    def new_food(self):
        i = 0
        self.foodX = int(random.random() * (self.width - 3) + 2)
        self.foodY = int(random.random() * (self.height - 3) + 2)
        k = self.width * self.height
        while i < k:
            if not self.is_snake_part(self.foodX, self.foodY):
                return
            else:
                self.foodX = int(random.random() * (self.width - 3) + 2)
                self.foodY = int(random.random() * (self.height - 3) + 2)
        self.foodX = 0
        self.foodY = 0

    def _start_game(self):
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self.foodX = int(random.random() * (self.width - 3) + 2)
        self.foodY = int(random.random() * (self.height - 3) + 2)
        while True:
            if self.game_status:
                self.movement()
                print()
                print(self.space(self.width - 4) + 'Snake 2D')
                print()
                self._draw()
                m = 2 * self.width + 2 -
                 len(('Snake length : ' + str(self.snake_length))) - len(
                    ("Score : " + str(self.score)))
                x = "Score : " + str(self.score) +
                 self.space(m) + str('Snake length : ' + str(self.snake_length))
                print(x)
                if self.direction == 'Key.esc':
                    break
            else:
                print("Game Over")
                print("Snake Master")
                print(self.score)
                print('Enter space bar to continue......')
                if self.direction == 'Key.space':
                    self.game_status = True
                    self.reset_game()
            time.sleep(0.01)
            print("\033[H\033[J")

    def reset_game(self):
        self.snake.clear()
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self.snake.append(SnakeBody(self.width / 2, self.height / 2))
        self._dir = 'Key.right'
        self.score = 0
        self.snake_length = 3

    @staticmethod
    def space(v):
        s = ''
        for j in range(0, int(v)):
            s = s + ' '
        return s

    def movement(self):
        if self.direction == 'Key.up' and self._dir != 'Key.down':
            self._dir = 'Key.up'
        if self.direction == 'Key.down' and self._dir != 'Key.up':
            self._dir = 'Key.down'
        if self.direction == 'Key.left' and self._dir != 'Key.right':
            self._dir = 'Key.left'
        if self.direction == 'Key.right' and self._dir != 'Key.left':
            self._dir = 'Key.right'
        i = self.snake.__len__() - 1
        while i >= 1:
            self.snake.__getitem__(i).x = self.snake.__getitem__(i - 1).x
            self.snake.__getitem__(i).y = self.snake.__getitem__(i - 1).y
            i = i - 1
        if self._dir == 'Key.up':
            self.snake.__getitem__(0).y = self.snake.__getitem__(0).y - 1
            if self.snake.__getitem__(0).y == 0:
                self.snake.__getitem__(0).y = self.height - 1
        elif self._dir == 'Key.down':
            self.snake.__getitem__(0).y = self.snake.__getitem__(0).y + 1
            if self.snake.__getitem__(0).y == self.height:
                self.snake.__getitem__(0).y = 1
        elif self._dir == 'Key.left':
            self.snake.__getitem__(0).x = self.snake.__getitem__(0).x - 1
            if self.snake.__getitem__(0).x == 0:
                self.snake.__getitem__(0).x = self.width - 1
        elif self._dir == 'Key.right':
            self.snake.__getitem__(0).x = self.snake.__getitem__(0).x + 1
            if self.snake.__getitem__(0).x == self.width:
                self.snake.__getitem__(0).x = 1

        if self.snake.__getitem__(0).x == self.foodX 
        and self.snake.__getitem__(0).y == self.foodY:
            self.snake.append(SnakeBody(0, 0))
            self.new_food()
            self.score = self.score + 8
            self.snake_length = self.snake_length + 1
        if self.head_hits_body():
            self.game_status = False

    def run(self):
        self._start_game()

    def head_hits_body(self):
        for i in range(1, len(self.snake)):
            if self.snake.__getitem__(0).x == self.snake.__getitem__(i).x 
            and self.snake.__getitem__(
                    0).y == self.snake.__getitem__(i).y:
                return True
        return False


if __name__ == '__main__':
    queue = Queue()


    def on_press(self):
        key_pressed = "{0}".format(self)
        queue.put(key_pressed)


    print('Welcome to Snake 2D')
    print('Enter the esc key to exit')
    print('Enter the width and height')
    x_w = int(input())
    h_w = int(input())
    game = Game(50, 30)
    game.start()
    keys = keyboard.Listener(on_press=on_press, args=(queue,))
    keys.start()
    while True:
        value = queue.get()
        Game.direction = value
        if value == 'Key.esc':
            break
