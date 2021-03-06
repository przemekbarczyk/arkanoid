"""Moduł zawierający klase rakietki."""

import pygame

from game_module import constants


class Racket:
    """Klasa rakietki gracza:

    Porusza się w osi X sterowana przez gracza za pomocą myszy."""

    def __init__(self):
        """Konstruktor inicjalizuje zmienne i tworzy powierzchnie piłki."""

        self.width = constants.RACKET_WIDTH
        self.height = constants.RACKET_HEIGHT
        self.x_cord = 0
        self.y_cord = constants.RESOLUTIONS[0][1] - 40
        self.color = constants.RACKET_COLOR

        # konfiguruje kształt rakietki
        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(self.color)  # pokolorowanie powierzchni
        # ustawienie prostokąta zawierającego obiekt w początkowej pozycji
        self.rect = self.surface.get_rect(x=int(self.x_cord), y=int(self.y_cord))

    def move(self, x_cord, window):
        """Przesuwa rakietkę o wyznaczone miejsce."""

        # wyznacza przesunięcie paletki gracza
        x_cord_new = x_cord - (self.width / 2)  # wyznacza nowe współrzędne paletki

        # paletka wykracza poza okno gry w prawo
        if x_cord_new > window.width - self.width:
            x_cord_new = window.width - self.width
        # paletka wykracza poza okno gry w lewo
        elif x_cord_new < 0:
            x_cord_new = 0

        # aktualizuje położenie paletki w poziomie
        self.rect.x = round(x_cord_new)

    def update(self, window):
        """Aktualizuje położenie paletki po zmianie rozdzielczości."""

        self.y_cord = window.height - 40
        self.rect = self.surface.get_rect(x=int(self.x_cord), y=int(self.y_cord))

    def draw(self, window):
        """Rysuje piłkę w oknie."""

        window.surface.blit(self.surface, self.rect)
