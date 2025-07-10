from .util import validate_str_tuple_dict
from .util import INPUT_TYPE

class ControllerConfig:
    def __init__(self,mappings):
        if validate_str_tuple_dict(mappings):
            self.mappings = mappings
            
    def get_inputs(self):
        "A list of buttons/axis/hats"
        buttons = []
        axis = []
        hats = []
        for x in self.mappings:
            if self.mappings[x][0] == INPUT_TYPE.DIGITAL:
                buttons.append(x)
            elif self.mappings[x][0] == INPUT_TYPE.ANALOG:
                axis.append(x)
            elif self.mappings[x][0] == INPUT_TYPE.HAT:
                hats.append(x)
        return {"buttons":buttons,"axis":axis,"hats":hats}
    
    def get_input_characteristics(self,input:str):
        "Gives the type and value corresponing to the given button"
        return self.mappings[input]
        