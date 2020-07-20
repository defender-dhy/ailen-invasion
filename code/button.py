import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        '''初始化按钮的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''将msg渲染成图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self): 
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect) 
        self.screen.blit(self.msg_image, self.msg_image_rect) 



'''Pygame没有内置创建按钮的方法，我们创建一个Button类，用于创建带标签的实心矩形。
你可以在游戏中使用这些代码来创建任何按钮'''
'''
- 模块pygame.font，它让Pygame能够将文本渲染到屏幕上。
- self.font处，实参None让Pygame使用默认字体，而48
指定了文本的字号。为让按钮在屏幕上居中，我们创建一个表示按钮的rect对象（见），并将
其center属性设置为屏幕的center属性。
- Pygame通过将你要显示的字符串渲染为图像来处理文本。在处，我们调用prep_msg()来处
理这样的渲染。
'''
'''
prep_msg()接受实参self以及要渲染为图像的文本（msg）。调用font.render()将存储在
msg中的文本转换为图像，然后将该图像存储在msg_image中。方法font.render()还接受
一个布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）。余下的两
个实参分别是文本颜色和背景色（如果没有指定背景色，Pygame将以透明背景的方式渲染文本）

让文本图像在按钮上居中：根据文本图像创建一个rect，并将其center属性设
置为按钮的center属性。
'''
'''
调用screen.fill()来绘制表示按钮的矩形，再调用screen.blit()，并向它传递一幅图
像以及与该图像相关联的rect对象，从而在屏幕上绘制文本图像。
'''