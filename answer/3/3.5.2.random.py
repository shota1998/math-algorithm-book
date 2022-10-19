import random

N = 1_000_000
M = 0

for i in range(N):
    px = 6.0 * random.random()
    py = 9.0 * random.random()

    dist_33 = ((px - 3.0) ** 2 + (py - 3.0) ** 2) ** 0.5
    dist_37 = ((px - 3.0) ** 2 + (py - 7.0) ** 2) ** 0.5
    
    if dist_33 <= 3.0 or dist_37 <= 2.0:
        M += 1

print(M)