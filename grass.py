import pygame
from random import randint

class Grass(pygame.sprite.Sprite):
    grasses = []
    pygame.mixer.init()
    grass_sound = pygame.mixer.Sound('sound/rustling_grass_2.mp3')
    image = pygame.image.load('image/deco/grass.png')

    def __init__(self, WIDTH, HEIGHT, object_instances, triggers, scale=2):
        super().__init__()
        self.image = Grass.image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.flip(self.image, randint(0, 1), randint(0, 1))
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect(center=(randint(0, WIDTH), randint(0, HEIGHT)))


       #self.chanel = pygame.mixer.Chanel1
        self.triggers = triggers
        self.sound_played = {trigger: False for trigger in triggers}

        Grass.grasses.append(self)
        object_instances.append(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        for trigger in self.triggers:
            if not self.sound_played[trigger]:
                if (self.rect.collidepoint(trigger.rect.center)):
                    Grass.grass_sound.play()
                    self.sound_played[trigger] = True
            else:
                self.sound_played[trigger] = False
