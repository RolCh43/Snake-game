import time
from snake import Snake
from game_screen import GameScreen

class Game:
    def __init__(self):
        self.game_screen = GameScreen()
        self.snake = Snake()
        self.game_over = False
        self.direction_changed = False

        self.game_screen.screen.listen()
        self.game_screen.screen.onkey(self.up, "Up")
        self.game_screen.screen.onkey(self.down, "Down")
        self.game_screen.screen.onkey(self.left, "Left")
        self.game_screen.screen.onkey(self.right, "Right")
        


    def start_game(self):
        while not self.game_over:
            time.sleep(0.1)
            self.snake.move()
            self.direction_changed = False
            self.game_screen.screen.update()

        self.game_screen.screen.mainloop()   

    def up(self):
        if not self.direction_changed:
            self.snake.up()
            self.direction_changed = True
   
    def down(self):
        if not self.direction_changed:
            self.snake.down()
            self.direction_changed = True
    
    def left(self):
        if not self.direction_changed:
            self.snake.left()
            self.direction_changed = True
    
    def right(self):
        if not self.direction_changed:
            self.snake.right()
            self.direction_changed = True
