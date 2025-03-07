import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """子弹类"""
    def __init__(self, ai_obj):
        """子弹类初始化函数"""
        super().__init__()

        self.screen = ai_obj.screen
        self.settings = ai_obj.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_obj.ship.image_rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        """更新子弹位置"""
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹矩形"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    