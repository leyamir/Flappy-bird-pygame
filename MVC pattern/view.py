import model
import pygame
import controller

pygame.init()
def draw_background():
    model.screen.blit(model.background, (0, 0))

def draw_game_name():
    model.screen.blit(model.name_image, model.name_image_rect)

def draw_floor():
    model.screen.blit(model.floor_1, (model.floor_1_x, model.floor_1_y))
    model.screen.blit(model.floor_2, (model.floor_2_x, model.floor_2_y))
    controller.auto_move_floor()

def draw_pipe():
    controller.set_random_gap_pos()
    model.screen.blit(model.top_pipe_image, model.top_pipe_rect_1)
    model.screen.blit(model.bottom_pipe_image, model.bottom_pipe_rect_1)
    model.screen.blit(model.top_pipe_image, model.top_pipe_rect_2)
    model.screen.blit(model.bottom_pipe_image, model.bottom_pipe_rect_2)
    controller.auto_move_pipe_column()

def draw_bird():
    model.screen.blit(model.bird_image, model.bird_rect)

def view_model():
    if model.game_state == "idle":
        pygame.display.flip()
        draw_background()
        draw_game_name()
        draw_floor()
    elif model.game_state == "active":
        pygame.display.flip()
        draw_background()
        draw_pipe()
        draw_floor()
        draw_bird()


