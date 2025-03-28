#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame.font import Font
import pygame
from Code.Const import WIN_WIDTH, COLOR_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0  # Start at the first menu option
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            # Loop through MENU_OPTION and highlight the selected option
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Handle events (Quit and Key Down for navigation)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

                if event.type == pygame.KEYDOWN:
                    # Handle Down key to go down the menu
                    if event.key == pygame.K_DOWN:
                        menu_option += 1
                        if menu_option >= len(MENU_OPTION):
                            menu_option = 0  # Wrap to the top option
                    # Handle Up key to go up the menu
                    elif event.key == pygame.K_UP:
                        menu_option -= 1
                        if menu_option < 0:
                            menu_option = len(MENU_OPTION) - 1  # Wrap to the bottom option
                    if event.key == pygame.K_RETURN: 
                        return MENU_OPTION[menu_option]

            

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    
