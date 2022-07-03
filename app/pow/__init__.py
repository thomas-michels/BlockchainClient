"""
    Module for Proof of Work
"""

class ProofOfWork:
    """
        ProofOfWork class
    """

# from numba import vectorize
# import time
# import numpy as np

# @vectorize(['float32(float32, float32, float32)'], target='cuda')
# def VectorAdd(a, b, c):
#     return a + b + c

# def main():
#     N = 32000000

#     A = np.ones(N, dtype=np.float32)
#     B = np.ones(N, dtype=np.float32)
#     C = np.ones(N, dtype=np.float32)

#     start = time.time()
#     D = VectorAdd(A,B,C)
#     vector_add_time = time.time() - start

#     print(f"C[:5] = {D[:5]}")
#     print(f"C[-5:] = {D[-5:]}")
#     print(f"VectorAdd {vector_add_time}")

# main()