import pygame
from pygame.sprite import Sprite
class Bullets(Sprite):
    """创建子弹类，并且编组"""
    def __init__(self, ai_game):
        """创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullet_color = ai_game.settings.bullet_color

        """创建子弹像素"""
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        """创建子弹浮点数"""
        self.y = float(self.rect.y)

    def update(self):
        """更新子弹的位置,子弹向上移动"""
        self.y -= self.settings.bullet_moving_speed

        """将子弹的浮点数转换成像素位数"""
        self.rect.y = self.y

    def draw_bullet(self):
        """画出子弹在屏幕的图像"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)