# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 20:59:48 2020

@author: 86178
"""

class Settings():
    '''储存《外星人入侵》的所有设置的类'''
    
    def __init__(self):
        
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5


'''
每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为settings的模块，
其中包含一个名为Settings的类，用于将所有设置存储在一个地方，以免在代码中到处添加设置。
这样，我们就能传递一个设置对象，而不是众多不同的设置。另外，这让函数调用更简单，且在
项目增大时修改游戏的外观更容易：要修改游戏，只需修改settings.py中的一些值，而无需查找
散布在文件中的不同设置。
'''