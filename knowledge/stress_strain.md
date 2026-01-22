# Elastic Stress and Strain

## Calculations

### Stress in 1-D Extension (Linearised)
X, Y are material coordinates
x, y = spatial coordinates

$$
A = L/L_0
where A > 1
$$

$$
x¬ = x_(X_)
x = AX,             y = Y_
u_x = x - X,        u_y = y - Y
u_x = AX - X
u_x = X(A - 1),     u_y = 0

E_XX = (A - 1) + 0.5 * ((A - 1)**2)
E_YY = E_ZZ = 0
E_XY = E_YZ = E_XZ = 0

epsilon_xx ~= du_x/X = A - 1
A - 1 << 1
$$

### Strain in Simple Shear
$$
x¬ = x_(X_)
x = X + (kappa * Y) = X * tan(theta),           y = Y
u_x = x - X,                                    u_y = y - Y
u_x = x + (kappa * Y) = X * (tan(theta) - 1),   u_y = 0

E_XX = E_ZZ = 0
E_YY = 0.5 * (kappa**2)
E_XY = 0.5 * kappa
E_YZ = E_XZ = 0

epsilon_xx ~= du_x/dX = epsilon_yy = epsilon_zz = 0
$$

### Strain for Rigid-Body Rotation
$$
x = X * cos(phi) + Y * sin(phi)
y = -X * sin(phi) + Y * cos(phi)

u_x = X * (cos(phi) - 1) + Y * sin(phi)
u_y = -X * sin(phi) + Y * (cos(phi) - 1)

epsilon_xx = cos(phi) - 1
epsilon_yy = cos(phi) - 1
epsilon_xy = 0.5 * (sin(phi) - sin(phi)) = 0
epsilon_yz = epsilon_xz = 0
$$

## Arterial Wall Stress in Hypertenstion
sum(F_y) = 0 at equilibrium
sum(F_y) = -2 * sigma_theta,theta(h * L) + P(2 * a * L)
sigma_theta,theta(h * L) is the domain that the pressure is acting upon and has a tension

sigma_theta,theta = (P * a) / h
if P increases then h has to increase the same amount as P
