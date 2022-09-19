import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# Variable 
game_speed = 5 #  5 6 8 10 12 15 
fps = 60
bird_speed = 3
bird_pos = 300
floor_speed = game_speed
floor_first_pos = 0

first_pipe_pos = 750
second_pipe_pos = 1200
pipe_speed = game_speed

hole_wide = 200
point = 0


screen = pygame.display.set_mode((600, 1000))
background = pygame.image.load("assets/bg.png").convert()
background = pygame.transform.scale(background, (800, 1000))

bird = pygame.image.load("assets/bird.png").convert_alpha()
bird = pygame.transform.scale(bird, (70, 54))
bird_rect = bird.get_rect()
bird_rect.height -= 20

floor = pygame.image.load("assets/floor.png")
floor = pygame.transform.scale(floor, (800, 100))

bottom_pipe = pygame.image.load("assets/bot_pipe.png").convert_alpha()
bottom_pipe = pygame.transform.scale(bottom_pipe, (80, 800))
bottom_pipe_rect = bottom_pipe.get_rect()
bottom_pipe_rect.width -= 20
top_pipe = pygame.image.load("assets/top_pipe.png").convert_alpha()
top_pipe = pygame.transform.scale(top_pipe, (80, 800))
top_pipe_rect = top_pipe.get_rect()
top_pipe_rect.width -= 20
top_pipe_rect.height -= 20

bottom_pipe_copy = pygame.image.load("assets/bot_pipe.png").convert_alpha()
bottom_pipe_copy = pygame.transform.scale(bottom_pipe_copy, (80, 800))
bottom_pipe_rect_copy = bottom_pipe_copy.get_rect()
bottom_pipe_rect_copy.width -= 20
top_pipe_copy = pygame.image.load("assets/top_pipe.png").convert_alpha()
top_pipe_copy = pygame.transform.scale(top_pipe_copy, (80, 800))
top_pipe_rect_copy = top_pipe_copy.get_rect()
top_pipe_rect_copy.width -= 20
top_pipe_rect_copy.height -= 20

start_message = pygame.image.load("assets/start.png").convert_alpha()
start_message = pygame.transform.scale(start_message, (420, 120))

font = pygame.font.Font('assets/Flappy-Bird.ttf', 100)
text = font.render(str(point), True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (300, 200)

record_text = font.render("rec", True, (255, 255, 255))
record_text_rect = record_text.get_rect()
record_text_rect.center = (200, 300)

flap_sound = pygame.mixer.Sound("assets/flap.wav")
hit_sound = pygame.mixer.Sound("assets/hit.wav")
start_sound = pygame.mixer.Sound("assets/start.wav")
point_sound = pygame.mixer.Sound("assets/point.wav")

def build_floor():
    global floor_first_pos, floor_speed
    screen.blit(floor, (floor_first_pos, 900))
    screen.blit(floor, (floor_first_pos + 750, 900))
    floor_first_pos -= floor_speed
    if floor_first_pos <= -800:
        floor_first_pos = 0
    
def build_pipe(pos, top_pipe_location):
    bottom_pipe_location = top_pipe_location + 800 + hole_wide
    top_pipe_rect.center = (pos, top_pipe_location)
    bottom_pipe_rect.center = (pos, bottom_pipe_location)
    #pygame.draw.rect(screen, (255, 0, 0), bottom_pipe_rect, 4)
    #pygame.draw.rect(screen, (255, 0, 0), top_pipe_rect, 4)
    screen.blit(bottom_pipe, bottom_pipe_rect)
    screen.blit(top_pipe, top_pipe_rect)

def build_pipe_copy(pos, top_pipe_location):
    bottom_pipe_location = top_pipe_location + 800 + hole_wide
    top_pipe_rect_copy.center = (pos, top_pipe_location)
    bottom_pipe_rect_copy.center = (pos, bottom_pipe_location)
    #pygame.draw.rect(screen, (255, 0, 0), bottom_pipe_rect_copy, 4)
    #pygame.draw.rect(screen, (255, 0, 0), top_pipe_rect_copy, 4)
    screen.blit(bottom_pipe_copy, bottom_pipe_rect_copy)
    screen.blit(top_pipe_copy, top_pipe_rect_copy)


def check_loose():
    if bird_rect.centery >= 900 or bird_rect.centery <= 0 or bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect_copy) or bird_rect.colliderect(top_pipe_rect_copy):
        return False
    return True


