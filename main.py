# FIXME: Fancy Header Here Later

import pygame
from player import Player
from enemy import Enemy
from rockets import Rocket
import background
from pygame.locals import *
import random
from random import randint
import obstacles
import background

def game():
    global start_time
    # Initialize main menu appearance
    background1 = pygame.image.load("graphics/BG.png")
    background1 = pygame.transform.scale(background1, (1280, 1280)) # 1280, 1280
    plane_fly1, plane_fly2 = plane_menu_images()
    plane_rect = plane_fly1.get_rect(topright=(1500, 100)) # 1500, 100 start for moving
    screen.blit(background1, (0, 0))
    play_img, how_img, lboard_img = button_images()
    # Main Menu loop
    running = True
    frame_flag = True
    opacity = 0
    #INITIAL GAMESTATE
    gamestate = 0
    enemyStopwatch = 0
    #obstacle vars
    air_time = 0
    cloud_time = 0
    ground_time = 0

    air_speed = 180
    ground_speed = 420

    frame_counter = 0
    checker = True
    #player (weird bug that forces me to put this here)
    player = Player()
    player_group = pygame.sprite.GroupSingle()
    player_group.add(player)

    while running:
        if gamestate == 0:
            for event in pygame.event.get():
            # If user hits the x button on pygame window
                if event.type == QUIT:
                    running = False
                # If any of the buttons are clicked
                if pygame.time.get_ticks() > 3000: #ensures everything is loaded properly before startup
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if play_rect.collidepoint(pos):
                            gamestate = 1 # <-------- PUT GAMEPLAY FUNCTION HERE
                            start_time = pygame.time.get_ticks()
                        if how_rect.collidepoint(pos):
                            pass # <------ PUT HOW TO PLAY MENU HERE
                        if lboard_rect.collidepoint(pos):
                            pass # <----- PUT LEADERBOARD MENU HERE
                        if credits_rect.collidepoint(pos):
                            print('credits') # <----- PUT CREDIT MENU HERE
            # Plane animation
            screen.blit(background1, (0, 0))
            plane_rect, frame_flag = plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag)

            # Buttons / GUI Functionality
            play_rect = buttons(play_img, opacity, (width/2, height/2))
            how_rect = buttons(how_img, opacity, (320, 550))
            lboard_rect = buttons(lboard_img, opacity, (920, 550))
            font = pygame.font.SysFont(None, 36)
            credits = font.render("CREDITS", True, (255, 255, 255))
            credits_rect = credits.get_rect(center=(width/2, 650))
            screen.blit(credits, credits_rect)
            pygame.display.update()
            opacity += 3
        elif gamestate == 1:
            time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (time - player.stopwatch) > 480:
                            rocket_group.add(player.create_rocket())
                            player.stopwatch = pygame.time.get_ticks()
                            player.animationState = 2
                            shoot.play()
                            shoot.set_volume(0.2)
            if (time - enemyStopwatch) > 2000:
                enemies.add(Enemy(1400,randint(100,620)))
                enemyStopwatch = pygame.time.get_ticks()
            screen.blit(sky_surf_scaled, (0,0))

            ground_time += 1
            air_time += 1
            cloud_time += 1
            frame_counter += 1
            
            if (frame_counter > 300) and (checker == True):
                air_speed -= 2
                ground_speed -= 5
                frame_counter = 0
                if (air_speed < 120) or (ground_speed < 180):
                    checker = False

            if (air_time > air_speed):
                obj2 = random.randint(0,1)
                x = random.randint(400, 1280)
                slope = random.randint(1,10)
                air_group.add(obstacles.AirObstacles(air_obstacles[obj2], x, slope))
                air_time = 0
            
            if (cloud_time > 180):
                backgrounds.add(background.Background(clouds[random.randint(0,2)]))
                cloud_time = 0

            if (ground_time > ground_speed):
                ground_group.add(obstacles.GroundObstacles(ground_obstacles[random.randint(0,2)]))
                ground_time = 0

            backgrounds.draw(screen)
            backgrounds.update()

            air_group.draw(screen)
            air_group.update()

            ground_group.draw(screen)
            ground_group.update()

            score()
                    
            player_group.draw(screen)
            player_group.update()
            enemies.draw(screen)
            enemies.update()
            rocket_group.draw(screen)
            rocket_group.update()
            for enemy in enemies:
                if enemy.rect.y < player.rect.y:
                    enemy.rect.y += 2
                if enemy.rect.y > player.rect.y:
                    enemy.rect.y -= 2
                if pygame.sprite.spritecollideany(enemy,rocket_group):
                    enemy.getHit = True
            for rocket in rocket_group:
                if pygame.sprite.spritecollideany(rocket,enemies):
                    rocket.getHit = True
                if pygame.sprite.spritecollideany(rocket,ground_group):
                    rocket.getHit = True
                if pygame.sprite.spritecollideany(rocket,air_group):
                    rocket.getHit = True
                if rocket.animationState == 0:
                    enemyDie.play()
                    enemyDie.set_volume(0.2)
            for player in player_group:
                if pygame.sprite.spritecollideany(player,enemies):
                    player.image = pygame.transform.scale(player.dead, (116,80))
                if pygame.sprite.spritecollideany(player,air_group):
                    player.image = pygame.transform.scale(player.dead, (116,80))
                if pygame.sprite.spritecollideany(player,ground_group):
                    player.image = pygame.transform.scale(player.dead, (116,80))
                    #gamestate = 2
            pygame.sprite.groupcollide(rocket_group,air_group,False,True)
            pygame.display.update()
            clock.tick(60)
        elif gamestate == 2:
            #GAMEOVER SCREEN
            pass


