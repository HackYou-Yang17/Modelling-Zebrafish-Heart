from datetime import datetime
from pathlib import Path
import numpy as np


class Ising_Model:
    def __init__(self, size=10, T=2.0, J=1.0, bias=0.5):
        self.L = size
        self.T = T  # Temperature
        self.J = J  # Coupling strength
        self.bias = bias

        self.spins = np.random.choice([-1, 1], size=(self.L, self.L))  # Initial state
        self.energy = self.energy_func()
        self.mag = np.sum(self.spins)

        # For visualization
        self.data_lib = [self.spins]
        self.energy_lib = [self.energy]
        self.mag_lib = [self.mag / (self.L**2)]

        print(
            f"Created a {self.L} x {self.L} Ising model, "
            + f"at J = {self.J}, "
            + f"with initial mag of {self.mag_lib[0]:.4f}"
        )

    def energy_func(self):
        # Based on Hamiltonian
        energy = 0  # Initialisation
        energy = (
            -self.J
            * 0.5
            * np.sum(
                self.spins
                * (np.roll(self.spins, 1, axis=0) + np.roll(self.spins, 1, axis=1))
            )
        )  # 1: rolls left and up, -1: rolls right and down
        return energy

    def proposal(self, neighbours):
        if np.random.random() < self.bias:
            proposed = 1 if neighbours > 0 else -1  # Do align
        else:
            proposed = -1 if neighbours > 0 else 1  # Don't align
        return proposed

    def hastings_ratio(self, spin, proposed, neighbours):
        # Calculates proposal probabilities Q(current→proposed) and Q(proposed→current)
        # Calculates the Hastings ratio
        if neighbours > 0:
            q_forward = self.bias if proposed == 1 else (1 - self.bias)
            q_reverse = self.bias if spin == 1 else (1 - self.bias)
        else:  # neighbours ≤ 0
            q_forward = self.bias if proposed == -1 else (1 - self.bias)
            q_reverse = self.bias if spin == -1 else (1 - self.bias)
        return q_reverse / q_forward

    def metropolis_hasting(self):
        i, j = np.random.randint(0, self.L, size=2)
        spin = self.spins[i, j]

        # Gets closest neighbours
        neighbours = (
            self.spins[(i - 1) % self.L, j]
            + self.spins[(i + 1) % self.L, j]
            + self.spins[i, (j - 1) % self.L]
            + self.spins[i, (j + 1) % self.L]
        )

        # Provides asymmetric proposal
        proposed = self.proposal(neighbours)

        # Hastings acceptance
        if proposed != spin:
            dE = -self.J * (proposed - spin) * neighbours  # Energy function
            alpha = np.exp(-dE / self.T) * (
                self.hastings_ratio(spin, proposed, neighbours)
            )
            # Accepts the proposed spin if the change in global energy is lower
            # or by chance of alpha (alpha-percent chance)
            if dE < 0 or np.random.random() < alpha:
                self.spins[i, j] = proposed
                self.energy += dE
                self.mag += proposed - spin

    def run(self, steps, save_every=10):
        for step in range(steps):
            self.metropolis_hasting()

            if step % save_every == 0:
                self.data_lib.append(self.spins.copy())
                self.energy_lib.append(self.energy)
                self.mag_lib.append(self.mag / (self.L**2))

    def save_data(self, params, filename="ising_data"):
        full_file = filename + f"_{datetime.now().isoformat()}"
        mapping = {"-": "_", ".": "_", ":": "_"}
        full_file = "".join(mapping.get(c, c) for c in full_file)

        file_path = Path(__file__).parent.parent.joinpath("data", filename, full_file)
        np.savez(
            file_path,
            data_history=np.array(self.data_lib),
            energy_history=np.array(self.energy_lib),
            mag_history=np.array(self.mag_lib),
            params=params,
        )
        print(f"Saved {len(self.data_lib)} frames to {full_file}\n")


"""
Monte Carlo improvements:

`Measurements`:         Compute observables (specific heat, susceptibility, correlation functions) during simulation, not just energy/magnetization.
`Thermalization`:       Discard initial steps (burn-in) before collecting data to reach equilibrium.
`Correlation time`:     Sample less frequently than autocorrelation time to get independent measurements.
`Error estimation`:     Use block averaging or bootstrap to estimate statistical errors.
`Parallelization`:      Run multiple independent chains for better statistics or use vectorized updates.
`Adaptive schemes`:     Adjust proposal bias during simulation to optimize acceptance rate (~50%).
`Better sampling`:      Implement cluster algorithms (Wolff/Swendsen-Wang) for critical slowing down near T_c.
`Replica exchange`:     Run multiple temperatures simultaneously with swapping for better phase space exploration.
"""
