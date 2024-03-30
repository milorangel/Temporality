import pygame
import os
from math import atan2, cos, sin
from random import randint
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, object_instances, triggers, control_keys, speed=2, scale=2, animation_speed=8):
        super().__init__()
        self.speed = speed
        self.control_keys = control_keys
        self.x = x
        self.y = y

        # le son marche pas
        self.running = False
        self.is_sound_playing = False

        pygame.mixer.init()
        self.run_sound = pygame.mixer.Sound('sound/running-in-grass.mp3')


        self.scale = scale
        self.animation_speed = animation_speed
        self.current_direction = 'down'
        self.current_animation_index = 0
        self.animation_control = 0
        self.lasts_direction = [self.current_direction, self.current_direction] #--



        # image loading
        self.image_sets = []
        self.directions = ['down', 'up', 'left', 'right']
        for direction in self.directions:
            image_set = []
            image_folder = f'image/player/{direction}/'
            for filename in os.listdir(image_folder):
                if filename.endswith('.png'):
                    image_path = os.path.join(image_folder, filename)
                    image = pygame.image.load(image_path)
                    image_set.append(image)
            self.image_sets.append(image_set)

        self.width = image.get_width()
        self.height = image.get_height()



        # image scaling
        self.scaled_image_sets = [
            [pygame.transform.scale(img, (int(self.width * scale), int(self.height * scale))) for img in images]
            for images in self.image_sets]

        self.image = self.scaled_image_sets[self.directions.index(self.current_direction)][self.current_animation_index]
        self.rect = self.image.get_rect(topleft=(x, y))


        object_instances.append(self)
        triggers.append(self)

    def draw(self, surface):
        surface.blit(self.image, self.rect.center)

    def run_animation(self, current_direction):
            #self.animation_control = self.animation_speed
        if current_direction == self.lasts_direction[0] or current_direction != self.lasts_direction[1]: #--
            self.animation_control += 1
            if self.animation_control >= self.animation_speed:
                self.animation_control = 0
                self.current_animation_index += 1
                self.current_scaled_image_set = self.scaled_image_sets[self.directions.index(current_direction)]
                if self.current_animation_index >= len(self.current_scaled_image_set):
                    self.current_animation_index = 0
                self.image = self.current_scaled_image_set[self.current_animation_index]
            self.lasts_direction.insert(0, self.current_direction) #--

            # -- pour redemmarer l'animation si on change de direction
            # -- pour ne pas finir le cicle d'une direction qd on la change
            # -- pour ne pas avancer vers le haut tourné vers la droite par exemple
            # -- comment faire pour les diagonales??

            # -- aaah les diagonales

    def control(self, HEIGHT):
        keys = pygame.key.get_pressed()
        self.running = False
        # portail
        if self.y > HEIGHT + self.height:
            self.y = - 0 - self.height
        if self.y < 0 - self.height:
            self.y = HEIGHT + self.height
        # speed up
        if keys[self.control_keys[4]]:
            self.speed = 2
            self.animation_speed = 8
        else:
            self.speed = 1
            self.animation_speed = 10

        kx = 0
        ky = 0


        if keys[self.control_keys[0]]: #[pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_LSHIFT]
            ky =-1
            self.run_animation('up')
        if keys[self.control_keys[1]]:
            ky =1
            self.run_animation('down')
        if keys[self.control_keys[2]]:
            kx =-1
            self.run_animation('left')
        if keys[self.control_keys[3]]:
            kx =1
            self.run_animation('right')


        if ky != 0 or kx != 0:
            self.running = True
            angle = atan2(ky, kx)
            dx = self.speed * cos(angle)
            dy = self.speed * sin(angle)
            self.x += dx
            self.y += dy
            self.rect.center = (self.x, self.y)


        # Inside the method where you check for sound playing:
        if self.running:
            if not self.is_sound_playing:
                self.run_sound.play()
                self.is_sound_playing = True
        else:
            if self.is_sound_playing:
                self.run_sound.stop()
                self.is_sound_playing = False

