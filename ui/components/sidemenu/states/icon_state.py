from ui.components.sidemenu.states.i_sidemenu_state import ISidemenuState


class IconState(ISidemenuState):

    def __init__(self, model):
        super().__init__(model)

    def move_to_next_visibility_state(self):
        self.sidemenu_model.sidemenu_controller.extend_sidemenu()
        self.sidemenu_model.set_state(self.sidemenu_model.extended_state)
