from pathlib import Path
class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 60
        self.ship_h = 80
        self.ship_speed = 8

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'green_beam.png'
        self.laser_sound =  Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 10
        self.bullet_w = 50
        self.bullet_h = 50
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 3
        self.fleet_direction = 1
        self.fleet_drop_speed = 40