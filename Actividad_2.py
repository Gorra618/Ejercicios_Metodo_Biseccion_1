import numpy as np


def biseccion(fun, a, b, nit=1e4, errx=1e-5):
    nit = int(nit)
    hx = []  # Historial de puntos medios
    hy = []  # Historial de valores funcionales
    
    fa = fun(a)
    fb = fun(b)
    
    if fa * fb > 0:
        return "Sin raiz"
    
    c = a
    iter_count = 0
    
    while (b - a) / 2 > errx:
        c = (a + b) / 2
        fc = fun(c)
        
        # Guardar en el historial
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
    
    return (np.array(hx), np.array(hy))


hx2, hy2 = biseccion(np.sin, 2, 4, nit=1e4, errx=1e-5)

for i, (x, y) in enumerate(zip(hx2[-10:], hy2[-10:]), len(hx2) - 9):
    print(f"x = {x} | f(x) = {y}")
