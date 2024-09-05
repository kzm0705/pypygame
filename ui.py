import pygame



class Userinterface():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None,60)

    def my_score(self,screen):
        current_score = self.font.render(str(self.score),True,(255,255,255))
        screen.blit(current_score, (10,10))
        






