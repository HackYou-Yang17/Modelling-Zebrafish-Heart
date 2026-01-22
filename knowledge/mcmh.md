# Monte Carlo Metropolis Hasting Algorithm

## What Is The Boltzmann Distribution?
`Example Systems:`
- A collection of atoms in a material
- Spins in a magnet
- Particles in a gas

These systems have many possible configurations (e.g., positions of all atoms, orientations of all spins). Each configuration has a certain energy, and the probability of finding the system in that configuration is given by Boltzmann's distribution:

$$
P(configuration) \propto e^\frac{-E}{k_B T}
$$

## What Is The Problem?
`Problem:`  For a system with N particles, there are astronomically many possible 
            configurations. Calculating average properties (like magnetization, pressure, etc.) requires summing over all configurations weighted by their probability. This is impossible to do exactly.

`Solution:` Instead of summing over all configurations, we generate a  
            representative sample of configurations where each configuration appears with its correct Boltzmann probability. Then we compute averages using this sample.

`Monte Carlo:`  It's a method using random numbers to sample configurations. And   
                Metropolis-Hastings tells us how to do this sampling correctly.