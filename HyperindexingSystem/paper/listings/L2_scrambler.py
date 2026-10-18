# Listing 2 - an invertible scrambler of [0, N): LCG + xorshift, cycle-walked into range
def make_scrambler(N, a=1664525, c=1013904223, s1=7, s2=5):
    e = max(1, (N - 1).bit_length()); M = 1 << e; mask = M - 1
    a_inv = pow(a, -1, M)                       # a odd -> invertible mod 2^e
    def f(x):                                   # bijection on [0, M)
        x = (a * x + c) & mask                  # Hull-Dobell: a = 1 mod 4, c odd
        x ^= x >> s1
        x ^= (x << s2) & mask
        return x
    def finv(y):
        z = y
        for _ in range(e // s2 + 1): z = y ^ ((z << s2) & mask)
        y = z
        for _ in range(e // s1 + 1): z = y ^ (z >> s1)
        return (a_inv * (z - c)) & mask
    def scramble(x):                            # bijection on [0, N)
        x = f(x)
        while x >= N: x = f(x)
        return x
    def unscramble(y):
        y = finv(y)
        while y >= N: y = finv(y)
        return y
    return scramble, unscramble
