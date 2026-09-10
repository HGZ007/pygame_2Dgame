import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """创建外星人飞船"""
    def __init__(self,ai_game):
        """初始化外星飞船的设置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """添加外星飞船的图片"""
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        """设置外星人的的边距和他们的位置。"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """设置其精确位置"""
        self.x = float(self.rect.x)

    def update(self):
        """控制飞船移动"""
        self.x += self.settings.aliens_speed
        self.rect.x = self.x