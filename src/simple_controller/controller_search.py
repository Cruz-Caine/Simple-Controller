from .util import ensure_pygame_initialized
import pygame

class ControllerSearch:

    def __init__(self):
        ensure_pygame_initialized()
        self.joysticks=[]
    
    def search(self):
        "Research for controllers"
        pygame.joystick.quit()
        pygame.joystick.init()

    def count(self):
        "Checks the amount of controllers detected"
        return pygame.joystick.get_count()

    def __get_index_name(self, index : int):
        "Returns the name corresponding to an index"
        if (index < 0 or index > self.count()):
            raise IndexError("Index out of range")
        joystick = pygame.joystick.Joystick(index)
        name = joystick.get_name()
        joystick.quit()
        return name

    def comp(self):
        "Returns the names of connected controllers"
        controllers = {}
        for x in range(self.count()):
            controllers[x] = self.__get_index_name(x)
        return controllers