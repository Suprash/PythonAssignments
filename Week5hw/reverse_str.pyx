# reverse_str.pyx
# Contains: reverse_str, dot_product, sum_of_squares

def reverse_str(s: str) -> str:
    if not s:
        return ""
    b = s.encode("utf-32-le")
    n = len(b)
    unit = 4
    count = n // unit

    out = bytearray(n)
    src = memoryview(b)
    dst = memoryview(out)
    cdef Py_ssize_t i

    for i in range(count):
        dst[i*unit:(i+1)*unit] = src[(count-1-i)*unit:(count-i)*unit]

    return bytes(out).decode("utf-32-le")


# =======================
# 1. Dot Product
# =======================

def dot_product(double[:] a, double[:] b):
    cdef Py_ssize_t i, n
    n = a.shape[0]

    if b.shape[0] != n:
        raise ValueError("Vectors must have same length")

    cdef double s = 0

    for i in range(n):
        s += a[i] * b[i]

    return s


# =======================
# 2. Sum of Squares
# =======================

def sum_of_squares(int n):
    cdef long long i
    cdef long long total = 0

    for i in range(1, n + 1):
        total += i * i

    return total
