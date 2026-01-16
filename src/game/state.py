class GameState:
    def __init__(
            self, 
            snake: list[tuple[int, int]], 
            direction: tuple[int, int], 
            food: tuple[int,int], 
            score: int = 0, 
            game_over: bool = False
            ):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.score = score
        self.game_over = game_over

