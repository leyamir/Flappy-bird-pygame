import model
import view
import controller
import pygame

clock = pygame.time.Clock()
while True:
    controller.event_control()
    view.view_model()
    pygame.display.update()
    clock.tick(60)


