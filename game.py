import time
from snake import Snake
from game_screen import GameScreen

class Game:
    def __init__(self):
        self.game_screen = GameScreen()
        self.snake = Snake()
        self.game_over = False
        


    def start_game(self):
        while not self.game_over:
            time.sleep(0.2)
            self.snake.move()
            self.game_screen.screen.update()

        self.game_screen.screen.mainloop()   