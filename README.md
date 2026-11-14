# CT #1: Practicing Number Theory

## Name: Meharin Choudhury
## ID: IT-23040


# Introduction

Number Theory is one of the most important branches of mathematics and serves as the foundation of modern cryptography. This report explores several fundamental concepts including Greatest Common Divisor (GCD), Euclid’s Algorithm, Extended Euclid’s Algorithm, Prime Numbers, Modular Arithmetic, Chinese Remainder Theorem, Fermat’s Little Theorem, and Euler’s Theorem.


# 1. Greatest Common Divisor (GCD)

The Greatest Common Divisor of two integers \(a\) and \(b\) is the largest positive integer that divides both numbers.

## Formula

\[
gcd(a,b)
\]

## Example

\[
gcd(24,16)=8
\]

<img width="2175" height="2268" alt="image" src="https://github.com/user-attachments/assets/4fcc51ec-7095-4f6b-af5c-f3bdddae3859" />


## Output
8

# 2. Euclid's Algorithm

Euclid's Algorithm efficiently computes GCD using repeated division.

## Formula

\[
gcd(a,b)=gcd(b,a \bmod b)
\]

## Example

Find gcd(48,18)

- 48 mod 18 = 12
- 18 mod 12 = 6
- 12 mod 6 = 0

Therefore,

\[
gcd(48,18)=6
\]

## Python Code
def euclid(a, b):
    while b:
        a, b = b, a % b
    return a

print(euclid(48, 18))

## Output
6

# 3. Extended Euclidean Algorithm

The Extended Euclidean Algorithm finds integers \(x\) and \(y\) such that

\[
ax + by = gcd(a,b)
\]

## Example

\[
391(-3) + 299(4) = 23
\]

## Python Code
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y

print(extended_gcd(391, 299))

## Output
(23, -3, 4)

# 4. Least Common Multiple (LCM)

The Least Common Multiple of two integers is the smallest positive number divisible by both.

## Formula

\[
LCM(a,b)=\frac{a \times b}{GCD(a,b)}
\]

## Example

\[
LCM(24,16)=48
\]

## Python Code
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(24, 16))

## Output
48

# 5. Modular Arithmetic

A congruence relation is written as

\[
a \equiv b \pmod n
\]

## Example

\[
17 \equiv 2 \pmod 5
\]

because both leave remainder 2 when divided by 5.

Modular arithmetic is widely used in cryptographic algorithms such as RSA and Diffie-Hellman.


# 6. Modular Inverse

A number \(x\) is called the modular inverse of \(a\) modulo \(n\) if

\[
ax \equiv 1 \pmod n
\]

## Example

\[
2^{-1} \equiv 5 \pmod 9
\]

because

\[
2 \times 5 = 10 \equiv 1 \pmod 9
\]

## Python Code
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

print(mod_inverse(2, 9))

## Output
5

# 7. Chinese Remainder Theorem (CRT)

If

\[
x \equiv a \pmod m
\]

and

\[
x \equiv b \pmod n
\]

where \(gcd(m,n)=1\), then a unique solution exists modulo \(mn\).

## Example

\[
x \equiv 2 \pmod 3
\]

\[
x \equiv 3 \pmod 5
\]

Solution:

\[
x = 8
\]

## Python Code
from sympy.ntheory.modular import crt

moduli = [3, 5]
remainders = [2, 3]

solution = crt(moduli, remainders)

print(solution[0])

## Output
8

# 8. Prime Numbers

A prime number is a natural number greater than 1 that has exactly two positive divisors: 1 and itself.

## Examples

2, 3, 5, 7, 11, 13

Prime numbers are building blocks of Number Theory and play a crucial role in modern cryptography. RSA encryption relies heavily on the properties of large prime numbers.


# 9. Sieve of Eratosthenes

The Sieve of Eratosthenes is an efficient algorithm for generating all prime numbers up to a given limit.

## Python Code
n = 50

prime = [True] * (n + 1)

p = 2

while p * p <= n:

    if prime[p]:

        for i in range(p * p, n + 1, p):
            prime[i] = False

    p += 1

for i in range(2, n + 1):
    if prime[i]:
        print(i, end=" ")

## Output
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47


# 10. Fermat’s Little Theorem

If \(p\) is a prime number and \(gcd(a,p)=1\), then

\[
a^{p-1} \equiv 1 \pmod p
\]

## Example

\[
2^6 \equiv 1 \pmod 7
\]

## Python Verification
print(pow(2, 6, 7))

## Output
1


# 11. Euler's Totient Function

Euler’s Totient Function counts positive integers less than \(n\) that are coprime with \(n\).

## Notation

\[
\phi(n)
\]

## Example

\[
\phi(10)=4
\]

because 1, 3, 7 and 9 are coprime with 10.


# 12. Euler's Theorem

If

\[
gcd(a,n)=1
\]

then

\[
a^{\phi(n)} \equiv 1 \pmod n
\]

## Example

\[
3^4 \equiv 1 \pmod {10}
\]

## Python Verification
print(pow(3, 4, 10))


## Output
1


# Applications in Cryptography

- RSA Encryption
- Digital Signatures
- Secure Communication
- Public Key Infrastructure (PKI)
- Secure Key Exchange Protocols

Prime numbers, modular arithmetic, and number theoretic functions form the backbone of modern cryptographic systems.



# Conclusion

This exercise explored fundamental concepts of Number Theory including GCD, Euclid’s Algorithm, Extended Euclidean Algorithm, Modular Arithmetic, Chinese Remainder Theorem, Prime Numbers, Fermat’s Little Theorem, Euler’s Totient Function, and Euler’s Theorem. These concepts are fundamental in computational mathematics and modern cryptography.



# References

1. Maths and Physics Club, IIT Bombay - Number Theory and Cryptography Workshop
2. Day 1 Workshop Notes
3. Day 2 Prime Numbers Workshop Notes
4. https://github.com/mnp-club/Number_Theory_and_Cryptography_Workshop/tree/main/Number%20Theory
