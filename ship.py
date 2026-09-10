import pygame

class Ship:
    """创建一个飞船实例"""
    def __init__(self, ai_game):
        """将游戏屏幕surface加入成飞船的属性"""
        self.screen = ai_game.screen
        # 提取屏幕像素
        self.screen_rect = ai_game.screen.get_rect()

        """获取图片"""
        self.image = pygame.image.load('ship.bmp')
        # 提取飞船像素
        self.rect = self.image.get_rect()

        """确定图片的位置"""
        self.rect.midbottom = self.screen_rect.midbottom

        """连续移动"""
        self.moving_right = False
        self.moving_left = False

        """存储一个浮点数——换一个变量"""
        self.x = float(self.rect.x)

        """连接settings文件和此文件"""
        self.settings = ai_game.settings

    def blitme(self):
        """将图片填充至屏幕中"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            """向右移动"""
            self.x += self.settings.ship_moving_speed

        elif self.moving_left and self.rect.left > 0:
            """向左移动"""
            self.x -= self.settings.ship_moving_speed

        self.rect.x = self.x

