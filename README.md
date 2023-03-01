# README

Hi! This python module `nbody` simulates a set of 'n_bodies' for tf seconds.
Below are the public functions for the module

Get this library with:
```git clone https://github.com/imnotartsy/NBody```

Get Started with:
```python3 nbody_examples.py```

  
## Function Headers


### Printing and Plotting Helper Functions

* `printBodyAttrs(times, n_bodies, i)` 

    Prints the attributes of each body at a given time


* `plotBodies(n_bodies)`

    Returns a 2D plot of the x and y position of each body


* `plot_3d(n_bodies, times)`
    
    Returns a 3D plot of the x and y position of each body over time


* `plot_x(n_bodies, times)`

    Returns a plot of the x position of each body over time


* `plot_energy(n_bodies, times)`

    Returns a plot of the potential and kinetic energy of each body over time



### Discretization Function

`iterate(tf, res, n_bodies_init, p, f, epsilon=.05, debug=False):`
Returns a "times" dictionary with the following structure:

``` Python
times = {
    "times" : [t0, t+res, t+res*2, ... tf],
    "a" : {
        "m" : 1,
        "x" : [x0, x1, x2, ...],  
        "y" : [y0, y1, y2, ...],  
        "z" : [z0, z1, z2, ...],  
        "vx": [vx0, vx1, vx2, ...],
        "vy": [vy0, vy1, vy2, ...],
        "vz": [vz0, vz1, vz2, ...],
        "ax": [ax0, ax1, ax2, ...],
        "ay": [ay0, ay1, ay2, ...],
        "az": [az0, az1, az2, ...],
        "U" : [U0, U1, U2, ...],
        "K" : [K0, K1, K2, ...],
        "fx": [fx0, fx1, fx2, ...],
        "fy": [fy0, fy1, fy2, ...],
        "fz": [fz0, fz1, fz2, ...],
    },
    ...
}
```

