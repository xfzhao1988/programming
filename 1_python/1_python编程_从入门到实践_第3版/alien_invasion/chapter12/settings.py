class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)

        # 飞船移动速度
        self.ship_speed = 1.5

        # 飞船发射的子弹相关配置
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_speed = 5
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        
    
    
