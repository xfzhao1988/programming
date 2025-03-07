import pygame

class Ship():
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.setting = ai_game.settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("./resources/images/ship.bmp")

        self.image_rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部的中央
        self.image_rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储一个浮点数
        self.x = float(self.image_rect.x)

        # 移动标志（初始化时为False）
        self.moving_right = False
        self.moving_left = False

        
    def update_position(self):
        """更新飞船位置"""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
            if(self.x + self.image_rect.width > self.screen_rect.right):
                self.x = self.screen_rect.right - self.image_rect.width
                print("#######################")
        if self.moving_left and self.image_rect.left > 0:
            self.x -= self.setting.ship_speed
            if(self.x < 0):
                # self.x = 0
                print("$$$$$$$$$$$$$$$$$$$$$$$$$")

        self.image_rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.image_rect)