is_up = False
game_active = False
point_data = open("highscore.txt", "r")
highscore = point_data.readline() 
highscore = int(highscore)
point_data.close()
while not(game_active):
    screen.blit(background, (0, 0))
    screen.blit(start_message, (80, 400))
    text_rect.centerx = 180
    text = font.render("Record " + str(highscore), True, (255, 255, 255))
    screen.blit(text, text_rect)

    build_floor()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                start_sound.play()
                game_active = True
    pygame.display.update() 
    clock.tick(fps)

x = random.randint(-150, 10)
x_copy = random.randint(-200, 50)
is_loose = False
text_rect.centerx = 300
while True:
    if point == 5:
        game_speed = 6
    elif point == 15:
        game_speed = 8
    elif point == 25:
        game_speed = 10
    elif point == 35:
        game_speed = 12
    elif point == 45:
        game_speed = 15

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE and game_active:
                flap_sound.play()
                is_up = True
                bird_speed = 10
            if event.key == pygame.K_SPACE and not(game_active):
                start_sound.play()
                game_active = True
                bird_speed = 3
                bird_pos = 300
                is_up = False
                is_loose = False
                point = 0
                text_rect.centerx = 300
                game_speed = 5
                
    
    if game_active == True:
        if is_up == True:
            first_pipe_pos -= pipe_speed
            second_pipe_pos -= pipe_speed
            bird_speed -= 0.4
            bird_pos -= bird_speed
            bird_rect.centery -= bird_speed
            screen.blit(background, (0, 0))
            bird_rect.center = (200, bird_pos)
            #pygame.draw.rect(screen, (255, 0, 0), bird_rect, 4)
            screen.blit(bird, bird_rect)
            
            build_pipe(first_pipe_pos, x)
            build_pipe_copy(second_pipe_pos, x_copy)
            build_floor()
            text = font.render(str(point), True, (255, 255, 255))
            screen.blit(text, text_rect)
        else:
            first_pipe_pos -= pipe_speed
            second_pipe_pos -= pipe_speed
            bird_speed += 0.4
            bird_pos += bird_speed
            bird_rect.centery += bird_speed

            screen.blit(background, (0, 0))
            bird_rect.center = (200, bird_pos)
            #pygame.draw.rect(screen, (255, 0, 0), bird_rect, 4)
            screen.blit(bird, bird_rect)

            build_pipe(first_pipe_pos, x)
            build_pipe_copy(second_pipe_pos, x_copy)
            build_floor()

        if bird_speed == 3:
            is_up = False
        if first_pipe_pos <= -150:
            x = random.randint(-350, 150)
            first_pipe_pos = 750
        if second_pipe_pos <= -150:
            x_copy = random.randint(-350, 150)
            second_pipe_pos = 750
        if first_pipe_pos == 150  or second_pipe_pos == 150:
            point_sound.play()
            point += 1
    else:
        first_pipe_pos = 750
        second_pipe_pos = 1200
        x = random.randint(-150, 10)
        x_copy = random.randint(-200, 50)
        screen.blit(background, (0, 0))
        build_floor()
        screen.blit(start_message, (80, 400))
        text_rect.centerx = 190
        text = font.render("Score " + str(point), True, (255, 255, 255))
        screen.blit(text, text_rect)
        point_data = open("highscore.txt", "r")
        highscore = point_data.readline() 
        highscore = int(highscore)
        record_text = font.render("Record " + str(highscore), True, (255, 255, 255))
        screen.blit(record_text, record_text_rect)

    game_active = check_loose()
    if is_loose == False and game_active == False:
        hit_sound.play()
        pygame.event.clear()
        pygame.time.delay(1000)
        pygame.event.clear()
        point_data = open("highscore.txt", "r")
        highscore = point_data.readline() 
        highscore = int(highscore)
        if point > highscore:
            point_data = open("highscore.txt", "w")
            point_data.write(str(point))
            point_data.close()
        is_loose = True
    pygame.display.update() 

    clock.tick(fps)
