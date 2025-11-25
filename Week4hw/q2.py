import ctypes
lib = ctypes.CDLL('./myclib.so')

lib.add_two.argtypes = (ctypes.c_char_p,ctypes.c_char_p)
lib.add_two.restype = ctypes.c_char_p
result = lib.add_two("ab","cd")
print(result)