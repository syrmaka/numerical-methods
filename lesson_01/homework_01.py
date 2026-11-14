import math

# Задача 1
data = [
    ("3.14/pi",   3.14,  math.pi),
    ("2.718/e",   2.718, math.e),
    ("9.8/9.81",  9.8,   9.81),
    ("0.333/1/3", 0.333, 1/3),
]

print("1)")
for name, x, xt in data:
    dx = abs(x - xt)
    d = dx / abs(xt) * 100
    print(f"{name:12} dx={dx:.3e}  delta={d:.4f}%")

# порядок
print("sort dx:", [n for n, x, xt in sorted(data, key=lambda t: abs(t[1]-t[2]))])
print("sort %:",  [n for n, x, xt in sorted(data, key=lambda t: abs(t[1]-t[2])/abs(t[2]))])

# Задача 2
print("\n2)")
for name, x, xt in [("мост", 1247.0, 1250.0), ("болт", 9.7, 10.0)]:
    dx = abs(x - xt)
    print(name, "dx =", dx, "delta =", round(dx/xt*100, 4), "%")

# Задача 3
def relative_error(approx, exact):
    if exact == 0:
        return float("inf")
    return abs(approx - exact) / abs(exact)

print("\n3)")
for name, x, xt in data:
    print(name, relative_error(x, xt))
print("exact=0 ->", relative_error(1.0, 0))

# Задача 4
print("\n4)")
x = 47.3
e = 0.001
print(x/(1+e), x/(1-e))