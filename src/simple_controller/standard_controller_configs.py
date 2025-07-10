from .controller_config import ControllerConfig
from .util import INPUT_TYPE

# PlayStation 4 Controller (pygame 2.x)
PLAYSTATION4_CONFIG = ControllerConfig({
    # Face buttons
    "Cross": (INPUT_TYPE.DIGITAL, 0),
    "Circle": (INPUT_TYPE.DIGITAL, 1),
    "Square": (INPUT_TYPE.DIGITAL, 2),
    "Triangle": (INPUT_TYPE.DIGITAL, 3),
    
    # Shoulder buttons
    "L1": (INPUT_TYPE.DIGITAL, 9),
    "R1": (INPUT_TYPE.DIGITAL, 10),
    "L2": (INPUT_TYPE.ANALOG, 4),
    "R2": (INPUT_TYPE.ANALOG, 5),
    
    # D-pad (as buttons)
    "DPad_Up": (INPUT_TYPE.DIGITAL, 11),
    "DPad_Down": (INPUT_TYPE.DIGITAL, 12),
    "DPad_Left": (INPUT_TYPE.DIGITAL, 13),
    "DPad_Right": (INPUT_TYPE.DIGITAL, 14),
    
    # Menu buttons
    "Share": (INPUT_TYPE.DIGITAL, 4),
    "Options": (INPUT_TYPE.DIGITAL, 6),
    "PS": (INPUT_TYPE.DIGITAL, 5),
    "Touchpad": (INPUT_TYPE.DIGITAL, 15),
    
    # Stick buttons
    "L3": (INPUT_TYPE.DIGITAL, 7),
    "R3": (INPUT_TYPE.DIGITAL, 8),
    
    # Analog sticks
    "Left_Stick_X": (INPUT_TYPE.ANALOG, 0),
    "Left_Stick_Y": (INPUT_TYPE.ANALOG, 1),
    "Right_Stick_X": (INPUT_TYPE.ANALOG, 2),
    "Right_Stick_Y": (INPUT_TYPE.ANALOG, 3)
})

# PlayStation 5 Controller (pygame 2.x)
PLAYSTATION5_CONFIG = ControllerConfig({
    # Face buttons
    "Cross": (INPUT_TYPE.DIGITAL, 0),
    "Circle": (INPUT_TYPE.DIGITAL, 1),
    "Square": (INPUT_TYPE.DIGITAL, 2),
    "Triangle": (INPUT_TYPE.DIGITAL, 3),
    
    # Shoulder buttons
    "L1": (INPUT_TYPE.DIGITAL, 4),
    "R1": (INPUT_TYPE.DIGITAL, 5),
    "L2": (INPUT_TYPE.DIGITAL, 6),
    "R2": (INPUT_TYPE.DIGITAL, 7),
    
    # D-pad (as HAT only)
    "DPad": (INPUT_TYPE.HAT, 0),
    
    # Menu buttons
    "Share": (INPUT_TYPE.DIGITAL, 8),
    "Options": (INPUT_TYPE.DIGITAL, 9),
    "PS": (INPUT_TYPE.DIGITAL, 10),
    
    # Stick buttons
    "L3": (INPUT_TYPE.DIGITAL, 11),
    "R3": (INPUT_TYPE.DIGITAL, 12),
    
    # Analog sticks
    "Left_Stick_X": (INPUT_TYPE.ANALOG, 0),
    "Left_Stick_Y": (INPUT_TYPE.ANALOG, 1),
    "Right_Stick_X": (INPUT_TYPE.ANALOG, 3),
    "Right_Stick_Y": (INPUT_TYPE.ANALOG, 4),
    
    # Triggers as analog
    "L2_Analog": (INPUT_TYPE.ANALOG, 2),
    "R2_Analog": (INPUT_TYPE.ANALOG, 5)
})

# Xbox 360 Controller (pygame 2.x)
XBOX360_CONFIG = ControllerConfig({
    # Face buttons
    "A": (INPUT_TYPE.DIGITAL, 0),
    "B": (INPUT_TYPE.DIGITAL, 1),
    "X": (INPUT_TYPE.DIGITAL, 2),
    "Y": (INPUT_TYPE.DIGITAL, 3),
    
    # Shoulder buttons
    "LB": (INPUT_TYPE.DIGITAL, 4),
    "RB": (INPUT_TYPE.DIGITAL, 5),
    "LT": (INPUT_TYPE.ANALOG, 2),
    "RT": (INPUT_TYPE.ANALOG, 5),
    
    # D-pad (as HAT)
    "DPad": (INPUT_TYPE.HAT, 0),
    
    # Menu buttons
    "Back": (INPUT_TYPE.DIGITAL, 6),
    "Start": (INPUT_TYPE.DIGITAL, 7),
    "Guide": (INPUT_TYPE.DIGITAL, 10),
    
    # Stick buttons
    "LS": (INPUT_TYPE.DIGITAL, 8),
    "RS": (INPUT_TYPE.DIGITAL, 9),
    
    # Analog sticks
    "Left_Stick_X": (INPUT_TYPE.ANALOG, 0),
    "Left_Stick_Y": (INPUT_TYPE.ANALOG, 1),
    "Right_Stick_X": (INPUT_TYPE.ANALOG, 3),
    "Right_Stick_Y": (INPUT_TYPE.ANALOG, 4)
})

