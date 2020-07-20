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

        # 飞船设置
        self.ship_limit = 3
        
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 外星人设置
        self.fleet_drop_speed = 10
        # 击败一个外星人获得分数的提高速度
        self.score_scale = 1.5

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.3

        # 最高得分
        self.high_score = 0

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        # 记分
        self.alien_points = 50

        # fleet_direction为1表示向右移，为-1表示左移
        self.fleet_direction = 1
        '''随游戏的进行，我们将提高这些速度，而每当玩家开始新游戏时，都将重置这些速度。'''
    
    def increase_speed(self):
        '''提高速度设置 和 外星人点数'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)



'''
每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为settings的模块，
其中包含一个名为Settings的类，用于将所有设置存储在一个地方，以免在代码中到处添加设置。
这样，我们就能传递一个设置对象，而不是众多不同的设置。另外，这让函数调用更简单，且在
项目增大时修改游戏的外观更容易：要修改游戏，只需修改settings.py中的一些值，而无需查找
散布在文件中的不同设置。
'''