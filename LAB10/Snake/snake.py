import pygame
import sys
import random
from snake_function import get_or_create_user, save_game, load_last_state
import json

# === USER LOGIN ===
username = input("Введите имя пользователя: ")
user_id = get_or_create_user(username)
last_state = load_last_state(user_id)

pygame.init()
HEIGHT = 600
WIDTH = 600
grid_SIZE = 20
grid_WIDTH = WIDTH // grid_SIZE
grid_HEIGHT = HEIGHT // grid_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()

FOOD_TIMEOUT = 5000
FPS = 5
score = 0
level = 1

myfont = pygame.font.SysFont("monospace", 16)

# Define levels and walls
levels = {
    1: [],  # no walls
    2: [(5, y) for y in range(5, 25)] + [(25, y) for y in range(5, 25)],
    3: [(x, 10) for x in range(10, 20)] + [(x, 20) for x in range(10, 20)]
}

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * grid_SIZE)) % WIDTH), (cur[1] + (y * grid_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        elif (int(new[0] / grid_SIZE), int(new[1] / grid_SIZE)) in levels[level]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        global level, FPS
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        level = 1
        FPS = 5

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (grid_SIZE, grid_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_p:
                    save_game(user_id, score, level, snake.positions, snake.direction, food.position)
                    print("Game paused and saved!")

def drawGrid(surface):
    for y in range(grid_HEIGHT):
        for x in range(grid_WIDTH):
            r = pygame.Rect((x * grid_SIZE, y * grid_SIZE), (grid_SIZE, grid_SIZE))
            color = (170, 215, 81) if (x + y) % 2 == 0 else (162, 209, 73)
            pygame.draw.rect(surface, color, r)
    # Draw walls
    for (wx, wy) in levels[level]:
        wall_rect = pygame.Rect((wx * grid_SIZE, wy * grid_SIZE), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, (120, 120, 120), wall_rect)

class Food:
    def __init__(self):
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_WIDTH - 1) * grid_SIZE,
                         random.randint(0, grid_HEIGHT - 1) * grid_SIZE)
        self.weight = random.randint(1, 3)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_SIZE, grid_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
        font = pygame.font.SysFont("monospace", 16)
        text = font.render(str(self.weight), True, (0, 0, 0))
        text_rect = text.get_rect(center=r.center)
        surface.blit(text, text_rect)

snake = Snake()
food = Food()

if last_state:
    score = last_state[2]
    level = last_state[3]
    snake.positions = json.loads(last_state[4])
    snake.direction = eval(last_state[5])
    food.position = tuple(json.loads(last_state[6]))

while True:
    snake.handle_keys()
    drawGrid(surface)
    snake.move()

    if pygame.time.get_ticks() - food.spawn_time > FOOD_TIMEOUT:
        food.randomize_position()

    if snake.get_head_position() == food.position:
        snake.length += food.weight
        score += food.weight
        FPS += food.weight
        food.randomize_position()
        if score > 10 and level == 1:
            level = 2
        elif score > 25 and level == 2:
            level = 3

    snake.draw(surface)
    food.draw(surface)

    screen.blit(surface, (0, 0))
    text = myfont.render("Player: {}  Score: {}  Level: {}".format(username, score, level), 1, (0, 0, 0))
    screen.blit(text, (5, 10))

    pygame.display.flip()
    clock.tick(FPS)