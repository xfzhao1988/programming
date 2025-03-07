import sys
import pygame

from settings import Settings
from rocket import Rocket


class RocketGame():
    """火箭游戏类"""
    def __init__(self):
        """火箭游戏类初始化"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)
        
    def run_game(self):
        """运行游戏"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.left_moving_flag = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.right_moving_flag = True
        elif event.key == pygame.K_UP:
            self.rocket.top_moving_flag = True
        elif event.key == pygame.K_DOWN:
            self.rocket.down_moving_flag = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.left_moving_flag = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.right_moving_flag = False
        elif event.key == pygame.K_UP:
            self.rocket.top_moving_flag = False
        elif event.key == pygame.K_DOWN:
            self.rocket.down_moving_flag = False

    def _update_screen(self):
        self.screen.fill(self.settings.screen_bg_color)
        
        self.rocket.update_position()
        self.rocket.display()

        pygame.display.flip()

if __name__ == "__main__":
    rg = RocketGame()
    rg.run_game()