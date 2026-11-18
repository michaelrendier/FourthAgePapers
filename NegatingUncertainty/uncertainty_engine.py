"""
uncertainty_engine.py: Negating Uncertainty, the engine.  numpy only; every listing runs cold.
Units hbar = m = omega = 1 unless a function says otherwise.

Machinery (ESTABLISHED, textbook): oscillator eigenstates psi_n, the Fourier pair x <-> p, the quadrature
operator O_theta = cos(theta) x + sin(theta) p, Robertson's relation.
Machinery (the author's reading, THEORETICAL): x and p as two projections of one circular motion in the (x, p) plane.
Nothing here uses a framework constant.
"""
import numpy as np
from math import factorial, pi

# ---------------------------------------------------------------- grid and states
def grid(N=2048, L=14.0):
    x = np.linspace(-L, L, N, endpoint=False); x = x - x[np.argmin(abs(x))]   # exact point at 0
    return x, x[1] - x[0]

def hermite_state(n, x):
    """normalised oscillator eigenfunction psi_n(x) (hbar = m = omega = 1), by the stable recurrence"""
    h0 = pi**-0.25*np.exp(-x**2/2)
    if n == 0: return h0
    h1 = np.sqrt(2)*x*h0
    for k in range(1, n):
        h0, h1 = h1, np.sqrt(2/(k + 1))*x*h1 - np.sqrt(k/(k + 1))*h0
    return h1

def gaussian_state(sigma, x):
    """real Gaussian with position spread sigma (so sigma_p = 1/(2 sigma) when pure)"""
    return (2*pi*sigma**2)**-0.25*np.exp(-x**2/(4*sigma**2))

def norm(psi, dx): return psi/np.sqrt(np.sum(abs(psi)**2)*dx)

# ---------------------------------------------------------------- operators (spectral, so p is exact on the grid)
def apply_p(psi, dx):
    k = 2*pi*np.fft.fftfreq(len(psi), d=dx)
    return np.fft.ifft(k*np.fft.fft(psi))              # p psi = -i d/dx psi, with hbar = 1

def expect(psi, op_psi, dx):                           # <psi| O psi>
    return np.sum(np.conj(psi)*op_psi)*dx

def spreads(psi, x, dx):
    """(sigma_x, sigma_p) of a normalised state"""
    mx = expect(psi, x*psi, dx).real; mp = expect(psi, apply_p(psi, dx), dx).real
    vx = expect(psi, (x - mx)**2*psi, dx).real
    pp = apply_p(psi, dx) - mp*psi
    vp = (np.sum(abs(pp)**2)*dx)
    return np.sqrt(vx), np.sqrt(vp)

def quadrature_spread(psi, x, dx, theta):
    """spread of O_theta = cos(theta) x + sin(theta) p, from the operator applied to the state (no formula used)"""
    Opsi = np.cos(theta)*x*psi + np.sin(theta)*apply_p(psi, dx)
    m = expect(psi, Opsi, dx).real
    return np.sqrt(np.sum(abs(Opsi - m*psi)**2)*dx)

# ---------------------------------------------------------------- the circle (motion > 0) and the point (motion = 0)
def circle_of_energy(E):
    """classical oscillator orbit of energy E (hbar = m = omega = 1): radius, area, and the rms of its two projections"""
    r = np.sqrt(2*E)
    return {"radius": r, "area": pi*r**2, "rms_x": r/np.sqrt(2), "rms_p": r/np.sqrt(2)}

def circle_projection_rms(r, theta, n=200001):
    """rms of the projection of a circle of radius r on the axis at angle theta, by sampling the orbit"""
    t = np.linspace(0, 2*pi, n, endpoint=False)
    return np.sqrt(np.mean((r*np.cos(t)*np.cos(theta) + r*np.sin(t)*np.sin(theta))**2))

# ---------------------------------------------------------------- the Fourier pair as a quarter turn
def fourier_pair(psi, x, dx):
    """phi(p) on the same grid: phi(p) = (2 pi)^-1/2 integral psi(x) e^{-i p x} dx (direct sum, no FFT conventions)"""
    return (dx/np.sqrt(2*pi))*np.exp(-1j*np.outer(x, x)) @ psi

# ---------------------------------------------------------------- helium (the video's estimate)
HBAR, KB, U = 1.054571817e-34, 1.380649e-23, 1.66053906660e-27
def helium_estimates(n_per_A3=0.02183):
    m = 4.002602*U
    hb2_2m = HBAR**2/(2*m)/KB*1e20            # K Angstrom^2
    r = (3/(4*pi*n_per_A3))**(1/3)            # radius of the volume per atom, Angstrom
    return {"hbar2_over_2m_K_A2": hb2_2m, "r_A": r,
            "video_E_K": hb2_2m/r**2,                         # E = p^2/2m, p = hbar/r
            "gauss3d_sigma_r_over_2_K": 3*hb2_2m/(4*(r/2)**2)} # 3 axes, hbar^2/(8 m sigma^2) each, sigma = r/2

if __name__ == "__main__":
    x, dx = grid()
    print("P1/P2 eigenstates: sigma_x sigma_p vs (n+1/2), and the circle of energy (n+1/2)")
    for n in range(9):
        psi = norm(hermite_state(n, x), dx); sx, sp = spreads(psi, x, dx); c = circle_of_energy(n + 0.5)
        print("  n=%d  quantum %.9f  (n+1/2) %.1f  circle rms product %.9f  area/h %.9f" % (n, sx*sp, n + .5, c['rms_x']*c['rms_p'], c['area']/(2*pi)))
    print("P3 quadrature spread over theta for n = 0,1,4: max relative spread")
    for n in (0, 1, 4):
        psi = norm(hermite_state(n, x), dx); s = np.array([quadrature_spread(psi, x, dx, th) for th in np.linspace(0, pi, 37)])
        print("  n=%d  %.2e" % (n, (s.max() - s.min())/s.mean()))
    print("P4 squeezed Gaussian sigma_x = 0.5: spread vs ellipse formula and conjugate product")
    psi = norm(gaussian_state(0.5, x), dx); sx, sp = spreads(psi, x, dx)
    for th in (0, pi/8, pi/4, 3*pi/8, pi/2):
        a = quadrature_spread(psi, x, dx, th); b = quadrature_spread(psi, x, dx, th + pi/2)
        f = np.sqrt(sx**2*np.cos(th)**2 + sp**2*np.sin(th)**2)
        print("  theta=%.3f  spread %.6f  ellipse %.6f  conjugate product %.6f" % (th, a, f, a*b))
    print("P5 kinetic energy of a Gaussian vs hbar^2/(8 m sigma^2)")
    for s in (1.0, 0.5, 0.25, 0.1):
        psi = norm(gaussian_state(s, x), dx); E = 0.5*np.sum(abs(apply_p(psi, dx))**2)*dx
        print("  sigma=%.2f  KE %.6f  formula %.6f" % (s, E, 1/(8*s**2)))
    print("P7 Fourier transform of psi_n versus (-i)^n psi_n")
    for n in range(6):
        psi = norm(hermite_state(n, x), dx); phi = fourier_pair(psi, x, dx)
        print("  n=%d  max error %.2e" % (n, abs(phi - (-1j)**n*psi).max()))
    print("P6 liquid helium-4:", {k: round(v, 3) for k, v in helium_estimates().items()})
