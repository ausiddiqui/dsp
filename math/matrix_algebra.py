# Matrix Algebra

import numpy as np
A = np.array([[1, 2, 3],
              [2, 7, 4]])

B = np.array([[1, -1],
              [0, 1]])

C = np.array([[5, -1],
              [9, 1],
              [6, 0]])

D = np.array([[3,-2,-1],
              [1, 2, 3]])

u = np.array([[6, 2, -3, 5]])

v = np.array([[3, 5, -1, 4]])

w = np.array([[1],
              [8],
              [0],
              [5]])

# 1. Matric Dimensions
# Write the dimensions of each matrix.

#1.1) A
print "dimensions of A:", A.shape
# dimensions of A: (2, 3)

#1.2) B
print "dimensions of B:", B.shape
# dimensions of B: (2, 2)

#1.3) C
print "dimensions of C:", C.shape
# dimensions of C: (3, 2)

#1.4) D
print "dimensions of D:", D.shape
# dimensions of D: (2, 3)

#1.5) u
print "dimensions of u:", u.shape
# dimensions of u: (1, 4)

#1.6) w
print "dimensions of w:", w.shape
# dimensions of w: (4, 1)

# 2. Vector Operations
# Perform the following operations. Assume α = 6.

#2.1) u + v =
print u + v
# [[ 9  7 -4  9]]

#2.2) u - v =
print u - v
# [[ 3 -3 -2  1]]

#2.3) αu =
alpha = 6
print alpha * u
# [[ 36  12 -18  30]]

#2.4) u · v =
print np.inner(u, v)
# [[51]]

#2.5) ||u|| =
print np.linalg.norm(u)
# 8.60232526704

# 3. Matrix Operations
# Evaluate each of the following expressions, if it is defined; else fill in with "not defined." Do your work by hand on scratch paper.

#3.1) A + C =
print "A + C = not defined"
# A + C = not defined

#3.2) A - C^t =
print A - np.transpose(C)
# [[-4 -7 -3]
# [ 3  6  4]]

#3.3) C^t + 3D =
print np.transpose(C) + 3 * D
# [[14  3  3]
# [ 2  7  9]]

#3.4) BA =
np.dot(B, A)
# array([[-1, -5, -1],
#       [ 2,  7,  4]])

#3.5) BA^T =
print "np.dot(B, np.tranpose(A)) = not defined"
# np.dot(B, np.tranpose(A)) = not defined

# Optional

#3.6) BC =
print "np.dot(B, C) = not defined"
# np.dot(B, C) = not defined

#3.7) CB =
print np.dot(C, B)
# [[ 5 -6]
# [ 9 -8]
# [ 6 -6]]

#3.8) B^4 =
print B**4
# [[1 1]
# [0 1]]

#3.9) AA^T =
print np.dot(A,np.transpose(A))
# [[14 28]
# [28 69]]

#3.10) D^T D =
print np.dot(np.transpose(D),D)
# [[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
