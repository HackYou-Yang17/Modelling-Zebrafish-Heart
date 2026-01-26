from modelling.xy_model import Xy_Model
import numpy as np


class Nematic_Model(Xy_Model):
    def __init__(self, size=10, T=2, J=1, bias=0, S=0.5, N=2):
        super().__init__(size, T, J, bias, S)
        self.N = N

        print(
            f"Created a {self.L} x {self.L} Nematic model, "
            + f"at J = {self.J}, "
            + f"with initial magnetisation of {self.mag_lib[0]:.4f}"
        )

    def energy_func(self):
        energy = 0  # Initialisation
        energy = (
            -self.J
            * 0.5
            * np.sum(
                np.cos(
                    self.N * (self.angles - np.roll(self.angles, 1, axis=0))
                )  # Vertical
                + np.cos(
                    self.N * (self.angles - np.roll(self.angles, 1, axis=1))
                )  # Horizontal
            )
        )  # 1: rolls left and up, -1: rolls right and down
        return energy

    def proposal(self, angle):
        # wrap around [-pi/2, pi/2)
        return (angle + np.random.normal(self.bias, self.sigma)) % (
            2 * np.pi
        )  # Mapping

    def hastings_ratio(self, angle, proposed):
        pass

    def local_dE(self, angle, proposed, neighbours):
        dE = 0
        for neighbour in neighbours:
            dE += -self.J * (
                np.cos(self.N * (proposed - neighbour))
                - np.cos(self.N * (angle - neighbour))
            )
        return dE

    def magnetisation(self):
        sum_cos = np.sum(np.cos(self.N * (self.angles))) / self.L**2
        sum_sin = np.sum(np.sin(self.N * (self.angles))) / self.L**2
        return np.sqrt(sum_cos**2 + sum_sin**2)

    def metropolis_hasting(self):
        super().metropolis_hasting()


class Quartic_Model(Nematic_Model):
    def __init__(self, size=10, T=2, J=1, bias=0, S=0.5, N=4):
        super().__init__(size, T, J, bias, S)

        print(
            f"Created a {self.L} x {self.L} Quartic model, "
            + f"at J = {self.J}, "
            + f"with initial magnetisation of {self.mag_lib[0]:.4f}"
        )
