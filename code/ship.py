# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:47:34 2020

@author: 86178
"""

import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 储存小数值
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
        
    def blitme(self): 
        """在指定位置绘制飞船""" 
        self.screen.blit(self.image, self.rect) 
        
# rect的centerx等属性只能存储整数值，因此我们需要对Ship类做些修改(增加self.center)



# __init__()接受两个参数：引用self和screen，其中后者指定了要将飞船绘制到什么地方。
# pygame.image.load(),这个函数返回一个表示飞船的surface，而我们将这个surface存储到了self.image中
# 加载图像后，我们使用get_rect()获取相应surface的属性rect。
# 像处理矩形一样处理游戏元素十分高效，这种做法的效果通常很好，游戏玩家几乎注意不到我们处理的不是游戏元素的实际形状。
# 在Pygame中，原点(0, 0)位于屏幕左上角，在1200×800的屏幕上，原点位于左上角，而右下角的坐标为(1200, 800)
