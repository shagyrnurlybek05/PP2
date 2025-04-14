import pygame
import sys

pygame.init()

# ---------- Настройкасы ----------
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 100, 255)
RED = (200, 50, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scene Manager Demo")
clock = pygame.time.Clock()

# ---------- Класс ----------
class Scene:
    def __init__(self):
        pass

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

# ---------- Басты меню ----------
class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont(None, 60)

    def handle_events(self, events):
        global current_scene
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                current_scene = GameScene()

    def draw(self, screen):
        screen.fill(BLACK)
        text = self.font.render("ENTER ды бас ойынды бастау үшін", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))

# ---------- Ойын сценасы ----------
class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(WIDTH//2 - 25, HEIGHT//2 - 25, 50, 50)
        self.speed = 5

    def handle_events(self, events):
        global current_scene
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_scene = GameOverScene()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, self.rect)

# ---------- Ойын біткен сценасы----------
class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont(None, 60)

    def handle_events(self, events):
        global current_scene
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                current_scene = MainMenu()

    def draw(self, screen):
        screen.fill(RED)
        text = self.font.render("Ойын бітті!  R ды бас бастау үшін", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))

# ---------- Ойынды бастау ----------
current_scene = MainMenu()

while True:
    events = pygame.event.get()
    current_scene.handle_events(events)
    current_scene.update()
    current_scene.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
