# Imports
import pygame
import button
import player
import world_slab
import grass
from random import randint, choice

# Initialize Pygame
pygame.init()

# screen variables
WIDTH, HEIGHT = 800, 600
xCENTER = WIDTH // 2
yCENTER = HEIGHT // 2
CENTER = (xCENTER, yCENTER)

# musique
def sound_init():
    pygame.mixer.init()
    pygame.mixer.music.load('sound/Tejano Blue - Cigarettes After Sex.mp3')
    #pygame.mixer.music.play(loops=-1)

    wind_sound1 = pygame.mixer.Sound('sound/wind1.mp3')
    wind_sound2 = pygame.mixer.Sound('sound/wind2.mp3')
    global sounds
    sounds = [wind_sound1, wind_sound2]

# def

def random_sound(random_sound_variable):
    random_sound_variable += 1
    if random_sound_variable > 10:
        random_sound_variable = 0
        for i in sounds:
            if randint(0, 10) == 0:
                i.play()


def redrawScreen(sc, object_instances):
    sc.fill('#111111')
    for obj in object_instances:
        obj.draw(sc)



def main():
    main_menu = False
    object_instances = []
    triggers = []
    random_sound_variable = 0
    sound_init()

    clock = pygame.time.Clock()

    # Screen
    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")

    # world slabs
    colors = ('#999999', '#888888')
    for j in range(4):
        y = j * 400
        for i in range(6):
            x = i * 400
            w_s = world_slab.World_Slab(x, y, object_instances, WIDTH, HEIGHT)

    #player
    p1_ck = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d, pygame.K_LSHIFT]
    p1 = player.Player(xCENTER, yCENTER, object_instances, triggers, p1_ck)

    #p2_ck = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RSHIFT]
    #p2 = player.Player(xCENTER, yCENTER, object_instances, triggers, p2_ck)

    #grass

    for i in range(randint(3, 12)):
        g_instance = grass.Grass(WIDTH, HEIGHT, object_instances, triggers)


    # Buttons
    btn_exit = button.Button(xCENTER, 170, pygame.image.load('image/btn.png'), "EXIT")
    btn_continue = button.Button(xCENTER, 60, pygame.image.load('image/btn.png'), "CONTINUE")

    # main loop
    run = True
    while run:

        clock.tick(60)

        redrawScreen(sc, object_instances)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                main_menu = not main_menu

        if main_menu:
            if btn_exit.draw(sc):
                run = False

            if btn_continue.draw(sc):
                main_menu = False

        p1.control(HEIGHT)
        #p2.control(keys, HEIGHT)

        random_sound(random_sound_variable)

        pygame.display.flip()

    pygame.quit()


main()
