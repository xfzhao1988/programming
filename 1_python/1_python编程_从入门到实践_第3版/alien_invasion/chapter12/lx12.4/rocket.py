import pygame

class Rocket():
    """火箭类"""
    def __init__(self, rocket_game_obj):
        """火箭类初始化函数"""
        self.screen = rocket_game_obj.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("./images/rocket.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

        self.settings = rocket_game_obj.settings

        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)
        
        # 初始化rocket左右上下移动标志为，默认为false
        self.left_moving_flag = False
        self.right_moving_flag = False
        self.top_moving_flag = False
        self.down_moving_flag = False

    def display(self):
        """将rocket图片显示到screen上"""
        self.screen.blit(self.image, self.image_rect)

    def update_position(self):
        if self.left_moving_flag and self.x > 0:
            self.x -= self.settings.rocket_moving_speed
            if self.x < 0:
                self.x = 0
        if self.right_moving_flag and self.x < self.screen_rect.right:
            self.x += self.settings.rocket_moving_speed
            if self.x > self.screen_rect.right - self.image_rect.width:
                self.x = self.screen_rect.right - self.image_rect.width
        if self.top_moving_flag and self.y > 0:
            self.y -= self.settings.rocket_moving_speed
            if self.y < 0:
                self.y = 0
        if self.down_moving_flag and self.y < self.screen_rect.bottom:
            self.y += self.settings.rocket_moving_speed
            if self.y > self.screen_rect.bottom - self.image_rect.height:
                self.y = self.screen_rect.bottom - self.image_rect.height

        self.image_rect.x = self.x
        self.image_rect.y = self.y