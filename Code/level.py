#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from Code.entity1 import Entity
from Code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            pygame.display.flip()
        pass
