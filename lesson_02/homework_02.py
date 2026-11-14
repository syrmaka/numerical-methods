import math
import random
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

mp.mp.dps = 50

# задача 1
print("1) обусловленность")
print("sqrt", abs(1e-8 * (1/(2*math.sqrt(1e-8))) / math.sqrt(1e-8)))
print("log", abs(1.001 * (1/1.001) / math.log(1.001)))
print("x-1", abs(1.000001 / (1.000001 - 1)))
print("sin", abs((math.pi/2) * math.cos(math.pi/2) / math.sin(math.pi/2)))
print("самая плохая x-1, cond 1e6")

# задача 2
print()
a = 1 + 1e-8
b = 1.0
f0 = a - b
f1 = (a + 1e-9) - b
print("delta f", f1 - f0)
print("cond", a / (a - b))  # примерно 1e8

# задача 3
print()
prev = None
for e in [1e-2, 1e-4, 1e-6]:
    D = 4 - 4*(1-e)
    x = (2 - math.sqrt(D)) / 2
    shift = abs(1 - x)
    if prev is None:
        print(e, shift)
    else:
        print(e, shift, "отн", shift / prev)
    prev = shift

# задача 4
print()
# f = x^2-1 в точке 1 хорошо обусловлена, но плохой алгоритм теряет точность
for x in [1.0000001, 1.00001, 1.0001]:
    good = (x-1)*(x+1)
    bad = x*x - 1
    print(x, bad, good, abs(bad-good))

# задача 5
print()
for b in [1e8, 1e4, 1e12]:
    a = 1.0
    c = 1.0
    D = b*b - 4*a*c
    bad = (-b + math.sqrt(D)) / (2*a)
    good = (2*c) / (-b - math.sqrt(D))
    ex = mp.mpf(2*c) / (-mp.mpf(b) - mp.sqrt(mp.mpf(b)**2 - 4*mp.mpf(a)*mp.mpf(c)))
    print(b, "ошибки", abs(bad-float(ex))/float(ex), abs(good-float(ex))/float(ex))

# задача 6
print()
xs = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]
e1_list = []
e2_list = []
for x in xs:
    bad = (1 - math.cos(x)) / (x*x)
    good = 2 * math.sin(x/2)**2 / (x*x)
    ex = float((1 - mp.cos(mp.mpf(x))) / (mp.mpf(x)**2))
    e1 = abs(bad-ex) / ex
    e2 = abs(good-ex) / ex
    e1_list.append(e1)
    e2_list.append(e2)
    print(x, e1, e2)

plt.loglog(xs, e1_list, 'o-', label='bad')
plt.loglog(xs, e2_list, 's-', label='good')
plt.legend()
plt.savefig('plot6.png')

# задача 7
print()
for x in [1e4, 1e8, 1e12, 1e14, 1e16]:
    bad = math.sqrt(x+1) - math.sqrt(x)
    good = 1 / (math.sqrt(x+1) + math.sqrt(x))
    ex = float(mp.sqrt(mp.mpf(x)+1) - mp.sqrt(mp.mpf(x)))
    print(x, abs(bad-ex)/ex, abs(good-ex)/ex)

# задача 8
print()
for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    bad = math.log(1 + x)
    good = math.log1p(x)
    ex = float(mp.log(1 + mp.mpf(x)))
    print(x, abs(bad-ex)/ex, abs(good-ex)/ex)

# задача 9
print()
for n in [10**5, 10**6, 10**7]:
    arr = [1/k for k in range(1, n+1)]
    t = 0.0
    for v in arr:
        t += v
    s = sum(arr)
    fs = math.fsum(arr)
    ex = float(sum(1/mp.mpf(k) for k in range(1, n+1)))
    print(n, abs(t-ex)/ex, abs(s-ex)/ex, abs(fs-ex)/ex)

# задача 10
print()
x = 1e-8
ex = float((1 - mp.cos(mp.mpf(x))) / mp.mpf(x)**2)
b64 = (1 - math.cos(x)) / x**2
b32 = float(np.float32((1 - np.cos(np.float32(x))) / np.float32(x)**2))
g64 = 2 * math.sin(x/2)**2 / x**2
print("bad64", abs(b64-ex)/ex)
print("bad32", abs(b32-ex)/ex)
print("good64", abs(g64-ex)/ex)

# задача 11
print()
x = 1e-10
a = math.sqrt(x+1) - math.sqrt(x)
b = 1 / (math.sqrt(x+1) + math.sqrt(x))
ex = float(mp.sqrt(mp.mpf(x)+1) - mp.sqrt(mp.mpf(x)))
print("a == b", a == b)
print("a - ex", a - ex)
print("b - ex", b - ex)

# задача 12
print()
xs = np.logspace(2, 16, 8)
errs = []
for x in xs:
    bad = math.sqrt(x+1) - math.sqrt(x)
    ex = float(mp.sqrt(mp.mpf(x)+1) - mp.sqrt(mp.mpf(x)))
    errs.append(abs(bad-ex)/ex)
plt.figure()
plt.loglog(xs, errs, 'o-')
plt.savefig('plot12.png')
print("наклон", (math.log(errs[-1]) - math.log(errs[0])) / (math.log(xs[-1]) - math.log(xs[0])))

# задача 13
print()
print("python", sys.version.split()[0], "numpy", np.__version__)
random.seed(42)
a1 = [random.random() for _ in range(10**5)]
rng = np.random.default_rng(42)
a2 = rng.random(10**5)
for name, arr in [("random", a1), ("numpy", a2)]:
    print(name, sum(arr), math.fsum(arr), np.sum(arr))

# задача 14
print()
arr = [1e300, 1e-300, 0.0, 1e-320, float('inf'), float('nan')]
print("sum", sum(arr))
print("fsum", math.fsum(arr))  # тут может быть ошибка или nan
print("nan и inf ломают всё")

# задача 15
print()
xs = np.logspace(-16, -1, 8)
eb_list = []
eg_list = []
for x in xs:
    bad = math.log(1 + x)
    good = math.log1p(x)
    ex = float(mp.log(1 + mp.mpf(x)))
    eb_list.append(abs(bad-ex)/ex)
    eg_list.append(abs(good-ex)/ex)
    print("x", x, "err", eb_list[-1], eg_list[-1])

plt.figure()
plt.loglog(xs, eb_list, 'o-', label='bad')
plt.loglog(xs, eg_list, 's-', label='good')
plt.legend()
plt.savefig('plot15.png')