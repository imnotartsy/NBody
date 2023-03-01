# nbody_examples.py
# Examples of using the nbody module

import nbody as nb
from collections import namedtuple


# Initial Conditions
Body = namedtuple("Body", "m x y z vx vy vz ax ay az")



### Main Program ###
# Initial conditions


# Seconds simulated
tf = 57000

# Resolution of simulation (how many seconds between each simulation)
res = 60               # simulate once every minute

n_bodies_init = {
    "a": Body(100, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    "b": Body(1.0, 2, 2, 0, 0, 0, 0, 0, 0, 0),
    "c": Body(1.0, -2, 2, 0, 0, 0, 0, 0, 0, 0),
    "d": Body(1.0, -2, -2, 0, 0, 0, 0, 0, 0, 0),
    "e": Body(1.0, 2, -2, 0, 0, 0, 0, 0, 0, 0),
}



# * Alternative Initial Conditions for Solar system simulation
# earth_mass = 5.972*10**24
# earth_distance = 1.4774*10**11
# # Manually setting N bodies in the problem
# n_bodies_init = {
#   "Mercury": Body(0.055*earth_mass, 0.387*earth_distance, 0, 0, 0, 0, 0, 0, 0, 0),
#   "Venus":   Body(0.815*earth_mass, 0.723*earth_distance, 0, 0, 0, 0, 0, 0, 0, 0),
#   "Earth":   Body(1*earth_mass,     1*earth_distance,     0, 0, 0, 0, 0, 0, 0, 0),
#   "Mars":    Body(0.107*earth_mass, 1.52*earth_distance,  0, 0, 0, 0, 0, 0, 0, 0),
#   "Jupiter": Body(317.8*earth_mass, 5.20*earth_distance,  0, 0, 0, 0, 0, 0, 0, 0),
#   "Saturn":  Body(95.2*earth_mass,  9.57*earth_distance,  0, 0, 0, 0, 0, 0, 0, 0),
#   "Uranus":  Body(14.5*earth_mass,  19.17*earth_distance, 0, 0, 0, 0, 0, 0, 0, 0),
#   "Neptune": Body(17.1*earth_mass,  30.18*earth_distance, 0, 0, 0, 0, 0, 0, 0, 0),
#   "Pluto":   Body(0.0022*earth_mass,39.48*earth_distance, 0, 0, 0, 0, 0, 0, 0, 0)
# }



# Potential functions
# Graviational Force
G = 6.67e-11
# Inputs:
#   m1, m2 - mass of first body and second body
#   x1, x2 - position of first bost and second body
# Output: the Force on body 1 from body 2
def componentGravF(m1, m2, x1, x2, epsilon):
  if abs(x2 - x1) <= epsilon:
    f = 0
  elif (x2 - x1) > 0:
    f =   G * (m1 * m2)/(x2 - x1)**2
  elif (x2 - x1) < 0:
    f = - G * (m1 * m2)/(x2 - x1)**2

  return f

# Potential functions
# Graviational Potential
G = 6.67e-11
# Inputs:
#   m1, m2 - mass of first body and second body
#   x1, x2 - position of first bost and second body
# Output: the Force on body 1 from body 2
def componentGravP(m1, m2, x1, x2, epsilon):
  if abs(x2 - x1) <= epsilon:
    f = 0
  elif (x2 - x1) > 0:
    f =   (m1 * m2)/(x2 - x1)
  elif (x2 - x1) < 0:
    f = - (m1 * m2)/(x2 - x1)

  return f





### Use of nbody module

# Plot initial conditions/positions (before simulation)
nb.plotBodies(n_bodies_init)

# Iterate through the simulation for tf seconds using the initial conditions + Potential and Force functions
times = nb.iterate(tf, res, n_bodies_init, componentGravP, componentGravF)


# View the output!
nbodies = list(n_bodies_init.keys())

# Cool 3D plot
nb.plot_3d(nbodies, times)

# Plot just the x dimension
nb.plot_x(nbodies, times) 

# Plot the Energies
nb.plot_energy(nbodies, times)