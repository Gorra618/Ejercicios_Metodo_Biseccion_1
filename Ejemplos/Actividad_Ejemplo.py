# errx = 1e-4

def function_ejemplo(x):
    return - x + 10

def biseccion(fun,a,b,nit,errx):
    f_a = fun(a)
    f_b = fun(b)
    
    if f_a * f_b > 0:
        return "Sin raiz"

    # BUCLE 
    i = 0   
    while b-a > errx and i < nit:
        i += 1
        c = (a + b) / 2
        f_c = fun(c)

        if f_a * f_c > 0:
            a = c
            f_a = f_c
        else:
            b = c
            f_b = f_c

    # FIN DEL BUCLE