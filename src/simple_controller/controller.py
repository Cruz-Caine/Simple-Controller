from .util import ensure_pygame_initialized, INPUT_TYPE
from .controller_config import ControllerConfig
from .standard_controller_configs import GENERIC_CONFIG
import pygame

class Controller:
    def __init__(self, controller_index: int, config : ControllerConfig = GENERIC_CONFIG):
        ensure_pygame_initialized()
        
        if controller_index < 0 or controller_index >= pygame.joystick.get_count():
            raise IndexError("Controller index out of range")
        
        self.joystick = pygame.joystick.Joystick(controller_index)
        self.joystick.init()
        self.config = config
        
    def query(self, input_name: str):
        pygame.event.pump()
        
        if input_name not in self.config.mappings:
            raise KeyError(f"Input '{input_name}' not found in configuration")
        
        input_type, input_index = self.config.mappings[input_name]
        
        if input_type == INPUT_TYPE.DIGITAL:
            return self.joystick.get_button(input_index)
        elif input_type == INPUT_TYPE.ANALOG:
            return self.joystick.get_axis(input_index)
        elif input_type == INPUT_TYPE.HAT:
            return self.joystick.get_hat(input_index)
        else:
            raise ValueError(f"Unknown input type: {input_type}")
    
    def state(self):
        pygame.event.pump()
        
        inputs = {}
        for input_name in self.config.mappings:
            input_type, input_index = self.config.mappings[input_name]
            
            if input_type == INPUT_TYPE.DIGITAL:
                inputs[input_name] = self.joystick.get_button(input_index)
            elif input_type == INPUT_TYPE.ANALOG:
                inputs[input_name] = self.joystick.get_axis(input_index)
            elif input_type == INPUT_TYPE.HAT:
                inputs[input_name] = self.joystick.get_hat(input_index)
                
        return inputs
    
    def get_button_state(self, button_name: str):
        pygame.event.pump()
        
        if button_name not in self.config.mappings:
            raise KeyError(f"Button '{button_name}' not found in configuration")
        
        input_type, input_index = self.config.mappings[button_name]
        
        if input_type != INPUT_TYPE.DIGITAL:
            raise ValueError(f"'{button_name}' is not a digital input")
        
        return self.joystick.get_button(input_index)
    
    def get_axis_state(self, axis_name: str):
        pygame.event.pump()
        
        if axis_name not in self.config.mappings:
            raise KeyError(f"Axis '{axis_name}' not found in configuration")
        
        input_type, input_index = self.config.mappings[axis_name]
        
        if input_type != INPUT_TYPE.ANALOG:
            raise ValueError(f"'{axis_name}' is not an analog input")
        
        return self.joystick.get_axis(input_index)
    
    def get_hat_state(self, hat_name: str):
        pygame.event.pump()
        
        if hat_name not in self.config.mappings:
            raise KeyError(f"Hat '{hat_name}' not found in configuration")
        
        input_type, input_index = self.config.mappings[hat_name]
        
        if input_type != INPUT_TYPE.HAT:
            raise ValueError(f"'{hat_name}' is not a hat input")
        
        return self.joystick.get_hat(input_index)
    
    def is_connected(self):
        return self.joystick.get_init()
    
    def disconnect(self):
        if self.joystick.get_init():
            self.joystick.quit()
    
    def get_name(self):
        return self.joystick.get_name()