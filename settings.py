from pathlib import Path
class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 60
        self.ship_h = 80

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'green_beam.png'
        self.laser_sound =  Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound =  Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 50
        self.alien_h = 50
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (252, 231, 40)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20

        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'


    def initialize_dynamic_settings(self):
        self.ship_speed = 8
        self.starting_ship_count = 3

        self.bullet_w = 50
        self.bullet_h = 50
        self.bullet_speed = 10
        self.bullet_amount = 5

        self.fleet_speed = 3
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
