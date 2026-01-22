from modelling.xy_model import Xy_Model
import numpy as np


class Nematic_Model(Xy_Model):
    def __init__(self, size=10, T=2, J2=1, bias=0, S=0.5):
        super().__init__(size, T, J2, bias, S)

        print(
            f"Created a {self.L} x {self.L} Nematic model, "
            + f"at J = {self.J}, "
            + f"with initial magnetisation of {self.mag_lib[0]:.4f}"
        )

    def proposal(self, angle):
        # wrap around [-pi/2, pi/2)
        pass

    def metropolis_hasting(self):
        super().metropolis_hasting()
