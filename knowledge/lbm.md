# Lattice Boltzmann Method (LBM)

## What is the Lattice Boltzmann Method?
The Lattice Boltzmann Method (LBM) is a computational fluid dynamics (CFD) technique for simulating fluid flow. It is an efficient means of simulating passive fluids such as active nematic and polar systems. The most common is the D2Q9 model (2-dimensions, 9-quasi-velocities) lattice.

### Macroscopic vs. Mesoscopic
`CFD (Navier-Stokes Solvers):`  These solve the Navier-Stokes equations, 
                                which are macroscopic, continuum-based equations. They deal with bulk properties like velocity (u), pressure (p), and density (ρ). They are derived from the conservation of mass, momentum, and energy.

`Lattice Boltzmann Method:`     LBM does not directly solve the Navier-Stokes 
                                equations. Instead, it operates at a mesoscopic scale. It models a fluid as a collection of fictitious particles that reside on a discrete lattice and propagate and collide according to simple rules.

At each node of this grid, a set of ditribution functions is stored - denoted as `f_i(x, t)`. This is stored instead of pressure and velocity. f_i(x, t) represents the probability of finding a particle at location `x` and time `t` moving with a discrete velocity `e_i`.

The simulation proceeds in two fundamental steps at each time step:

`Streaming:`    Particles move (stream) from one lattice node to a neighboring node 
                along their direction e_i.

`Collision:`    When particles arrive at a node, they interact (collide), 
                redistributing their momenta. This step is where the physics of fluid behavior is encoded.

The macroscopic quantities (density, velocity) are then recovered as moments (i.e., weighted sums) of these distribution functions.

`Density`
$$
\rho(x, t) = \displaystyle\sum_{i} f_i(x, t)
$$
`Velocity`
$$
u = \frac{\displaystyle\sum_{i} e_if_i(x, t)}{\displaystyle\sum_{i} f_i(x, t)}
$$
`Density & Velocity (Mass Flow Rate)`
$$
\rho u(x, t) = \displaystyle\sum_{i} e_if_i(x, t)
$$


## Theoretical Foundations
`Boltzmann Equation:`   Describes the statistical behavior of a thermodynamic system 
                        not in equilibrium. It governs the evolution of the particle distribution function, `f(x, v, t)`, which gives the density of particles with velocity `v` at position `x` and time `t`.

$$
\frac{\partial f}{\partial t} + v \cdot \nabla f = \Omega(f)
$$

`Bhatnagar, Gross, and Krook (BGK):`    Assumed that all collisions drive the 
                                        distribution function towards a local equilibrium state `f_eq` at a single rate `τ` (the relaxation time).

$$
\Omega(f) = -\frac{1}{\tau}(f - f_{eq})
$$

`Boltzmann-BGK Equation:`

$$
\frac{\partial f}{\partial t} + v \cdot \nabla f = -\frac{1}{\tau}(f - f_{eq})
$$

### Discretization: Continuous To Lattice
`Velocity Space:`
`Equilibrium Distribution:`
`Space & Time:`