# Nintendo Switch Pro Controller (pygame 2.x)
NINTENDO_SWITCH_PRO_CONFIG = ControllerConfig({
    # Face buttons
    "A": (INPUT_TYPE.DIGITAL, 0),
    "B": (INPUT_TYPE.DIGITAL, 1),
    "X": (INPUT_TYPE.DIGITAL, 2),
    "Y": (INPUT_TYPE.DIGITAL, 3),
    
    # Shoulder buttons
    "L": (INPUT_TYPE.DIGITAL, 9),
    "R": (INPUT_TYPE.DIGITAL, 10),
    "ZL": (INPUT_TYPE.ANALOG, 4),
    "ZR": (INPUT_TYPE.ANALOG, 5),
    
    # D-pad
    "DPad_Up": (INPUT_TYPE.DIGITAL, 11),
    "DPad_Down": (INPUT_TYPE.DIGITAL, 12),
    "DPad_Left": (INPUT_TYPE.DIGITAL, 13),
    "DPad_Right": (INPUT_TYPE.DIGITAL, 14),
    
    # Menu buttons
    "Minus": (INPUT_TYPE.DIGITAL, 4),
    "Plus": (INPUT_TYPE.DIGITAL, 6),
    "Home": (INPUT_TYPE.DIGITAL, 5),
    "Capture": (INPUT_TYPE.DIGITAL, 15),
    
    # Stick buttons
    "L_Stick": (INPUT_TYPE.DIGITAL, 7),
    "R_Stick": (INPUT_TYPE.DIGITAL, 8),
    
    # Analog sticks
    "Left_Stick_X": (INPUT_TYPE.ANALOG, 0),
    "Left_Stick_Y": (INPUT_TYPE.ANALOG, 1),
    "Right_Stick_X": (INPUT_TYPE.ANALOG, 2),
    "Right_Stick_Y": (INPUT_TYPE.ANALOG, 3)
})


# Generic controller config with common button names
GENERIC_CONFIG = ControllerConfig({
    # Face buttons (most common across all controllers)
    "Button_0": (INPUT_TYPE.DIGITAL, 0),
    "Button_1": (INPUT_TYPE.DIGITAL, 1),
    "Button_2": (INPUT_TYPE.DIGITAL, 2),
    "Button_3": (INPUT_TYPE.DIGITAL, 3),
    
    # Shoulder buttons
    "Button_4": (INPUT_TYPE.DIGITAL, 4),
    "Button_5": (INPUT_TYPE.DIGITAL, 5),
    "Button_6": (INPUT_TYPE.DIGITAL, 6),
    "Button_7": (INPUT_TYPE.DIGITAL, 7),
    
    # Stick clicks and additional buttons
    "Button_8": (INPUT_TYPE.DIGITAL, 8),
    "Button_9": (INPUT_TYPE.DIGITAL, 9),
    "Button_10": (INPUT_TYPE.DIGITAL, 10),
    "Button_11": (INPUT_TYPE.DIGITAL, 11),
    "Button_12": (INPUT_TYPE.DIGITAL, 12),
    "Button_13": (INPUT_TYPE.DIGITAL, 13),
    "Button_14": (INPUT_TYPE.DIGITAL, 14),
    "Button_15": (INPUT_TYPE.DIGITAL, 15),
    
    # Standard analog inputs (sticks and triggers)
    "Axis_0": (INPUT_TYPE.ANALOG, 0),  # Usually left stick X
    "Axis_1": (INPUT_TYPE.ANALOG, 1),  # Usually left stick Y
    "Axis_2": (INPUT_TYPE.ANALOG, 2),  # Usually right stick X or left trigger
    "Axis_3": (INPUT_TYPE.ANALOG, 3),  # Usually right stick Y or right trigger
    "Axis_4": (INPUT_TYPE.ANALOG, 4),  # Usually right stick Y or left trigger
    "Axis_5": (INPUT_TYPE.ANALOG, 5),  # Usually right trigger
    
    # Additional axes for complex controllers
    "Axis_6": (INPUT_TYPE.ANALOG, 6),
    "Axis_7": (INPUT_TYPE.ANALOG, 7),
    
    # Hat/D-pad inputs (standard for most controllers)
    "Hat_0": (INPUT_TYPE.HAT, 0)
})
