import pygame
import os

# ----------- Конфигурация параметрлері ------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MUSIC_FOLDER = "/Users/shagyrnurlybek/Documents/GitHub/LAB07/Music"
BACKGROUND_IMAGE = "/Users/shagyrnurlybek/Documents/GitHub/LAB07/Music image/TAU.jpeg"
BUTTONS_FOLDER = "Music buttons"

# Кнопкалардың өлшемдері
BUTTON_SIZE = (70, 70)

# Түстер
WHITE = (255, 255, 255)
NAVY_BLUE = (20, 20, 50)
SEMI_TRANSPARENT_BLACK = (0, 0, 0, 150)

# Pygame-ды іске қосамыз
pygame.init()

# ----------- Көмекші функциялар ------------
def load_playlist(music_folder):
    """ Музыка папкасындағы барлық .mp3 файлдарды жүктеу """
    return [os.path.join(music_folder, song) for song in os.listdir(music_folder) if song.endswith(".mp3")]


def load_button_images(folder_path):
    """ Кнопка суреттерін жүктеу және өлшемін өзгерту """
    return {
        'play': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "play.png")), BUTTON_SIZE),
        'pause': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "pause.png")), BUTTON_SIZE),
        'next': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "next.jpeg")), BUTTON_SIZE),
        'previous': pygame.transform.scale(pygame.image.load(os.path.join(folder_path, "back.jpeg")), BUTTON_SIZE),
    }


def draw_text(surface, text, font, color, x, y):
    """ Берілген мәтінді экранға шығару """
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))


def draw_buttons(surface, buttons, is_playing, button_rects):
    """ Кнопкаларды экранға шығару және олардың орындарын сақтау """
    play_x = SCREEN_WIDTH // 2 - 35
    play_y = SCREEN_HEIGHT - 100
    next_x = play_x + 90
    prev_x = play_x - 90

    # Кнопка орындарын сақтау (тінтуірмен басу үшін)
    button_rects['play'] = pygame.Rect(play_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])
    button_rects['next'] = pygame.Rect(next_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])
    button_rects['previous'] = pygame.Rect(prev_x, play_y, BUTTON_SIZE[0], BUTTON_SIZE[1])

    # Кнопкаларды экранға шығару
    surface.blit(buttons['pause'] if is_playing else buttons['play'], (play_x, play_y))
    surface.blit(buttons['next'], (next_x, play_y))
    surface.blit(buttons['previous'], (prev_x, play_y))


def main():
    # Экранды іске қосу
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Nurlybek - Playlist")

    # Қажетті файлдарды жүктеу
    playlist = load_playlist(MUSIC_FOLDER)
    button_images = load_button_images(BUTTONS_FOLDER)
    background = pygame.image.load(BACKGROUND_IMAGE)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Фонды экранға шақтау

    # Қаріп түрін анықтау
    font_song_name = pygame.font.SysFont(None, 24)

    # Музыканың бастапқы күйін сақтау
    current_index = 0
    is_playing = True
    pygame.mixer.music.load(playlist[current_index])
    pygame.mixer.music.play()

    clock = pygame.time.Clock()
    running = True

    # Кнопка орындарын сақтау үшін
    button_rects = {}

    while running:
        screen.blit(background, (0, 0))

        # Төменгі жағына жартылай мөлдір фон қосу (кнопкалар жақсы көріну үшін)
        overlay = pygame.Surface((SCREEN_WIDTH, 120), pygame.SRCALPHA)
        overlay.fill(SEMI_TRANSPARENT_BLACK)  
        screen.blit(overlay, (0, SCREEN_HEIGHT - 120))

        # Қазіргі ойналып жатқан музыканың атын шығару
        current_song_name = os.path.basename(playlist[current_index])
        draw_text(screen, f"Қазір ойнап жатыр: {current_song_name}", font_song_name, WHITE, 20, SCREEN_HEIGHT - 110)

        # Кнопкаларды экранға шығару және олардың орындарын жаңарту
        draw_buttons(screen, button_images, is_playing, button_rects)

        pygame.display.update()
        clock.tick(30)

        # Оқиғаларды өңдеу
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Ойнату/тоқтату
                    if is_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    is_playing = not is_playing

                elif event.key == pygame.K_RIGHT:  # Келесі әнге өту
                    current_index = (current_index + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

                elif event.key == pygame.K_LEFT:  # Алдыңғы әнге қайту
                    current_index = (current_index - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

            elif event.type == pygame.MOUSEBUTTONDOWN:  # Тінтуірмен басу
                mouse_pos = pygame.mouse.get_pos()
                
                if button_rects['play'].collidepoint(mouse_pos):  # Play/Pause кнопкасы
                    if is_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    is_playing = not is_playing

                elif button_rects['next'].collidepoint(mouse_pos):  # Келесі ән
                    current_index = (current_index + 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

                elif button_rects['previous'].collidepoint(mouse_pos):  # Алдыңғы ән
                    current_index = (current_index - 1) % len(playlist)
                    pygame.mixer.music.load(playlist[current_index])
                    pygame.mixer.music.play()
                    is_playing = True

    pygame.quit()


if __name__ == "__main__":
    main()
