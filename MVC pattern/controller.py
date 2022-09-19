from pygame.time import delay
import model
import pygame
import sys 
import random

def auto_move_floor():
    model.floor_1_x -= model.speed
    model.floor_2_x -= model.speed
    if model.floor_2_x <= 0 and model.floor_1_lead == True:
        model.floor_1_x = model.window_width
        model.floor_1_lead = False
    if model.floor_1_x <= 0 and not(model.floor_1_lead): 
        model.floor_2_x = model.window_width
        model.floor_1_lead =  True


def move_bird():
    if not(model.bird_up):
        model.bird_rect.centery += model.bird_speed
        model.bird_speed += model.bird_acc_down
    else:
        model.bird_rect.centery -= model.bird_speed
        model.bird_speed -= model.bird_acc_up
        if model.bird_speed <= 0:
            model.bird_speed = model.bird_speed_down_init
            model.bird_up = False

def auto_move_pipe_column():
    model.pipe_column_pos_x_1 -= model.speed
    model.top_pipe_rect_1.x = model.pipe_column_pos_x_1
    model.bottom_pipe_rect_1.x = model.pipe_column_pos_x_1
    model.pipe_column_pos_x_2 -= model.speed
    model.top_pipe_rect_2.x = model.pipe_column_pos_x_2
    model.bottom_pipe_rect_2.x = model.pipe_column_pos_x_2
    if model.pipe_column_pos_x_1 <= model.pipe_end:
        model.pipe_column_pos_x_1 = model.pipe_start
        model.random_pipe_1_gap_pos = True
        model.top_pipe_rect_1.x = model.pipe_column_pos_x_1
        model.bottom_pipe_rect_1.x = model.pipe_column_pos_x_1
    if model.pipe_column_pos_x_2 <= model.pipe_end:
        model.pipe_column_pos_x_2 = model.pipe_start
        model.random_pipe_2_gap_pos = True
        model.top_pipe_rect_2.x = model.pipe_column_pos_x_2
        model.bottom_pipe_rect_2.x = model.pipe_column_pos_x_2

def set_random_gap_pos():
    if model.random_pipe_1_gap_pos == True:
        model.pipe_column_pos_y_1 = random.randint(-300, 0)
        model.top_pipe_rect_1.y = model.pipe_column_pos_y_1
        model.bottom_pipe_rect_1.y = model.pipe_column_pos_y_1 + model.pipe_height + model.gap_wide
        model.random_pipe_1_gap_pos = False
    elif model.random_pipe_2_gap_pos == True:
        model.pipe_column_pos_y_2 = random.randint(-300, 0)
        model.top_pipe_rect_2.y = model.pipe_column_pos_y_2
        model.bottom_pipe_rect_2.y = model.pipe_column_pos_y_2 + model.pipe_height + model.gap_wide
        model.random_pipe_2_gap_pos = False

def check_loose():
    if model.die == False:
        if model.bird_rect.centery <= 0 or model.bird_rect.centery >= model.window_height - model.floor_height:
            model.game_state = "idle"
            rest_data()
        elif model.bird_rect.colliderect(model.top_pipe_rect_1) or model.bird_rect.colliderect(model.top_pipe_rect_2) or model.bird_rect.colliderect(model.bottom_pipe_rect_1) or model.bird_rect.colliderect(model.bottom_pipe_rect_2):
            model.game_state = "idle"
            rest_data()
def rest_data():
    model.die = False
    model.bird_up = False
    model.bird_speed_down_init = 1
    model.bird_speed_up_init = 12
    model.bird_acc_down = 0.4
    model.bird_acc_up = 1
    model.bird_speed = model.bird_speed_down_init
    model.pipe_column_pos_x_1 = model.pipe_start
    model.pipe_column_pos_y_1 = random.randint(-300, 0)
    model.top_pipe_rect_1.x = model.pipe_column_pos_x_1
    model.top_pipe_rect_1.y = model.pipe_column_pos_y_1 
    model.bottom_pipe_rect_1.x = model.pipe_column_pos_x_1
    model.bottom_pipe_rect_1.y = model.pipe_column_pos_y_1 + model.pipe_height + model.gap_wide
    model.top_pipe_rect_2.x = model.pipe_column_pos_x_2
    model.top_pipe_rect_2.y = model.pipe_column_pos_y_2 
    model.bottom_pipe_rect_2.x = model.pipe_column_pos_x_2
    model.bottom_pipe_rect_2.y = model.pipe_column_pos_y_2 + model.pipe_height + model.gap_wide
    model.random_pipe_1_gap_pos = False
    model.random_pipe_2_gap_pos = False
    model.pipe_column_pos_x_2 = model.pipe_start + (model.pipe_start - model.pipe_end) / 2
    model.pipe_column_pos_y_2 = random.randint(-300, 0)
    model.init_bird_pos_x = model.window_width / 3
    model.init_bird_pos_y = model.window_height / 10
    model.bird_pos_x = model.init_bird_pos_x
    model.bird_pos_y = model.init_bird_pos_y

def event_control():
    check_loose()
    if model.game_state == "active":
        move_bird()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE and model.game_state == "idle":
                model.game_state = "active"
                model.bird_rect.centerx = model.init_bird_pos_x
                model.bird_rect.centery = model.init_bird_pos_y
            elif event.key == pygame.K_SPACE and model.game_state == "active":
                model.bird_up = True
                model.bird_speed = model.bird_speed_up_init
    pygame.event.clear()


