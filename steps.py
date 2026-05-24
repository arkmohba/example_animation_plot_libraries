
def flux_ftcs(q, c, dt, dx, j):
    return (c*q[j+1] - c*q[j]) / 2


def flux_upwind(q, c, dt, dx, j):
    return (c + abs(c))*q[j]/2 + (c-abs(c))*q[j+1]/2


def flux_lax(q, c, dt, dx, j):
    nu = c * dt / dx
    return ((1-1/nu) * c * q[j+1] + (1+1/nu) * c * q[j]) / 2


def flux_lax_wendroff(q, c, dt, dx, j):
    nu = c * dt / dx
    return ((1-nu) * c * q[j+1] + (1+nu) * c * q[j]) / 2


def step_with_flux(q, c, dt, dx, ff):
    qold = q.copy()
    for j in range(1, len(q) - 1):
        ff1 = ff(qold, c, dt, dx, j)
        ff2 = ff(qold, c, dt, dx, j-1)
        q[j] = qold[j] - dt / dx * (ff1 - ff2)
    return q
