
from ui.components.toolbar.states.extanded_state import ExtendedState
from ui.components.toolbar.states.icon_state import IconState



class SidemenuButtonModel:
    buttonName = ""
    pathLinkedMainWindowView = ""

    def __init__(self):
        self.extended_state = ExtendedState(self)
        self.icon_state = IconState(self)
        self.sidemenu_state = self.icon_state



    def set_state(self, state):
        self.sidemenu_state = state


class SidemenuButton1(SidemenuButtonModel):
    def __init__(self):
        super().__init__()
        self.buttonName = "test1"
        self.pathLinkedMainWindowView = ""

class SidemenuButton2(SidemenuButtonModel):
    def __init__(self):
        super().__init__()
        self.buttonName = "test2"
        self.pathLinkedMainWindowView = ""

class SidemenuButton3(SidemenuButtonModel):
    def __init__(self):
        super().__init__()
        self.buttonName = "test3"
        self.pathLinkedMainWindowView = ""

class SidemenuButton4(SidemenuButtonModel):
    def __init__(self):
        super().__init__()
        self.buttonName = "test4"
        self.pathLinkedMainWindowView = ""

class SidemenuButton5(SidemenuButtonModel):
    def __init__(self):
        super().__init__()
        self.buttonName = "test5"
        self.pathLinkedMainWindowView = ""
