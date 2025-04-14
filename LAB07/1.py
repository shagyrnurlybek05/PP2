import pygame
import time
import math

pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Название окна
pygame.display.set_caption("Mickey clock")

# Загрузка изображений
leftarm = pygame.image.load('/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB07/Clock images/hour.jpg')
rightarm = pygame.image.load('/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB07/Clock images/minut.jpg')
mainclock = pygame.transform.scale(pygame.image.load('/Users/shagyrnurlybek/Documents/GitHub/PP2/LAB07/Clock images/clock.jpg'), (800, 600))

# Масштабируем стрелки
rightarm = pygame.transform.scale(rightarm, (650, 600))  
leftarm = pygame.transform.scale(leftarm, (800, 800))  

done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Получаем текущее время
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Вычисляем углы стрелок
    minute_angle = - (minute * 6 + (second / 60) * 6)  
    second_angle = - (second * 6)  

    # Очищаем экран
    screen.fill((255, 255, 255))

    # Отображаем фон (часы)
    screen.blit(mainclock, (0, 0))

    # Вращаем и отображаем стрелки
    rotated_rightarm = pygame.transform.rotate(rightarm, minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(400, 300))
    screen.blit(rotated_rightarm, rightarmrect)

    rotated_leftarm = pygame.transform.rotate(leftarm, second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(400, 300))
    screen.blit(rotated_leftarm, leftarmrect)

    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS

pygame.quit()
