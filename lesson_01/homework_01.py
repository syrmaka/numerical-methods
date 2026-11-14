import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# задача 1
p = [(3.14, math.pi), (2.718, math.e), (9.8, 9.81), (0.333, 1/3)]
names = ["pi", "e", "g", "1/3"]

for i in range(len(p)):
    x, xt = p[i]
    dx = abs(x - xt)
    d = dx / xt * 100
    print(names[i], "dx=", round(dx, 8), "delta=", round(d, 4), "%")

# порядок
s1 = sorted(p, key=lambda t: abs(t[0] - t[1]))
s2 = sorted(p, key=lambda t: abs(t[0] - t[1]) / t[1])
print("по dx:", [names[p.index(t)] for t in s1])
print("по %:", [names[p.index(t)] for t in s2])

# задача 2
print()
for n, x, xt in [("мост", 1247, 1250), ("болт", 9.7, 10)]:
    print(n, "dx=", abs(x - xt), "delta=", abs(x - xt) / xt * 100, "%")

# задача 3
def relative_error(approx, exact):
    if exact == 0:
        return float("inf")
    return abs(approx - exact) / abs(exact)

print()
for i in range(len(p)):
    print(names[i], relative_error(p[i][0], p[i][1]))
print("ноль:", relative_error(1, 0))

# задача 4
print()
x = 47.3
e = 0.001
print(x / (1 + e), "..", x / (1 - e))

# задача 5
print()
print("|T|*0.005 <= 0.3  =>  |T| <= 60")
print("то есть B точнее A при температуре от -60 до 60")

# задача 6
print()
vals = ["0.004520", "1200", "1.200", "10.03", "0.03050", "250000"]
forms = ["4.520e-3", "1.2e3", "1.200e0", "1.003e1", "3.050e-2", "2.5e5"]
cnt = [4, 2, 4, 4, 4, 2]
for i in range(6):
    print(vals[i], "->", forms[i], "| значащих:", cnt[i])

# задача 7
print()
x = 4.738291
print(round(x, 2), "+- 0.02")
print("в 4.74 три значащие; 4.738291 писать нельзя - лишние цифры")

# задача 8
print()
print(round(0.5), round(1.5), round(2.5), round(3.5))
print(round(-0.5), round(-1.5), round(-2.5))
print("это banker's rounding, к чётному")
print("если всегда вверх, на 1e6 чисел накопится сдвиг ~5e5")

# задача 9
print()
n = 100
ex = math.fsum(1/k for k in range(1, n+1))
a = 0.0
b = 0.0
for k in range(1, n+1):
    a += 1/k
    b += round(1/k, 3)
print("float :", a, "dS=", abs(a - ex))
print("round3:", b, "dS=", abs(b - ex))
print("во сколько раз хуже:", abs(b - ex) / abs(a - ex))

# задача 10
print()
s = 0.1 + 0.2
print(s)
print("==0.3:", s == 0.3, "| isclose:", math.isclose(s, 0.3))
print("dx=", s - 0.3)
print("0.1 в двоичной - бесконечная дробь, поэтому неточно")

# задача 11
print()
a = 1 + 1e-15
d = a - 1
print("(1+1e-15)-1 =", d, "| ждали 1e-15")
print("отн.погр.:", abs(d - 1e-15) / 1e-15 * 100, "%")

A, B, C = 1.0, 1e8, 1.0
D = B*B - 4*A*C
x1 = (-B + math.sqrt(D)) / (2*A)
x2_bad = (-B - math.sqrt(D)) / (2*A)
x2_ok = C / (A * (-B - math.sqrt(D)) / (2*A))
print("x1 =", x1)
print("x2 плохо =", x2_bad)
print("x2 хорошо =", x2_ok)
print("разница %:", abs(x2_bad - x2_ok) / abs(x2_ok) * 100)

# задача 12
print()
arr = [0.1] * 1_000_000
t = 0.0
for v in arr:
    t += v
print("for :", t)
print("sum :", sum(arr))
print("fsum:", math.fsum(arr))
print("эталон 1e5")
print("ошибка for :", abs(t - 1e5))
print("ошибка sum :", abs(sum(arr) - 1e5))
print("ошибка fsum:", abs(math.fsum(arr) - 1e5))

# задача 13
print()
small = [1e-10] * 500_000
big = [1e6] * 500_000
ex = math.fsum(small + big)
a = 0.0
for v in small:
    a += v
for v in big:
    a += v
b = 0.0
for v in big:
    b += v
for v in small:
    b += v
print("маленькие сначала:", a, "dS=", abs(a - ex))
print("большие сначала :", b, "dS=", abs(b - ex))
print("fsum            :", ex)

# задача 14
print()
x = 1.0
step = 1.0001
ex = math.exp(10000 * math.log(step))
hist = []
marks = [1e-9, 1e-6, 1e-3]
got = {}
for i in range(1, 10001):
    x *= step
    r = abs(x - ex) / ex
    hist.append(r)
    for m in marks:
        if m not in got and r > m:
            got[m] = i
for m in marks:
    print("delta >", m, "на шаге", got.get(m, "не дошло"))

plt.plot(hist)
plt.yscale("log")
plt.xlabel("step")
plt.ylabel("rel error")
plt.savefig("err.png")
print("сохранил err.png")

# задача 15
print()
n = 1_000_000
sf = 0.0
for _ in range(n):
    sf += 0.01
getcontext().prec = 28
sd = Decimal(0)
for _ in range(n):
    sd += Decimal("0.01")
si = 0
for _ in range(n):
    si += 1
print("exact :", Decimal(n) * Decimal("0.01"))
print("float :", sf)
print("Decimal:", sd)
print("int коп.:", si, "=", si / 100, "руб")
print("расхождение float:", sf - 10000)