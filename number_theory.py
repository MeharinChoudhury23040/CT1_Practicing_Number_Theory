""" Meharin Choudhury. IT-23040. """
""" CT#1 - Practicing Number Theory: all experiments in one module. """
import math
from math import gcd, log, isqrt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("figures", exist_ok=True)


# ---------- 1. Primes: sieve and trial division ----------
def sieve(n):
    """Sieve of Eratosthenes: all primes <= n."""
    is_p = [True] * (n + 1)
    is_p[0:2] = [False, False]
    for i in range(2, isqrt(n) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i, v in enumerate(is_p) if v]


def is_prime_trial(n):
    """Trial division up to sqrt(n), skipping multiples of 2 and 3 (wheel of 6)."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ---------- 2. Infinitude of primes ----------
def euclid_step(primes):
    """Smallest prime divisor of (product + 1): never in the list."""
    N = math.prod(primes) + 1
    d = 2
    while N % d:
        d += 1
    return N, d


# ---------- 3. Fermat test, pseudoprimes, Carmichael ----------
def fermat_test(n, a):
    return pow(a, n - 1, n) == 1


def fermat_pseudoprimes(base, limit):
    return [n for n in range(3, limit)
            if not is_prime_trial(n) and gcd(n, base) == 1 and fermat_test(n, base)]


def is_carmichael(n):
    if n < 3 or is_prime_trial(n):
        return False
    return all(pow(a, n - 1, n) == 1 for a in range(2, n) if gcd(a, n) == 1)


def korselt(n):
    """Korselt: squarefree, composite and (p-1) | (n-1) for each prime p | n."""
    if n < 3 or is_prime_trial(n):
        return False
    m, p, ps = n, 2, []
    while p * p <= m:
        if m % p == 0:
            ps.append(p)
            m //= p
            if m % p == 0:
                return False
        else:
            p += 1
    if m > 1:
        ps.append(m)
    return len(ps) > 1 and all((n - 1) % (q - 1) == 0 for q in ps)


# ---------- 4. Euler totient, primitive roots, Lucas test ----------
def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def order(a, n):
    k, x = 1, a % n
    while x != 1:
        x = x * a % n
        k += 1
    return k


def primitive_roots(p):
    return [a for a in range(1, p) if order(a, p) == p - 1]


def prime_factors(n):
    f, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            f.add(d)
            n //= d
        d += 1
    if n > 1:
        f.add(n)
    return f


def lucas_n_minus_1(n):
    """Lucas theorem: find a with a^(n-1)=1 and a^((n-1)/q)!=1 for all prime q | n-1."""
    for a in range(2, n):
        if pow(a, n - 1, n) != 1:
            continue
        if all(pow(a, (n - 1) // q, n) != 1 for q in prime_factors(n - 1)):
            return a
    return None


# ---------- 5. Lucas-Lehmer, Mersenne, perfect numbers ----------
def lucas_lehmer(p):
    if p == 2:
        return True
    s, M = 4, 2 ** p - 1
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0


def sigma_proper(n):
    return sum(d for d in range(1, n) if n % d == 0)


# ---------- 6. Antiprimes ----------
def num_divisors(n):
    return sum(1 for d in range(1, n + 1) if n % d == 0)


def antiprimes(limit):
    best, out = 0, []
    for n in range(1, limit + 1):
        d = num_divisors(n)
        if d > best:
            best = d
            out.append(n)
    return out


# ---------- 7. Cryptography: extended Euclid + toy RSA ----------
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def modinv(a, m):
    g, x, _ = egcd(a, m)
    assert g == 1, "no inverse"
    return x % m


def rsa_demo(p=61, q=53, e=17, msg=65):
    n, ph = p * q, (p - 1) * (q - 1)
    d = modinv(e, ph)
    c = pow(msg, e, n)
    return n, ph, d, c, pow(c, d, n)


# ---------- figures ----------
def fig_pi_x():
    N = 10 ** 5
    ps = sieve(N)
    xs = np.arange(2, N + 1)
    pi = np.searchsorted(ps, xs, side="right")
    plt.figure(figsize=(7, 4))
    plt.plot(xs, pi, label=r"$\pi(x)$")
    plt.plot(xs, xs / np.log(xs), "--", label=r"$x/\ln x$")
    plt.xlabel("x"); plt.ylabel("count"); plt.legend(); plt.grid(alpha=.3)
    plt.title("Prime Number Theorem")
    plt.tight_layout(); plt.savefig("figures/pi_x.png", dpi=150); plt.close()
    plt.figure(figsize=(7, 4))
    plt.plot(xs, pi / (xs / np.log(xs)))
    plt.axhline(1, color="r", ls="--")
    plt.xlabel("x"); plt.ylabel(r"$\pi(x)/(x/\ln x)$"); plt.grid(alpha=.3)
    plt.title("Ratio slowly tends to 1")
    plt.tight_layout(); plt.savefig("figures/pnt_ratio.png", dpi=150); plt.close()


def fig_ulam(n=201):
    grid = np.zeros((n, n))
    x = y = n // 2
    dx, dy, steps, k = 1, 0, 1, 1
    pset = set(sieve(n * n))
    while k <= n * n:
        for _ in range(2):
            for _ in range(steps):
                if 0 <= x < n and 0 <= y < n and k in pset:
                    grid[y, x] = 1
                x += dx; y += dy; k += 1
            dx, dy = -dy, dx
        steps += 1
    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="gray_r"); plt.axis("off")
    plt.title("Ulam spiral (primes in black)")
    plt.tight_layout(); plt.savefig("figures/ulam.png", dpi=150); plt.close()


def fig_gaps():
    ps = sieve(10 ** 5)
    gaps = np.diff(ps)
    plt.figure(figsize=(7, 4))
    plt.hist(gaps, bins=range(1, 60, 2), edgecolor="k")
    plt.xlabel("gap between consecutive primes"); plt.ylabel("frequency")
    plt.title("Prime gaps below 100,000")
    plt.tight_layout(); plt.savefig("figures/gaps.png", dpi=150); plt.close()


def fig_mod4_race():
    ps = sieve(10 ** 5)[1:]
    r1 = np.cumsum([p % 4 == 1 for p in ps])
    r3 = np.cumsum([p % 4 == 3 for p in ps])
    plt.figure(figsize=(7, 4))
    plt.plot(ps, r3 - r1)
    plt.axhline(0, color="r", ls="--")
    plt.xlabel("x"); plt.ylabel(r"$\pi(x;4,3)-\pi(x;4,1)$"); plt.grid(alpha=.3)
    plt.title("Chebyshev's bias: 4k+3 primes usually lead")
    plt.tight_layout(); plt.savefig("figures/chebyshev_bias.png", dpi=150); plt.close()


if __name__ == "__main__":
    print("primes<=50:", sieve(50))
    print("n^2+n+41 first composite n:",
          next(n for n in range(100) if not is_prime_trial(n * n + n + 41)))
    primes, steps = [2], []
    for _ in range(5):
        N, d = euclid_step(primes)
        steps.append((list(primes), N, d))
        if d not in primes:
            primes.append(d)
    for s in steps:
        print("Euclid:", s)
    print("(2*3*5*7*11*13)+1 =", 30031, "=", "59*509")
    print("Goldbach check 4..10000:",
          all(any(is_prime_trial(p) and is_prime_trial(n - p) for p in range(2, n // 2 + 1))
              for n in range(4, 10001, 2)))
    print("341 base2:", fermat_test(341, 2), "base3:", fermat_test(341, 3))
    print("91 base3:", fermat_test(91, 3), "base2:", fermat_test(91, 2))
    print("pseudoprimes base 2 <2000:", fermat_pseudoprimes(2, 2000))
    print("561 passes all coprime bases:", is_carmichael(561))
    print("Carmichael <10000:", [n for n in range(3, 10000) if korselt(n)])
    print("phi(p)=p-1 for primes<30:", all(phi(p) == p - 1 for p in sieve(30)))
    print("primitive roots mod 11:", primitive_roots(11), " mod 13:", primitive_roots(13))
    print("Lucas witness n=101:", lucas_n_minus_1(101), " n=97:", lucas_n_minus_1(97))
    print("Mersenne exponents (LL) <130:", [p for p in sieve(130) if lucas_lehmer(p)])
    print("2^67-1 prime?", lucas_lehmer(67), "| 2^127-1 prime?", lucas_lehmer(127))
    print("2^67-1 =", 2 ** 67 - 1, "= 193707721 * 761838257287")
    print("perfect numbers <10000:", [n for n in range(2, 10000) if sigma_proper(n) == n])
    print("antiprimes <400:", antiprimes(400))
    print("egcd(240,46):", egcd(240, 46))
    print("RSA (n, phi, d, cipher, decrypted):", rsa_demo())
    fig_pi_x(); fig_ulam(); fig_gaps(); fig_mod4_race()
    print("figures saved")
