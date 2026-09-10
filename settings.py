class Settings:
    """编写设置模块"""
    def __init__(self):
        """设置屏幕"""
        self.screen_width = 1200   #屏幕长度
        self.screen_height = 800    #屏幕宽度
        self.screen_color = (230, 230, 230)    #屏幕背景颜色

        """设置飞船速度"""
        self.ship_moving_speed = 1.2

        """设置子弹"""
        self.bullet_moving_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 250, 100)
        self.bullets_allowed = 3

        """设置飞船"""
        self.aliens_speed = 1