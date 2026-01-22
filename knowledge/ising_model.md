# Ising Model
## What Is The Ising model?
The Ising model is a mathematical abstraction of ferromagnetism in statistical mechanics. Conceived by Wilhelm Lenz and solved in one dimension by his student Ernst Ising in 1925, it represents one of the simplest models that exhibits phase transitions and collective behavior emerging from local interactions.

At its core, the Ising model captures the profound truth that complex macroscopic phenomena can emerge from simple microscopic rules


## What Does The Model Describe?
### Microscopic Degrees of Freedom
The model consists of discrete variables called "spins" (σᵢ) arranged on a lattice. Each spin can be in one of two states: +1 (↑) or -1 (↓). These represent magnetic dipole moments aligned "up" or "down."

### Hamiltonian (Energy Function) of Ising Model
The total energy of the system is given by:

$$
H = -J \displaystyle\sum_{<ij>} \sigma_i \sigma_j - h\displaystyle\sum_{i} \sigma_i
$$

where:
J = Coupling constant (J > 0 for ferromagnetic interaction)
⟨ij⟩ = Sum over nearest-neighbor pairs
h = External magnetic field
σᵢ = Spin at position i

This Hamiltonian embodies two fundamental principles:
`Alignment tendency:` Neighboring spins "want" to align (energy minimized when σᵢσⱼ = +1)
`Response to external field:` Spins "want" to align with external field h

