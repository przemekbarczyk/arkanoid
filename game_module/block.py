"""Moduł zawierający klase klocków."""

import pygame

from game_module import constants


class Block:
    """Klasa klocka:

    Klocek posiada swoje współrzędne, wymiary i kolor. Jeden obiekt = jeden klocek."""

    def __init__(self, x, y):
        """Konstruktor inicjalizuje zminne i tworzy powierzchnie klocka."""

        self.width = constants.BLOCK_WIDTH
        self.height = constants.BLOCK_HEIGHT
        self.color = constants.BLOCK_COLOR

        self.surface = pygame.Surface([self.width, self.height])  # utworzenie powierzchni obiektu
        self.surface.fill(constants.BLOCK_COLOR) # pokolorowanie powierzchni
        # ustawienie prostokąta zawierającego obiekt w początkowej pozycji
        self.rect = self.surface.get_rect(x=x, y=y)

    def draw(self, window):
        """Rysuje pojedyńczy klocek w oknie."""

        window.surface.blit(self.surface, self.rect)
