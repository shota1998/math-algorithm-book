import math

A, B, H, M = map(float, input().split())

PI = 3.14159265358979

AnH = 30.0 * H + 0.5 * M
AnM = 6.0 * M

Hx = A * math.cos(AnH * PI / 180.0)
Hy = A * math.sin(AnH * PI / 180.0)
Mx = B * math.cos(AnM * PI / 180.0)
My = B * math.sin(AnM * PI / 180.0)

dist = ((Hx - Mx) ** 2 + (Hy - My) ** 2) ** 0.5
print("%.12f" % dist)