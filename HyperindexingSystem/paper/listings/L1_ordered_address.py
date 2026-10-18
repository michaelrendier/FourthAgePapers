# Listing 1 - the ordered address (bijective base-N): text <-> non-negative integer
def address(text, alphabet):
    """Rank of `text` among all strings over `alphabet`, shortest first, then alphabetical."""
    N, a = len(alphabet), 0
    for ch in text:
        a = a * N + alphabet.index(ch) + 1
    return a - 1

def text_at(a, alphabet):
    """Inverse of address(): the string whose rank is `a`."""
    N, out = len(alphabet), []
    a += 1
    while a > 0:
        a, r = divmod(a - 1, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def page_at(loc, alphabet, k):
    """Fixed-length page: the k-digit base-N numeral of `loc` (digit 0 = first symbol)."""
    N, out = len(alphabet), []
    for _ in range(k):
        loc, r = divmod(loc, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def loc_of(page, alphabet):
    """Inverse of page_at()."""
    N, loc = len(alphabet), 0
    for ch in page:
        loc = loc * N + alphabet.index(ch)
    return loc
