import pygame
from enum import Enum

class INPUT_TYPE(Enum):
        DIGITAL = 1
        ANALOG = 2
        HAT = 3

def ensure_pygame_initialized():
    if not pygame.get_init():
        pygame.init()
        pygame.joystick.init()

def validate_str_tuple_dict(config):
    """Ensure dictionary has string keys and (INPUT_TYPE, int) tuple values"""
    if not isinstance(config, dict):
        raise TypeError("Config must be a dictionary")
    
    for key, value in config.items():
        # Check key is string
        if not isinstance(key, str):
            raise TypeError(f"Key '{key}' must be a string, got {type(key).__name__}")
        
        # Check value is tuple
        if not isinstance(value, tuple):
            raise TypeError(f"Value for '{key}' must be a tuple, got {type(value).__name__}")
        
        # Check tuple has exactly 2 elements
        if len(value) != 2:
            raise ValueError(f"Tuple for '{key}' must have exactly 2 elements, got {len(value)}")
        
        # Check first element is INPUT_TYPE enum
        if not isinstance(value[0], INPUT_TYPE):
            raise TypeError(f"First element of tuple for '{key}' must be INPUT_TYPE enum, got {type(value[0]).__name__}")
        
        # Check second element is int
        if not isinstance(value[1], int):
            raise TypeError(f"Second element of tuple for '{key}' must be an integer, got {type(value[1]).__name__}")
    
    return True