from modelling.ising_model import Ising_Model
import numpy as np


class Xy_Model(Ising_Model):
    def __init__(self, size=10, T=2.0, J=1.0, bias=0.0, S=0.5):
        self.L = size
        self.T = T  # Temperature
        self.J = J  # Coupling strength
        self.bias = bias
        self.sigma = S  # Gaussian width

        self.angles = np.random.uniform(0, 2*np.pi, size=(self.L, self.L)) # Initial state
        self.energy = self.energy_func()
        self.mag = self.magnetisation()

        # For visualization
        self.data_lib = [self.angles]
        self.energy_lib = [self.energy]
        self.mag_lib = [self.mag]

        print(f"Created a {self.L} x {self.L} X-Y model, " +
              f"at J = {self.J}, " +
              f"with initial magnetisation of {self.mag_lib[0]:.4f}")

    def energy_func(self):
        energy = 0 # Initialisation
        energy = -self.J * 0.5 * np.sum(
            np.cos(self.angles - np.roll(self.angles, 1, axis=0)) + # Vertical
            np.cos(self.angles - np.roll(self.angles, 1, axis=1)) # Horizontal
        ) # 1: rolls left and up, -1: rolls right and down
        return energy

    def proposal(self, angle):
        # Asymmetric proposal
        return (angle + np.random.normal(self.bias, self.sigma)) % (2*np.pi) # Mapping

    def hastings_ratio(self, angle, proposed):
        diff = (proposed - angle + np.pi) % (2*np.pi) - np.pi # Wrap to [-π, π)
        q_forward = np.exp(-0.5 * ((diff - self.bias)**2) / self.sigma**2)
        diff = (angle - proposed + np.pi) % (2*np.pi) - np.pi
        q_reverse = np.exp(-0.5 * ((diff - self.bias)**2) / self.sigma**2)
        return q_reverse / q_forward
    
    def local_dE(self, angle, proposed, neighbours):
        dE = 0
        for neighbour in neighbours:
            dE += -self.J * (np.cos(proposed - neighbour) - 
                             np.cos(angle - neighbour))
        return dE
    
    def magnetisation(self):
        sum_cos = np.sum(np.cos(self.angles)) / self.L**2
        sum_sin = np.sum(np.sin(self.angles)) / self.L**2
        return np.sqrt(sum_cos**2 + sum_sin**2)

    def metropolis_hasting(self):
        i, j = np.random.randint(0, self.L, size=2)
        angle = self.angles[i, j]

        neighbours = [
            self.angles[(i-1) % self.L, j],
            self.angles[(i+1) % self.L, j],
            self.angles[i, (j-1) % self.L],
            self.angles[i, (j+1) % self.L],
                    ]

        proposed = self.proposal(angle)
        hastings_ratio = self.hastings_ratio(angle, proposed)
        dE = self.local_dE(angle, proposed, neighbours)
        alpha = np.exp(-dE / self.T) * hastings_ratio

        if dE < 0 or np.random.random() < alpha:
            self.angles[i, j] = proposed
            self.energy += dE
            self.mag = self.magnetisation()

    def run(self, steps, save_every=10):
        for step in range(steps):
            self.metropolis_hasting()

            if step % save_every == 0:
                self.data_lib.append(self.angles.copy())
                self.energy_lib.append(self.energy)
                self.mag_lib.append(self.mag)