
from ui.components.sidemenu.states.extanded_state import ExtendedState
from ui.components.sidemenu.states.icon_state import IconState



class SidemenuButtonModel:
    buttonName = ""
    iconPath = ""

    def __init__(self, buttonName, iconPath):
        self.buttonName = buttonName
        self.iconPath = iconPath
        self.extended_state = ExtendedState(self)
        self.icon_state = IconState(self)
        self.sidemenu_state = self.icon_state

    def set_state(self, state):
        self.sidemenu_state = state
