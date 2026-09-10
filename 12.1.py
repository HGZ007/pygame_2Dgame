import pygame
import sys
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien

class Mygame:
    def __init__(self):
        """创建基本信息"""
        pygame.display.set_caption('')
        self.clock = pygame.time.Clock()
        pygame.init()

        """导入设置模块"""
        self.settings = Settings()

        """导入长度"""
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))

        """导入子弹"""
        self.bullets = pygame.sprite.Group()

        """导入飞船元素"""
        self.ship = Ship(self)

        """导入外星人飞船元素"""
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """运行游戏程序"""
        while True:
            self.check_events()     #控制键盘操作
            self.ship.update()      #控制飞船连续操作
            self._bullet_update()   #控制子弹
            self.update_aliens()
            self.update_screen()    #控制屏幕
            self.clock.tick(120)    # 控制帧率

    def check_events(self):
        """控制键盘输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """检查代码是否退出"""
                sys.exit()

            if event.type == pygame.KEYDOWN:
                """判断飞船是否连续移动"""
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                """判断飞船连续移动是否结束"""
                self.check_keyup_events(event)

    def check_keydown_events(self , event):
        """判断飞船是否连续移动"""
        if event.key == pygame.K_RIGHT:
            # 飞船连续向右移动
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            # 飞船连续向左移动
            self.ship.moving_left = True

        elif event.key == pygame.K_q:    #只有在全屏模式下的唯一方式
            #按q键退出游戏
            sys.exit()

        elif event.key == pygame.K_SPACE:
            """发射子弹"""
            self._fire_bullet()

    def check_keyup_events(self , event):
        """判断飞船连续移动是否结束"""
        if event.key == pygame.K_RIGHT:
            # 飞船停止连续向右移动
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            # 飞船连续向左移动
            self.ship.moving_left = False

    def _fire_bullet(self):
        """生产,发射子弹"""
        if len(self.bullets) < self.settings.bullets_allowed:
            """限制子弹的数量"""
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)

    def update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.screen_color)
        for bullet in self.bullets.sprites():
            """更新子弹，将子弹打印在屏幕上"""
            bullet.draw_bullet()

        """将飞船渲染到屏幕上"""
        self.ship.blitme()

        """将外星人飞船渲染到屏幕上"""
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _bullet_update(self):
        """控制子弹"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            """删除子弹"""
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))

    def _create_fleet(self):
        """创建外新人飞船"""
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size   #外星人的宽度

        current_x, current_y = alien_width / 2, alien_height / 2

        while current_y < self.settings.screen_height - 6 * alien_height:
            """在纵轴上创建外星人舰队排"""
            while current_x <= (self.settings.screen_width -
                                3 * (alien_width + 1)) * 3 / 2:
                """在横轴上创建外星人舰队"""
                self._create_alien(current_x, current_y)
                current_x += 3 * alien_width / 2

            current_x = alien_width / 2
            current_y += alien_height * 3 / 2

    def _create_alien(self, x_position, y_position):
        """创建一个新的外星人"""
        new_alien = Alien(self)  # 创建一个新的
        new_alien.x = x_position
        new_alien.rect.x = float(x_position)
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def update_aliens(self):
        """更新外星人的位置"""
        self.aliens.update()

if __name__ == "__main__":
    game = Mygame()
    game.run_game()