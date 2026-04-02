import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x - np.cos(x)


x = np.linspace(-5, 5, 400)
y = f(x)

plt.axhline(0)  # eje x
plt.plot(x, y, label="f(x) = x - cos(x)")
plt.legend()
plt.title("Gráfica de f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.savefig("Actividad_1.png")


def biseccion(f, a, b, tol=1e-3, max_iter=100):
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo")
        return None

    for i in range(max_iter):
        c = (a + b) / 2

        if abs(f(c)) < tol or (b - a) / 2 < tol:
            print(f"Raíz aproximada: {c}")
            print(f"Iteraciones: {i+1}")
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Se alcanzó el máximo de iteraciones")
    return c
