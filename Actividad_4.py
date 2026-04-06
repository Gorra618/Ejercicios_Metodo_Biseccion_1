import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x - np.tan(x)

# Método de bisección
def biseccion(f, a, b, tol_error, max_iter):
    if f(a) * f(b) >= 0:
        return "Sin Raiz"
    
    iteraciones = []
    i = 0
    while i < max_iter:
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2
        iteraciones.append((c, fc))
        if abs(fc) < tol_error or error < tol_error:
            return c, iteraciones
        if f(a) * fc < 0:
            b = c
        else:
            a = c
        i += 1
    return c, iteraciones

# Parámetros
max_iter = 100
tol_error = 1e-5
a = 0.1
b = np.pi/2 - 0.01  # Evitar la asíntota de tan(x)

# Ejecutar bisección
raiz, pares = biseccion(f, a, b, tol_error, max_iter)

print(f"Raíz encontrada: x = {raiz:.8f}")
print(f"f(x) = {f(raiz):.2e}")
print(f"Iteraciones: {len(pares)}")

# Graficar función y puntos evaluados
x = np.linspace(0.01, np.pi/2 - 0.01, 500)
y = f(x)

plt.figure(figsize=(10,5))
plt.plot(x, y, label='f(x) = 2x - tan(x)')
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)

# Graficar los puntos evaluados
pares_x = [p[0] for p in pares]
pares_y = [p[1] for p in pares]
plt.scatter(pares_x, pares_y, color='red', s=30, label='Pares evaluados')

# Marcar la raíz encontrada
plt.scatter([raiz], [f(raiz)], color='green', s=80, label=f'Raíz: x={raiz:.6f}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Bisección para 2x = tan(x)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("Actividad_4.png")

 