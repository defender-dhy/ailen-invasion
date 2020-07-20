import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    '''显示得分信息的类'''

    def __init__(self, ai_settings, screen, stats):

        """初始化显示得分涉及的属性""" 
        self.screen = screen 
        self.screen_rect = screen.get_rect() 
        self.ai_settings = ai_settings 
        self.stats = stats 

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 36)

        # 准备初始得分图像 && 最高得分图像 && 等级图像 && 剩余飞船
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = round(self.stats.score, -1)
        score_str = "score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                self.ai_settings.bg_color)
        
        # 将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 60
        '''函数round()通常让小数精确到小数点后多少位，其中小数位数是由第二个实参指定的。然
        而，如果将第二个实参指定为负数，round()将圆整到最近的10、100、1000等整数倍。
        {:,}".format(rounded_score)让Python将数值转换为字符串时在其中插入逗号'''
    
    def prep_high_score(self):
        '''将最高分转换为一幅渲染的图像'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "highest score: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高分放在顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级转换为一幅渲染图像'''
        self.level_image = self.font.render("level: "+str(self.stats.level), True, 
                    self.text_color, self.ai_settings.bg_color)
        
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        '''显示还剩下多少飞船'''
        self.ships = Group()
        for ship_member in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_member * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
        '''prep_ships()创建一个空编组self.ships，用于存储飞船实例。为填充这个编组，
        根据玩家还有多少艘飞船运行一个循环相应的次数，'''

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # 绘制飞船
        self.ships.draw(self.screen)



'''将要显示的文本转换为图像，我们调用了prep_score()'''