"""Wszystkie stałe występujące w programie."""
# pylint: disable=no-member

import pygame
pygame.init()  # konieczne dla fontów

# Okno i opcje---------------------------------------------------------------------------

# kolor tła okna
BACKGROUND_COLOR = (41, 39, 36)  # ciemny
# rozdzielczości okna
RESOLUTIONS = [(800, 600), (1200, 800)]
# tryb wyświetlania okna
FULLSCREEN = [0, pygame.FULLSCREEN]
# limity FPS'ów
FPS_LIMIT = [200, 300, 500]

# Czcionki-------------------------------------------------------------------------------

FONT_HEADINGS = pygame.font.SysFont(None, 60) # czcionka nagłówków
FONT_OPTIONS = pygame.font.SysFont(None, 40) # czcionka tekstów z menu'sów

# Piłka----------------------------------------------------------------------------------
BALL_SPEED = 3 # prędkość poruszania piłki
# wymiary piłki
BALL_WIDTH = 15
BALL_HEIGHT = 15
# początkowe współrzędne piłki
BALL_START_X = 50
BALL_START_Y = 100
# kolor piłki
BALL_COLOR = (255, 15, 35)  # czerwony

# Racket-----------------------------------------
# wymiary paletki
RACKET_WIDTH = 80
RACKET_HEIGHT = 16
# kolor paletki
RACKET_COLOR = (70, 150, 60)  # ciemna zieleń

# Block------------------------------------------
# wymiary klocków
BLOCK_WIDTH = 96
BLOCK_HEIGHT = 25
# kolor klocków
BLOCK_COLOR = (34, 105, 125)  # niebieski

# Przyciski------------------------------------------------------------------------------

# wymiary przycisków
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80

# kolor przycisków
BUTTON_COLOR = (62, 102, 138)  # niebiesko jakiś

# kolor napisów na przyciskach
BUTTON_TEXT_COLOR = (255, 255, 255)  # biały

# Menusy---------------------------------------------------------------------------------

# menu główne
MAIN_MENU_BUTTONS_NAMES = ["start", "options", "exit"]
MAIN_MENU_COLOR = (223, 240, 235) # białawo-błękitny
MAIN_MENU_HEADLINE = "main menu"
MAIN_MENU_HEADLINE_COLOR = (18, 49, 77)

# menu opcji
SETTINGS_MENU_HEADLINE = "settings"
SETTINGS_MENU_BUTTONS_NAMES = ["difficulty: easy", "resolution: 800x600", "fullscreen: off",
                               "main menu"]

# menu porażki
GAME_OVER_MENU_HEADLINE = 'game over'
GAME_OVER_MENU_BUTTONS_NAMES = ["try again", "main menu", "exit"]
GAME_OVER_MENU_COLOR = (219, 83, 100)  # czerwono jakiś
GAME_OVER_MENU_HEADLINE_COLOR = (0, 0, 0)

# menu pauzy
PAUSE_MENU_HEADLINE = 'pause'
PAUSE_MENU_BUTTONS_NAMES = ["continue", "main menu", "exit"]
PAUSE_MENU_COLOR = (0, 0, 0)
PAUSE_MENU_HEADLINE_COLOR = (0, 0, 0)

# menu zwycięstwa
WIN_MENU_HEADLINE = 'You won!'
WIN_MENU_BUTTONS_NAMES = ["main menu", "exit"]
WIN_MENU_COLOR = (139, 191, 128)  # zielono jakiś
WIN_MENU_HEADLINE_COLOR = (0, 255, 0)

# Sędzia---------------------------------------------------------------------------------

# położenie napisu z pozostałymi życiami
LIFES_STATUS_X = 20
LIFES_STATUS_Y = 100
LIFES_COLOR = (255, 255, 255)
