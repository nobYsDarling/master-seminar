# https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf#7

# Test graph
# TODO extend to handle construction sides and have an alternative route, that would be chosen.
#
#               N0          N1
#               ˄           ˄
#            e0 1        e2 1
#            e1 |        e3 |
#             A 1         B 1
#      e4, e5   ˅  e6, e7   ˅  e8, e9
# N2 +˂-1----1->+˂-1-----1->+˂-1----1->+ N3
#               ˄           ˄
#           e10 1       e12 1
#           e11 |           |
#             C 1         D |
#      e13, e14 ˅  e15, e16 |  e17, e18
# N4 +˂-1----1->+˂-2-----1->+˂-1----1->+ N5
#               ˄           ˄
#           e19 1       e21 1
#           e20 |       e22 |
#               1           1
#               ˅           ˅
#               N6          N7
#
# vertices: A, B, C, D, N0, N1, N2, N3, N4, N5, N6, N7
# edges:
#   e0:  (A,  N0): 1       e12: (D,   B): 1
#   e1:  (N0,  A): 1       e13: (C,  N4): 1
#   e2:  (B,  N1): 1       e14: (N4,  C): 1
#   e3:  (N1,  B): 1       e15: (D,   C): 2
#   e4:  (A,  N2): 1       e16: (C,   D): 1
#   e5:  (N2,  A): 1       e17: (N5,  D): 1
#   e6:  (B,   A): 1       e18: (D,  N5): 1
#   e7:  (A,   B): 1       e19: (N6,  C): 1
#   e8:  (N3,  B): 1       e20: (C,  N6): 1
#   e9:  (B,  N3): 1       e21: (N7,  D): 1
#   e10: (C,   A): 1       e22: (D,  N7): 1
#   e11: (A,   C): 1

# Adjacency matrix
A = [
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],  # A
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],  # B
    [1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0],  # C
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # D
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N0
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N2
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N3
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N4
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # N5
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # N6
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # N7
]

E = ['A', 'B', 'C', 'D', 'N0', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7']

res = []
for i0, v0 in enumerate(E):
    for i1, v1 in enumerate(E):
        if v0 != v1 and A[i0][i1]:
            print((v0, v1))
            res.append((v0, v1))

print(res)
