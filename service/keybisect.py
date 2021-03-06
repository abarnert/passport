"""Bisection algorithms."""

def key_insort_right(key, a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    kx = key(x)
    while lo < hi:
        mid = (lo+hi)//2
        if kx < key(a[mid]): hi = mid
        else: lo = mid+1
    a.insert(lo, x)

key_insort = key_insort_right   # backward compatibility

def key_bisect_right(key, a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    kx = key(x)
    while lo < hi:
        mid = (lo+hi)//2
        if kx < key(a[mid]): hi = mid
        else: lo = mid+1
    return lo

key_bisect = key_bisect_right   # backward compatibility

def key_insort_left(key, a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the left of the leftmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    kx = key(x)
    while lo < hi:
        mid = (lo+hi)//2
        if key(a[mid]) < kx: lo = mid+1
        else: hi = mid
    a.insert(lo, x)


def key_bisect_left(key, a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    kx = key(x)
    while lo < hi:
        mid = (lo+hi)//2
        if key(a[mid]) < kx: lo = mid+1
        else: hi = mid
    return lo
