import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1010
        self.bg_color = (230, 230, 230)
        self.bg = pygame.image.load('images/space.jpg')
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.bullet_speed_factor = 3
        self.bullet_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 => right, -1 => left
        self.fleet_direction = 1

        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction = 1 => right, -1 => left
        self.fleet_direction = 1
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
