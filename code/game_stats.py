class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        with open('./high_score.txt','r') as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1



'''不直接在__init()__中初始化大部分统计信息，而是加了reset_stats()方法
这样，在玩家开始新游戏时也能调用reset_stats()，而不是再设置一个新的实例'''
