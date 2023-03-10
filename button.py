import pygame
import constants


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,
                                            (int(width * scale),
                                             int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # pyget mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


def createButtonImage(link):
    return pygame.image.load(link).convert_alpha()


def createButton(button_image, delta):
    return Button(constants.WIDTH / 2 - button_image.get_width() / 2,
                  constants.HEIGHT / 2 - button_image.get_height() / 2 + delta,
                  button_image, 1)
