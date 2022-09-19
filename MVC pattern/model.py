import pygame
import random

pygame.init()

game_state = "idle" #game state can be "idle" or "playing" 
die = False
speed = 5

window_width = 500
window_height = 900
screen = pygame.display.set_mode((window_width, window_height))

pipe_width = window_width / 7
pipe_height = pipe_width * 6.5
pipe_hiden_range = 100 
pipe_moving_range = window_width + 2 * pipe_hiden_range
pipe_start = window_width + pipe_hiden_range
pipe_end = 0 - pipe_hiden_range
gap_wide = window_height / 5
top_pipe_image = pygame.image.load("assets/top_pipe.png").convert_alpha()
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
bottom_pipe_image = pygame.image.load("assets/bot_pipe.png").convert_alpha()
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))
pipe_column_pos_x_1 = pipe_start
pipe_column_pos_y_1 = random.randint(-300, 0)
top_pipe_rect_1 = top_pipe_image.get_rect()
bottom_pipe_rect_1 = bottom_pipe_image.get_rect()
top_pipe_rect_1.x = pipe_column_pos_x_1
top_pipe_rect_1.y = pipe_column_pos_y_1 
bottom_pipe_rect_1.x = pipe_column_pos_x_1
bottom_pipe_rect_1.y = pipe_column_pos_y_1 + pipe_height + gap_wide

pipe_column_pos_x_2 = pipe_start + (pipe_start - pipe_end) / 2
pipe_column_pos_y_2 = random.randint(-300, 0)
top_pipe_rect_2 = top_pipe_image.get_rect()
bottom_pipe_rect_2 = bottom_pipe_image.get_rect()
top_pipe_rect_2.x = pipe_column_pos_x_2
top_pipe_rect_2.y = pipe_column_pos_y_2 
bottom_pipe_rect_2.x = pipe_column_pos_x_2
bottom_pipe_rect_2.y = pipe_column_pos_y_2 + pipe_height + gap_wide
random_pipe_1_gap_pos = False
random_pipe_2_gap_pos = False

floor_height = window_height / 10

bird_height = window_height / 15
bird_width = bird_height * 1.2
init_bird_pos_x = window_width / 3
init_bird_pos_y = window_height / 10
bird_pos_x = init_bird_pos_x
bird_pos_y = init_bird_pos_y
bird_image = pygame.image.load("assets/bird.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
bird_rect = bird_image.get_rect()
bird_up = False
bird_speed_down_init = 1
bird_speed_up_init = 12
bird_acc_down = 0.4
bird_acc_up = 1
bird_speed = bird_speed_down_init


game_name_pos_x = window_width / 2
game_name_pos_y = window_height / 2

game_record_pos_x = 3 * (window_height / 8)
game_record_pos_y = window_width / 2

current_point_pos_x = window_height / 8
current_point_pos_y = window_width / 2

background = pygame.image.load("assets/bg.png").convert()
background = pygame.transform.scale(background, (window_width, window_height))

name_image = pygame.image.load("assets/start.png").convert_alpha()
name_image = pygame.transform.scale(name_image, (window_width/1.5, window_height/8))
name_image_rect = name_image.get_rect()
name_image_rect.centerx = game_name_pos_x
name_image_rect.centery = game_name_pos_y

floor_1 = pygame.image.load("assets/floor.png")
floor_1 = pygame.transform.scale(floor_1, (window_width + 1, floor_height))
floor_1_x = 0
floor_1_y = window_height - floor_height
floor_2 = pygame.image.load("assets/floor.png")
floor_2 = pygame.transform.scale(floor_2, (window_width + 1, floor_height))
floor_2_x = window_width
floor_2_y = window_height - floor_height
floor_1_lead = True

