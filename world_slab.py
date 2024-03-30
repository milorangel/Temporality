import pygame
from random import choice
from rotate_center import rot_center

class World_Slab(pygame.sprite.Sprite):
    world_slabs = []
    def __init__(self, x, y, object_instances, WIDTH, HEIGHT, scale=4):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.image = pygame.image.load('image/deco/world_slab_grass.png')
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))

        angle = choice((0, 90, 180, -90))
        self.image = rot_center(self.image, angle)
        self.rect = self.image.get_rect(center=(x, y))

        World_Slab.world_slabs.append(self)
        object_instances.append(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect.center)
