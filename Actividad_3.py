import numpy as np
import matplotlib.pyplot as plt


def f(x):
    """Función f(x) = 4*sin(x) + 1 - x"""
    return 4 * np.sin(x) + 1 - x


def biseccion(fun, a, b, nit=1e4, errx=1e-5):
    nit = int(nit)
    hx = []
    hy = []

    fa = fun(a)
    fb = fun(b)

    if fa * fb > 0:
        return "Sin raiz"

    c = a
    iter_count = 0

    while (b - a) / 2 > errx:
        c = (a + b) / 2
        fc = fun(c)

        hx.append(c)
        hy.append(fc)

        if fc == 0:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iter_count += 1
        if iter_count > nit:
            break

    return (np.array(hx), np.array(hy), iter_count, nit, (b - a) / 2)


x_grafica = np.linspace(0, 2 * np.pi, 1000)
y_grafica = f(x_grafica)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x_grafica, y_grafica, "b-", linewidth=2, label="f(x) = 4sin(x) + 1 - x")
plt.axhline(y=0, color="k", linestyle="--", alpha=0.3)
plt.axvline(x=0, color="k", linestyle="--", alpha=0.3)
plt.grid(True, alpha=0.3)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Función f(x) = 4sin(x) + 1 - x")
plt.legend()

a_inicial = 0
b_inicial = np.pi

plt.subplot(1, 2, 1)
plt.axvline(
    x=a_inicial,
    color="g",
    linestyle=":",
    alpha=0.7,
    label=f"Intervalo: [{a_inicial:.2f}, {b_inicial:.2f}]",
)
plt.axvline(x=b_inicial, color="g", linestyle=":", alpha=0.7)
plt.fill_between([a_inicial, b_inicial], -10, 10, alpha=0.1, color="green")
plt.legend()

resultado = biseccion(f, a_inicial, b_inicial, nit=1e4, errx=1e-5)

if isinstance(resultado, str):
    print("Error: No se encontró raíz en el intervalo")
else:
    hx, hy, iter_count, nit_max, error_final = resultado

    raiz = hx[-1]
    valor_en_raiz = hy[-1]

    print(f"Raiz: {raiz}")
    print(f"f(raiz) = {valor_en_raiz}")
    print(f"Iteraciones: {iter_count}")
    print(f"Error: {error_final}")

    if iter_count >= nit_max:
        print("Finalizo por cantidad de iteraciones")
    else:
        print("Finalizo por error alcanzado")

    x_zoom = np.linspace(a_inicial, b_inicial, 500)
    y_zoom = f(x_zoom)

    plt.subplot(1, 2, 2)
    plt.plot(x_zoom, y_zoom, "b-", linewidth=2, label="f(x)")
    plt.axhline(y=0, color="k", linestyle="--", alpha=0.3)
    plt.scatter(
        hx,
        hy,
        color="red",
        s=30,
        alpha=0.6,
        label=f"Puntos bisección ({len(hx)} puntos)",
    )
    plt.scatter(
        [raiz],
        [valor_en_raiz],
        color="green",
        s=150,
        marker="*",
        label=f"Raíz: x={raiz}",
        zorder=5,
    )
    plt.grid(True, alpha=0.3)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Función y puntos evaluados por bisección\n({iter_count} iteraciones)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("Actividad_3.png")
