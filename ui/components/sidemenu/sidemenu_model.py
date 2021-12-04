from ui.components.sidemenu.states.extanded_state import ExtendedState
from ui.components.sidemenu.states.icon_state import IconState


class SidemenuModel:

    def __init__(self, controller):
        self.extended_state = ExtendedState(self)
        self.icon_state = IconState(self)
        self.sidemenu_state = self.icon_state
        self.sidemenu_controller = controller

    def set_state(self, state):
            self.sidemenu_state = state