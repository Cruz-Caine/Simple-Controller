# Simple Controller

A simple controller wrapper built on pygame for easy game controller input handling in Python.

## Installation

```bash
pip install git+https://github.com/Cruz-Caine/Simple-Controller
```

## Requirements

- Python >= 3.9
- pygame

## Quick Start

```python
from simple_controller import Controller, ControllerSearch

# Find available controllers
search = ControllerSearch()
controllers = search.get_controllers()

if controllers:
    # Initialize first controller with default configuration
    controller = Controller(0)
    
    # Check if a button is pressed
    if controller.get_button_state('A'):
        print("A button pressed!")
    
    # Get analog stick value
    x_axis = controller.get_axis_state('left_stick_x')
    print(f"Left stick X: {x_axis}")
    
    # Get complete controller state
    state = controller.state()
    print(state)
```

## Features

- **Simple API**: Easy-to-use interface for controller input
- **Multiple Input Types**: Support for buttons (digital), axes (analog), and hats (d-pad)
- **Controller Discovery**: Find and enumerate available controllers
- **Configurable Mappings**: Customize button/axis mappings for different controller types
- **Connection Management**: Check connection status and handle disconnections

## API Reference

### Controller Class

#### `Controller(controller_index, config=GENERIC_CONFIG)`

Initialize a controller instance.

- `controller_index`: Index of the controller (0-based)
- `config`: ControllerConfig object defining input mappings

#### Methods

- `query(input_name)`: Get the current state of a specific input
- `state()`: Get the complete state of all configured inputs
- `get_button_state(button_name)`: Get digital button state (True/False)
- `get_axis_state(axis_name)`: Get analog axis value (-1.0 to 1.0)
- `get_hat_state(hat_name)`: Get hat/d-pad state tuple
- `is_connected()`: Check if controller is still connected
- `disconnect()`: Disconnect the controller
- `get_name()`: Get the controller's name

### ControllerConfig Class

Define custom input mappings for different controller types.

```python
from simple_controller import ControllerConfig, INPUT_TYPE

# Custom configuration example
custom_config = ControllerConfig({
    'jump': (INPUT_TYPE.DIGITAL, 0),      # Button 0
    'move_x': (INPUT_TYPE.ANALOG, 0),     # Axis 0
    'dpad': (INPUT_TYPE.HAT, 0)           # Hat 0
})

controller = Controller(0, custom_config)
```

### Input Types

- `INPUT_TYPE.DIGITAL`: Buttons (returns True/False)
- `INPUT_TYPE.ANALOG`: Analog sticks/triggers (returns float -1.0 to 1.0)
- `INPUT_TYPE.HAT`: D-pad/hat switches (returns tuple of x,y values)

## Examples

### Basic Controller Input

```python
from simple_controller import Controller

controller = Controller(0)

while True:
    # Check for button press
    if controller.query('A'):
        print("Action button pressed!")
    
    # Get analog input
    move_x = controller.query('left_stick_x')
    if abs(move_x) > 0.1:  # Dead zone
        print(f"Moving horizontally: {move_x}")
```

### Multiple Controllers

```python
from simple_controller import Controller, ControllerSearch

search = ControllerSearch()
controller_count = len(search.get_controllers())

controllers = []
for i in range(controller_count):
    controllers.append(Controller(i))

# Poll all controllers
for i, controller in enumerate(controllers):
    state = controller.state()
    print(f"Controller {i}: {state}")
```

## License

This project is licensed under the terms specified in the project configuration.

## Author

Cruz Caine (cruz@cruzcaine.com)