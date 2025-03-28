#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtle import position
from Code.Const import WIN_WIDTH
from Code.background import Background
class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, postion =(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                     list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                     list_bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            
