from modelling.nematic_model import Nematic_Model
import numpy as np


class Quartic_Model(Nematic_Model):
    def __init__(self, size=10, T=2, J2=1, bias=0, S=0.5, J4=1):
        super().__init__(size, T, J2, bias, S)

        self.J4 = J4

        print(
            f"Created a {self.L} x {self.L} Quartic model, "
            + f"at J = {self.J}, "
            + f"with initial magnetisation of {self.mag_lib[0]:.4f}"
        )

    def energy_func(self):
        pass

    def proposal():
        # wrap around [-pi/4, pi/4)
        pass

    def metropolis_hasting(self):
        super().metropolis_hasting()
