import sys
sys.path.append('../')

import unittest
from scipy.integrate import solve_ivp
import numpy as np

import lorenz
import case

def ode_lorenz_attractor_t(t, X):

    x = X[0]
    y = X[1]
    z = X[2]

    delta = 10
    beta = 8 / 3
    rho = 6

    dxdt = delta * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z

    return [dxdt, dydt, dzdt]


class TestMethod(unittest.TestCase):

    def test_solver(self):
        c0 = [4, 4, 5]
        dt = 0.01
        N = 50001
        T = N * dt

        sol = solve_ivp(ode_lorenz_attractor_t, y0=c0, t_span=[0, T], t_eval=np.arange(0, T, dt))
        x1 = sol.y[0]
        y1 = sol.y[1]
        z1 = sol.y[2]

        f = case.case1.ode_lorenz_attractor
        u, t = lorenz.solver.ode_solver(f, c0)

        x2 = u[:, 0]
        y2 = u[:, 1]
        z2 = u[:, 2]

        assert np.allclose(x1, x2, rtol=1e1, atol=1e1)
        assert np.allclose(y1, y2, rtol=1e1, atol=1e1)
        assert np.allclose(z1, z2, rtol=1e1, atol=1e1)
