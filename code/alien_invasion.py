# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:15:17 2020

@author: 86178
"""


import pygame 
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game(): 
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion") 
        
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    
    # 开始游戏的主循环
    while True: 
        
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹
        gf.update_bullets(bullets)           
        # 刷新屏幕        
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game() 


# pygame.init()初始化背景设置，让Pygame能够正确地工作
# 调用pygame.display.set_mode()来创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制。
# 实参(1200, 800)是一个元组，指定了游戏窗口的尺寸。
"""
# 对象screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。在这
# 个游戏中，每个元素（如外星人或飞船）都是一个surface。display.set_mode()返回的surface表
# 示整个游戏窗口。我们激活游戏的动画循环后，每经过一次循环都将自动重绘这个surface。
"""
# 游戏由一个while循环控制，其中包含一个事件循环以及管理屏幕更新的代码。
# 为访问Pygame检测到的事件，我们使用方法pygame.event.get()。所有键盘和鼠标事件都将促使for循环运行。
"""
# pygame.display.flip()，命令Pygame让最近绘制的屏幕可见。在这里，它在每次
# 执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在我们移动游戏元
# 素时，pygame.display.flip()将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，
# 从而营造平滑移动的效果。
"""

# 填充背景后，用ship.blitme()将飞船绘制到屏幕上，确保它出现在背景前面

# bullets:在check_events()中，需要在玩家按空格键时处理bullets；而在update_screen()中，需要更新要绘制到屏幕上的bullets。
# 当你对编组调用update()时，编组将自动对其中的每个精灵调用update()，因此代码行bullets.update()将为编组bullets中的每颗子弹调用bullet.update()
