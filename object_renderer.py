import pygame as pg
from settings import  *

class ObjectRenderer:
    def __init__(self, game):
          self.game = game
          self.screen = game.screen
          self.wall_textures = self.load_wall_textures()
          self.sky_image = self.get_texture("resources/textures/sky.png", (WIDTH, HALF_HEIGHT))
          self.sky_offset = 0

    def draw(self):
         self.draw_background()
         self.render_game_objects()

    def draw_background(self):
         self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % WIDTH #debesis
         self.screen.blit(self.sky_image, (-self.sky_offset, 0)) #debesis
         self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0)) #debesis
         #griida
         pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))


    def render_game_objects(self):
         list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
         for depth, image, pos in list_objects:
              self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
         texture = pg.image.load(path).convert_alpha()
         return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
         return {
              1: self.get_texture("resources/textures/1.PNG"),
              2: self.get_texture("resources/textures/2.PNG"),
              3: self.get_texture("resources/textures/3.PNG"),
              4: self.get_texture("resources/textures/4.PNG"),
              5: self.get_texture("resources/textures/5.PNG"),
         }
    