def plane_menu_images():
    ''' Loads plane images and returns them after manipulation '''

    # Loading, scaling and flipping first plane image
    plane_fly1 = pygame.image.load("graphics/plane/Fly (1).png")
    plane_fly1 = pygame.transform.scale(plane_fly1, (222, 151))
    plane_fly1 = pygame.transform.flip(plane_fly1, True, False)
    # Loading, scaling and flipping second plane image
    plane_fly2 = pygame.image.load("graphics/plane/Fly (2).png")
    plane_fly2 = pygame.transform.scale(plane_fly2, (222, 151))
    plane_fly2 = pygame.transform.flip(plane_fly2, True, False)
    # Returns two pygame images
    return plane_fly1, plane_fly2


def plane_animation(plane_rect, plane_fly1, plane_fly2, frame_flag):
    ''' Creates animation for plane's propellor.
    Also some functionality for menu movement.
    NOTE: be sure to call screen.blit(background, (0, 0)) before this function '''

    # Get center position from the previous frame's rectangle
    current_center = plane_rect.center
    # Speed is only necessary for flying plane image across screen, not animation
    speed = [-5,0]	# <--- not needed for propellor animation
    # Alternate images every frame
    if frame_flag:
        # Create a new rect with alternate plane image
        # *** At same location as previous frame using "center ="
        plane_rect = plane_fly2.get_rect(center = current_center)
        plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
        screen.blit(plane_fly2, plane_rect)
    else:
        plane_rect = plane_fly1.get_rect(center = current_center)
        plane_rect = plane_rect.move(speed) # <--- not needed for propellor animation
        screen.blit(plane_fly1, plane_rect)
    frame_flag = not frame_flag
    return plane_rect, frame_flag

def score():
        current_time = pygame.time.get_ticks() - start_time
        time = 'Score: ' + str(int(current_time/1000))
        score_surf = font.render(time, False, (64, 64, 64))
        score_rect = score_surf.get_rect(topleft = (0,0))
        screen.blit(score_surf, score_rect) 

def button_images():
    play_img = pygame.image.load("graphics/play.png")
    play_img = pygame.transform.scale(play_img, (322, 151))
    how_img = pygame.image.load("graphics/howtoplay.png")
    how_img = pygame.transform.scale(how_img, (300, 200))
    lboard_img = pygame.image.load("graphics/leaderboard.png")
    lboard_img = pygame.transform.scale(lboard_img, (505, 135))
    return play_img, how_img, lboard_img #cloud6


def buttons(img, opacity, position):
    ''' Adding buttons/fading in to the screen '''
    img.set_alpha(opacity)
    rect = img.get_rect(center=position)
    screen.blit(img, rect)
    return rect

if __name__ == "__main__":
    # CONSTANT values like colours here
    SKYBLUE = (135, 206, 235)

    # Create vars for screen size and width/height of screen
    size = 1280, 720
    width, height = size
    #Initialization
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    clouds = ["cloud1", "cloud5", "cloud9"] 
    ground_obstacles = ["ground obj 1", "ground obj 2", "ground obj 3"]
    air_obstacles = ["asteroid", "anvil"]

    backgrounds = pygame.sprite.Group()
    ground_group = pygame.sprite.Group()
    air_group = pygame.sprite.Group()

    sky_surf = pygame.image.load("graphics/backgrounds/uncolored_hills.png").convert()
    sky_surf_scaled = pygame.transform.scale(sky_surf, (1280,720))

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 50)
    start_time = 0
    # -------------------------------------------------------------------------------------------

    #sounds
    pygame.mixer.music.load('sfx/calm.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    shoot = pygame.mixer.Sound('sfx/playershoot.wav')
    enemyDie = pygame.mixer.Sound('sfx/enemy_die.wav')
    crash = pygame.mixer.Sound('sfx/crash.mp3')
    #rocket 
    rocket_group = pygame.sprite.Group()
    #enemies
    enemies = pygame.sprite.Group()
    # Main game loop
    game()

    pygame.quit()
