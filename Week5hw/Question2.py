#implement a function to compute the dot product of two 1D arrays (vectors) of length n using either Cython or CFFI

import numpy as np
import reverse_str

a = np.array([1.0,2.0,3.0], dtype = np.float64)
b = np.array([4.0, 5.0, 6.0], dtype=np.float64)
print("Dot product:", reverse_str.dot_product(a, b))