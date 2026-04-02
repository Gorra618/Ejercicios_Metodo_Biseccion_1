import numpy as np
import matplotlib.pyplot as plt


# algoritmo
def f(x):
    return x - np.cos(x)


tol = 1e-3


def biseccion(f, a, b, tol):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return "Sin raiz"

    c = a
    iter_count = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iter_count += 1
        if iter_count > 1000:
            break

    return (a + b) / 2


# grafico
x = np.linspace(-5, 5, 1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = x - cos(x)", linewidth=2)
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.grid(True, alpha=0.3)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gráfica de f(x) = x - cos(x)")
plt.legend()
plt.savefig("Actividad_1.png", dpi=150, bbox_inches="tight")
plt.savefig("Actividad_1.png")


a = -5
b = 5

existe_raiz = f(a) * f(b) < 0
print(f"\n¿Existe una raíz en [{a},{b}]?: {existe_raiz}")

if existe_raiz:
    raiz = biseccion(f, a, b, tol)
    print(f"Raíz aproximada (tol={tol}): {raiz:.6f}")
    print(f"f(raíz) = {f(raiz)}")
