import pygame
import random
import sys

pygame.init()

HEIGHT = 600
WIDTH = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


road = pygame.image.load(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/AnimatedStreet.png")
coin_i = pygame.image.load(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/Coin.png")
coin_im = pygame.transform.scale(coin_i, (100, 100))
player_im = pygame.image.load(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/Player.png")
enemy_im = pygame.image.load(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/Enemy.png")  


pygame.mixer.music.load(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/lab08_resources_background.wav")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/lab08_resources_coin.mp3")
crash_sound = pygame.mixer.Sound(r"/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB08/Resources/lab08_resources_crash.wav")  

font = pygame.font.SysFont("Verdana", 30)
count = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_im
        self.speed = 5
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 10)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_im
        self.speed = 7
        self.rect = self.image.get_rect()
        self.generate() 

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_im
        self.speed = 8
        self.rect = self.image.get_rect()
        self.generate()

    def generate(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.width)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate()


player = Player()
coin = Coin()
enemy = Enemy()

all_sprites = pygame.sprite.Group(player, coin, enemy)
coin_sprites = pygame.sprite.Group(coin)
enemy_sprites = pygame.sprite.Group(enemy)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player.move()
    coin.move()
    enemy.move()
    
    if pygame.sprite.spritecollideany(player, coin_sprites):
        coin_sound.play()
        count += 1
        coin.generate()


    if pygame.sprite.spritecollideany(player, enemy_sprites):
        crash_sound.play()
        pygame.time.delay(1000)

        screen.fill((255, 0, 0))
        game_over_text = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    
    screen.blit(road, (0, 0))
    all_sprites.draw(screen)
    

    score_text = font.render(f"Score: {count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)