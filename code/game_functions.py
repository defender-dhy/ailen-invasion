# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:23:04 2020

@author: 86178
"""

import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹""" 
    #创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
   

def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                    
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

        
def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
 
    # 让最近绘制的屏幕可见
    pygame.display.flip() 
     
    
def update_bullets(bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    # 更新子弹位置
    bullets.update()
    
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

            
# 读取属性event.key，以检查按下的是否是右箭头键（pygame.K_RIGHT）
'''
方法bullets.sprites()返回一个列表，其中包含编组bullets中的所有精灵。为在屏幕上绘制发射的
所有子弹，我们遍历编组bullets中的精灵，并对每个精灵都调用draw_bullet()
'''
