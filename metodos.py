import pandas as pd
import numpy as np
import math
import sympy as sym

def incremental_search(f, xinit, dx, n):
    x0 = xinit
    fx0 = f(x0)
    res = []
    cont = 1
    if fx0 == 0:
        res.append([cont, x0, x0])
        cont += 1
    actual_iterations = 1
    x1 = x0 + dx
    fx1 = f(x1)

    while actual_iterations < n:
        x0 = x1
        x1 = x0 + dx

        fx0 = fx1
        fx1 = f(x1)

        if fx1 == 0:
            res.append ([cont, x1, x1])
            cont+=1
        elif fx0 * fx1 < 0:
            res.append ([cont, x0, x1])
            cont+=1

        actual_iterations = actual_iterations + 1

    return res


def biseccion(f, xi, xs, tol, niter):
    Xi = xi
    Xs = xs
    Tol = tol
    Niter = niter
    Fun = f
    res = []
    fm=[]
    E=[]
    xn=[]
    N=[]
    a = []
    b= []
    c=0
    # Se evalúa la función en el límite inferior (Xi) y el superior (Xs) y se guardan los valores
    x=Xi
    fi=eval(Fun)
    x=Xs
    fs=eval(Fun)
    Error = 0
    res2= 'nan'

    # Se verifica si alguna de las funciones evaluadas da cero, es decir, si Xi o Xs es raíz.
    if fi==0:
        s=Xi
        E=0
        res2 = (Xi, "es raiz de f(x)")
    elif fs==0:
        s=Xs
        E=0
        res2 = (Xs, "es raiz de f(x)")
    elif fs*fi<0:
        # Se verifica que haya un cambio de signo
        c=0

        #Si lo hay, se encuentra el punto medio entre los límites Xi y Xs
        Xm=(Xi+Xs)/2
        x=Xm
        fe=eval(Fun)
        fm.append(fe)
        N.append(c)
        E.append(100)
        xn.append(x)

        # Si el punto medio NO es raíz, se continúa con el ciclo.
        while E[c]>Tol and fe!=0 and c<Niter:
            a.append(Xi)
            b.append(Xs)
            # Si entre f(Xi) y f(Xm) (punto medio) hay un cambio de signo, se asume que en ese intervalo está la raíz y Xm pasa a 
            # ser el límite superior de un intervalo
            if fi*fe<0:
                Xs=Xm
                x=Xs
                fs=eval(Fun)
            else:
                # Si entre f(Xi) y f(Xm) no hay un cambio de signo, se asume que la raíz está en el intervalo [Xm, Xs], reemplazando Xi con Xm.
                Xi=Xm
                x=Xi
                fs=eval(Fun)
            
            #Se calcula el punto medio nuevamente y se almacena en X para la tabla, así como el cáculo del error y el número de la iteración.
            Xa=Xm
            Xm=(Xi+Xs)/2
            x=Xm
            fe=eval(Fun)
            fm.append(fe)
            xn.append(x)
            Error=abs(Xm-Xa)
            E.append(Error)
            c=c+1
            N.append(c)
        a.append(Xi)
        b.append(Xs)
        if fe==0:
            s=x
            res2 = (s,"es raiz de f(x)")
        elif Error<Tol:
            s=x
            res2 = (s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        else:
            s=x
            res2 = ("Fracaso en ",Niter, " iteraciones")
    else:
        res2=("El intervalo es inadecuado")

    for i in range(0, len(N)):
        res.append([N[i], a[i],xn[i],b[i], fm[i], E[i]])
    return res, res2


def regla_falsa(f,t_error,xinf,xsup,tol,niter):
    x=xinf
    fxinf=eval(f)
    x=xsup
    res2= 'nan'
    fxsup=eval(f)
    print(fxinf)
    print(fxsup)
    resultados = [] #matriz para guardar resultados

    # Se verifica si alguno de los límites del intervalo es raíz
    if fxinf==0:
        res2 =  (xinf," es raiz")
    elif fxsup==0:
        res2 =  (xsup," es raiz")
    elif fxinf*fxsup<0:
        #Si ninguno de los extremos es raíz, se verifica el cambio de signo

        #Se calcula el punto medio con la fórumla de la regla falsa y se almacena la función evaluada en ese punto, el error y el niter.
        xm = xinf-((fxinf*(xsup-xinf))/float(fxsup-fxinf))
        x=xm
        fxm=eval(f)
        contador=1
        error=float(tol)+1
        resultados.append([contador,xinf,xsup,xm,fxm,'nan'])
        while(fxm!=0 and error>tol and contador<niter):
            if fxinf*fxm<0:
                #Si hay un camnbio de signo entre el f(Xm) y f(xi), Xs pasa a ser el punto medio
                xsup=xm
                fxsup=fxm
            else:
                xinf=xm
                fxinf=fxm
            
            #Se calcula de nuevo Xm y f(Xm) para esta iteración
            temp=xm
            xm = xinf-((fxinf*(xsup-xinf))/float(fxsup-fxinf))
            x=xm
            fxm=eval(f)
            #Dependiendo del tipo de error (relativo o absoluto) se calcula y se guarda en la tabla
            if t_error == 1:
                error = abs(xm - temp)
            else:
                error=abs((xm-temp)/xm)
            contador+=1
            resultados.append([contador,xinf,xsup,xm,fxm,error])
        if fxm==0:
            res2= ("xm es raiz")
        elif error <= tol:
            res2 = ( xm," se aproxima a una raiz con una tolerancia de ",tol)
        else:
            res2= ("Maximo de iteraciones alcanzado")
    else:
        res2= ("El intervalo es inadecuado")
    return resultados, res2


def punto_fijo(f, g, x0, tol, niter):
    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f
    g = g
    res = []
    res2= 'nan'
    fn = []
    xn = []
    E = []
    N = []
    gx = []
    x = X0
    f = eval(Fun)
    c = 0
    Error = 100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)

    #Si la función evaluada en X0 es diferente de cero...
    while Error > Tol and f != 0 and c < Niter:
        #Se calcula x evaluando la función auxiliar con el x actual
        x = eval(g)
        gx.append(x)

        #Se evalúa la función original con el nuevo x calculado a partir de G
        fe = eval(Fun)
        fn.append(fe)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    gx.append(x)
    if fe == 0:
        s = x
        res2 = (s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s = x
        res2 = ("Fracaso en ", Niter, " iteraciones ")

    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], gx[i], E[i]])
    for i in res:
        print(i)
    return res, res2


def newton_raphson(f, df, x0, tol, niter):
    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f
    df = df
    res = []
    res2= 'nan'
    fn=[]
    xn=[]
    E=[]
    N=[]
    x=X0
    #f=eval(Fun)
    f = eval(Fun)
    derivada = eval(df)

    #derivada=eval(df)
    c=0
    Error=100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    while Error>Tol and f!=0 and derivada!=0  and c<Niter:
        # Se recalcula X según la fórmula de Newthon-Rhapson y se reevalúa en f y f' hasta que f sea igual a cero o cumpla las demás condiciones de parada
        x=x-f/derivada
        f = eval(Fun)
        derivada = eval(df)
        fn.append(f)
        xn.append(x)
        c=c+1
        Error=abs(xn[c]-xn[c-1]) ##Decimales correctos
        #Error=abs((xn[c]-xn[c-1])/xn[c]) ## Cifras significativas
        N.append(c)
        E.append(Error)
    if f==0:
        s=x
        res2 = (s,"es raiz de f(x)")
    elif Error<Tol:
        s=x
        res2 = (s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s=x
        res2 = ("Fracaso en ",Niter, " iteraciones ")


    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], E[i]])
    for i in res:
        print(i)
    return res, res2


def secante(x0, x1, f, tol, niter):
    X0 = x0
    X1 = x1
    Tol = tol
    Niter = niter
    Fun = f
    res = []
    res2= 'nan'
    fn = []
    xn = []
    E = []
    N = []
    #Se evalúa la función en x0 y x1
    x = X0
    f = eval(Fun)
    x = X1
    f1 = eval(Fun)
    c = 0
    Error = 100
    fn.append(f)
    fn.append(f1)
    xn.append(X0)
    xn.append(X1)
    E.append(Error)
    E.append(Error)
    N.append(c)
    c = c + 1
    N.append(c)
    while Error > Tol and f != 0 and c < Niter:
        # Se calcula X con el método de la secante y se evalúa nuevamente en f 
        x = xn[c] - ((fn[c] * (xn[c] - xn[c - 1])) / (fn[c] - fn[c - 1]))
        f = eval(Fun)
        fn.append(f)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    if f == 0:
        s = x
        res2 = (s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s = x
        res2 = ("Fracaso en ", Niter, " iteraciones ")


    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], E[i]])
    for i in res:
        print(i)
    return res, res2


def multiple_roots(x0, f, df, df2, tol, niter):
    X0 = x0
    Tol = tol
    Niter = niter
    Fun = f

    # print("derivate Function df:")
    df = df
    df2 = df2
    res2= 'nan'
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    d1 = []
    d2 = []
    res= []
    # f=eval(Fun)
    # derivada=eval(df)
    # derivada2=eval(df2)
    x = X0
    f = eval(Fun)
    x = X0
    derivada = eval(df)
    x = X0
    derivada2 = eval(df2)
    c = 0
    Error = 100
    fn.append(f)
    d1.append(derivada)
    d2.append(derivada2)
    xn.append(x)
    E.append(Error)
    N.append(c)

    while Error > Tol and derivada != 0 and c < Niter:
        # cálculo de x y los términos necesarios para calcular X desde el método de Newthon
        arriba = (f * derivada)
        abajo = ((derivada) ** 2) - ((f) * (derivada2))
        x = x - (arriba / abajo)
        # derivada=eval(df)
        # f=eval(Fun)
        f = eval(Fun)
        derivada = eval(df)
        derivada2 = eval(df2)
        fn.append(f)
        d1.append(derivada)
        d2.append(derivada2)
        xn.append(x)
        c = c + 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
    if f == 0:
        s = x
        res2 = (s, "es raiz de f(x)")
    elif Error < Tol:
        s = x
        res2 = (s, "es una aproximacion de un raiz de f(x) con una tolerancia", Tol)

    else:
        s = x
        res2 = ("Fracaso en ", Niter, " iteraciones ")

    for i in range(0, len(N)):
        res.append([N[i], xn[i], fn[i], E[i]])
    for i in res:
        print(i)
    return res, res2


def simple_gauss(a, b):
    ab = to_aug(a, b)
    res = []
    res.append(np.copy(ab).tolist())
    assert a.shape[0] == a.shape[1]

    size = a.shape[0]

    # Stages

    for i in range(0, size - 1):
        # Compute multiplier for row in stage.
        for j in range(i + 1, size):
            multiplier = ab[j][i] / ab[i][i]
            for k in range(i, size + 1):
                ab[j][k] = ab[j][k] - (multiplier * ab[i][k])
        res.append(np.copy(ab).tolist())

    return res


def to_aug(a, b):
    return np.column_stack((a, b))


def regressive_substitution(ab, labels=None):
    size = ab.shape[0]
    assert ab.shape[1] == size + 1

    solutions = np.zeros(size, dtype=np.float64)
    solutions[size - 1] = ab[size - 1][size] / ab[size - 1][size - 1]

    # Loop backwards
    for i in range(size - 2, -1, -1):
        accum = 0
        for p in range(i + 1, size):
            accum += ab[i][p] * solutions[p]
        solutions[i] = (ab[i][size] - accum) / ab[i][i]

    # Update the labels and assign its values
    labeled_xs = np.zeros(size)
    if labels is not None:
        for i, v in enumerate(labels):
            labeled_xs[labels[i]] = solutions[i]
        solutions = labeled_xs

    return solutions


def progressive_substitution(ab):
    size = ab.shape[0]
    assert ab.shape[1] == size + 1

    solutions = np.zeros(size, dtype=np.float64)
    solutions[0] = ab[0][size] / ab[0][0]

    for i in range(1, size):
        accum = 0
        for p in range(0, i):
            accum += ab[i][p] * solutions[p]

        solutions[i] = (ab[i][size] - accum) / ab[i][i]
    return solutions


def gauss_partial_pivot(a, b):
    ab = to_aug(a, b)
    assert a.shape[0] == a.shape[1]
    res = []
    res.append(np.copy(ab).tolist())
    size = a.shape[0]

    # Stages
    for k in range(0, size - 1):
        partial_pivot(ab, k)
        # Compute multiplier for row in stage.
        for i in range(k + 1, size):
            multiplier = ab[i][k] / ab[k][k]
            for j in range(k, size + 1):
                ab[i][j] = ab[i][j] - (multiplier * ab[k][j])
        res.append(np.copy(ab).tolist())
    return res


def gauss_total_pivot(a, b):
    ab = to_aug(a, b)
    assert a.shape[0] == a.shape[1]
    res = []
    res.append(np.copy(ab).tolist())
    size = a.shape[0]
    labels = list(range(0, size))

    # Stages
    for k in range(0, size - 1):
        total_pivot(ab, k, labels)
        # Compute multiplier for row in stage.
        for i in range(k + 1, size):
            multiplier = ab[i][k] / ab[k][k]
            for j in range(k, size + 1):
                ab[i][j] = ab[i][j] - (multiplier * ab[k][j])
        res.append(np.copy(ab).tolist())

    return res, labels


def partial_pivot(ab, k):
    largest = abs(ab[k][k])
    largest_row = k
    size = ab.shape[0]

    for r in range(k + 1, size):
        current = abs(ab[r][k])
        if current > largest:
            largest = current
            largest_row = r
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]


def total_pivot(ab, k, labels):
    largest = abs(ab[k][k])
    largest_row = k
    largest_column = k

    size = ab.shape[0]
    # i itera filas, j columnas
    for i in range(k, size):
        for j in range(k, size):
            current = abs(ab[i][j])
            if current > largest:
                largest = current
                largest_row = i
                largest_column = j
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]
        if largest_column != k:
            ab[:, [k, largest_column]] = ab[:, [largest_column, k]]
            labels[k], labels[largest_column] = labels[largest_column], labels[k]


def lu_gauss(a, b):
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == b.shape[0]
    res=[]
    size = a.shape[0]
    #U
    #L
    lower_tri = np.identity(size, dtype=np.float64)
    #a = M
    # Stages
    for k in range(0, size - 1):
        # Compute multiplier for row in stage.
        for i in range(k + 1, size):
            multiplier = a[i][k] / a[k][k]
            for j in range(k, size):
                a[i][j] = a[i][j] - (multiplier * a[k][j])
                if i > j:
                    lower_tri[i][j] = multiplier
        u = np.copy(a)
        aux = k
        for i in range(aux +2 , size ):
            u[i] = 0
        res.append([u.tolist(), np.copy(lower_tri).tolist(), np.copy(a).tolist()])
    z = progressive_substitution(to_aug(lower_tri, b))
    return res, regressive_substitution(to_aug(a, z))


def LU_partial_decomposition(A, B):
    n, m = A.shape
    P    = np.identity(n)
    L    = np.identity(n)
    U    = A.copy()
    PF   = np.identity(n)
    LF   = np.zeros((n,n))
    for k in range(0, n - 1):
        index = np.argmax(abs(U[k:, k]))
        index = index + k 
        if index != k:
            P = np.identity(n)
            P[[index, k], k:n] = P[[k, index], k:n]
            U[[index, k], k:n] = U[[k, index], k:n] 
            PF = np.dot(P, PF)
            LF = np.dot(P, LF)
        L = np.identity(n)
        for j in range(k+1,n):
            L[j, k]  = -(U[j, k] / U[k, k])
            LF[j, k] =  (U[j, k] / U[k, k])
        U = np.dot(L,U)
    np.fill_diagonal(LF, 1)

    """ # Sustitución progresiva
    Z, x = [], []
    sum = 0
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i,j]*B[j]
        Z.append((B[i] - sum) / L[i, i])
    # Sustitución regresiva
    for i in range(U.shape[0]-1,-1,-1): 
        sum = 0
        for j in range(i, n):
            sum += U[i,j]*B[j]
        B[i] = B[i]/U[i,i] """
    for i in range(L.shape[0]): 
        for j in range(i):
            B[i] -= L[i,j]*B[j]
    # Sustitución regresiva
    for i in range(U.shape[0]-1,-1,-1): 
        for j in range(i+1, U.shape[1]):
            B[i] -= U[i,j]*B[j]
        B[i] = B[i]/U[i,i]
    
    return PF, LF, U, B


def crout(a, b):
    n = a.shape[0]
    lower_tri = np.identity(n, dtype=np.float64)
    upper_tri = np.identity(n, dtype=np.float64)
    res = []
    for k in range(0, n):
        sum0 = 0

        for p in range(0, k):
            sum0 += lower_tri[k][p] * upper_tri[p][k]
        lower_tri[k][k] = a[k][k] - sum0

        for i in range(k + 1, n):
            sum1 = 0
            for p in range(0, k):
                sum1 += lower_tri[i][p] * upper_tri[p][k]
            lower_tri[i][k] = a[i][k] - sum1

        for j in range(k + 1, n):
            sum2 = 0
            for p in range(0, k):
                sum2 += lower_tri[k][p] * upper_tri[p][j]
            upper_tri[k][j] = (a[k][j] - sum2) / lower_tri[k][k]
        res.append([np.copy(upper_tri),np.copy(lower_tri)])
    z = progressive_substitution(to_aug(lower_tri, b))
    return res, regressive_substitution(to_aug(upper_tri, z))


def dolittle_fac(a, b):
    size = a.shape[0]
    lower_tri = np.identity(size, dtype=np.float64)
    upper_tri = np.identity(size, dtype=np.float64)
    res = []
    for k in range(0, size):
        first_sum = 0
        # Compute lower_tri[k][k]
        for p in range(0, k):
            first_sum += lower_tri[k][p] * upper_tri[p][k]
        upper_tri[k][k] = a[k][k] - first_sum

        # Compute lower_tri[i][k]
        for i in range(k + 1, size):
            second_sum = 0
            for p in range(0, k):
                second_sum += lower_tri[i][p] * upper_tri[p][k]
            lower_tri[i][k] = (a[i][k] - second_sum) / upper_tri[k][k]

        # Compute upper_tri[k][j]
        for j in range(k + 1, size):
            third_sum = 0
            for p in range(0, k):
                third_sum += lower_tri[k][p] * upper_tri[p][j]
            upper_tri[k][j] = a[k][j] - third_sum
        res.append([np.copy(upper_tri),np.copy(lower_tri)])

    z = progressive_substitution(to_aug(lower_tri, b))
    return res, regressive_substitution(to_aug(upper_tri, z))


def cholesky_factorization(a, b):
    size = a.shape[0]
    lower_tri = np.identity(size, dtype=np.float64)
    upper_tri = np.identity(size, dtype=np.float64)
    res = []
    for k in range(0, size):
        first_sum = 0
        # Compute lower_tri[k][k]
        for p in range(0, k):
            first_sum += lower_tri[k][p] * upper_tri[p][k]
        upper_tri[k][k] = np.sqrt(a[k][k] - first_sum)
        lower_tri[k][k] = upper_tri[k][k]

        # Compute lower_tri[i][k]
        for i in range(k + 1, size):
            second_sum = 0
            for p in range(0, k):
                second_sum += lower_tri[i][p] * upper_tri[p][k]
            lower_tri[i][k] = (a[i][k] - second_sum) / lower_tri[k][k]

        # Compute upper_tri[k][j]
        for j in range(k + 1, size):
            third_sum = 0
            for p in range(0, k):
                third_sum += lower_tri[k][p] * upper_tri[p][j]
            upper_tri[k][j] = (a[k][j] - third_sum) / upper_tri[k][k]
        res.append([np.copy(upper_tri), np.copy(lower_tri)])
    z = progressive_substitution(to_aug(lower_tri, b))
    return res, regressive_substitution(to_aug(upper_tri, z))


def seidel(a, b, init, tol, n, err_type):
    table = []
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)
    res = []
    error = float("inf")
    xn = init
    i = 0

    #Cálculo del radio espectral
    radio, msj = r_espectral(a, 2)

    table.append(i)
    table.append(xn)
    table.append("")
    table.append("")
    table.append("newline")
    res.append([i, xn.tolist(), "nan"])

    while error > tol and i < n:
        x, abs_err, rel_err = next_iter(a, b, xn)
        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1

        res.append([i, xn.tolist(), abs_err])

    return xn, res, radio, msj


def next_iter(a, b, prev_x):
    size = a.shape[0]
    x = np.copy(prev_x)

    for i in range(0, size):
        d = a[i][i]
        accum = 0
        for j in range(0, size):
            if j != i:
                accum += a[i][j] * x[j]
        x[i] = (b[i] - accum) / d

    errs = abs(x - prev_x)
    abs_err = max(errs)
    rel_err = max(errs / abs(x))

    return x, abs_err, rel_err


def jacobi(a, b, init, tol, n, err_type):
    table = []
    assert a.shape[0] == a.shape[1]
    assert a.shape[0] == len(b)
    assert len(init) == len(b)
    res = []
    error = float("inf")

    xn = init
    i = 0

    #Cálculo del radio espectral
    radio, msj = r_espectral(a, 1)

    table.append(i)
    table.append(xn)
    table.append("")
    table.append("")
    table.append("newline")
    res.append([i, xn.tolist(), "nan"])
    while error > tol and i < n:
        x, abs_err, rel_err = next_iter2(a, b, xn)
        xn = x

        if err_type == "rel":
            error = rel_err
        else:
            error = abs_err

        i += 1

        res.append([i, xn.tolist(), abs_err])
        table.append("newline")
    return xn, res, radio, msj


def next_iter2(a, b, prev_x):
    size = a.shape[0]
    x = np.zeros(size, dtype=np.float64)

    for i in range(0, size):
        d = a[i][i]
        accum = 0
        for j in range(0, size):
            if j != i:
                accum += a[i][j] * prev_x[j]
        x[i] = (b[i] - accum) / d

    errs = abs(x - prev_x)
    abs_err = np.max(np.abs(errs))
    rel_err = np.max(errs / np.abs(x))

    return x, abs_err, rel_err


def sor(A,x0,b,Tol,niter,w):
    c=0
    E = []
    resultado = []
    error=Tol+1
    E.append(error)
    print('ESTOS ES A')
    print(A)
    D = np.diag(np.diag(A))
    print('esto es D sin diag:')
    print(D)
    L = -np.tril(A,-1)
    U = -np.triu(A, 1)
    resultado.append([c,x0,error])
    print('L')
    print(L)
    print('U')
    print(U)
    print('w')
    print(w)
    while error>Tol and c<niter:
        term11 = w*L
        print('Term 11')
        print(term11)
        term12 = D-term11
        print('Term 12')
        print(term12)
        term1I = np.linalg.inv(term12)
        print('Term 1I')
        print(term1I)
        term1 = np.linalg.inv(D-(w*L))
        print('Term 1')
        print(term1)
        term21 = (1-w)*D
        print('Term 21')
        print(term21)
        term22 = w*U
        print('Term 22')
        print(term22)
        term2= term21+term22
        print('Term 2')
        print(term2)
        T = term1 @ term2
        print('T')
        print(T)
        #T = np.dot(np.linalg.inv(D-(w*L)),((1-w)*D+(w*U)))
        #T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        radio, msj = r_espectral(T, 3)
        C = w * np.dot(np.linalg.inv(D-w*L),b)
        x1=np.dot(T,x0)+C
        E.append(np.linalg.norm(x1-x0))
        error=E[c]
        x0=x1
        c=c+1
        resultado.append([c,x0.tolist(),error])
        if error < Tol:
            s=x0
            n=c
            resultado_final="Solucion al sistema con una tolerancia de "+str(Tol)+" es "+str(s)
            return [resultado, radio, msj, resultado_final]
    s=x0
    n=c
    resultado_final="Fracasó"+str(niter)
    return [resultado, radio, msj, resultado_final]

# Recibe dos listas de puntos
def vandermonde_method(x,y):
        matrix = []
        coeficientes = []
        xn = np.array(x)
        yn = np.array([y]).T
        A = np.vander(xn)
        Ainv = np.linalg.inv(A)
        a = np.dot(Ainv, yn)
        matrix = A
        coeficientes = a
        return {'matrix': (matrix), 'coeficients':(coeficientes)}


def newton_interpolacion(x,y):
    n=len(y)
    Tabla=np.zeros([n,n])
    Tabla[:,0]=y
    for j in range(1,n):
            for i in range(n-j):
                Tabla[i][j] =  (Tabla[i+1][j-1] - Tabla[i][j-1]) / (x[i+j]-x[i])
    return {'table':(Tabla).tolist(),'coef':(Tabla[0]).tolist()}


def spline(x,y,d):
    n=len(x)
    A=np.zeros([(d+1)*(n-1),(d+1)*(n-1)] )
    b=np.zeros([(d+1)*(n-1),1])
    cua= []
    for i in range(0,len(x)):cua.append(x[i]*x[i])
    cub=[]
    for i in range(0,len(x)):cub.append(x[i]*x[i]*x[i])
    if d==1:
        c=0
        h=0
        for i in range(0,n-1):
            A[i,c]=x[i]
            A[i,c+1]=1
            b[i]=y[i]
            c=c+2
            h=h+1
        c=0
        for i in range(1,n):
            A[h,c]=x[i]
            A[h,c+1]=1
            b[h]=y[i]
            c=c+2
            h=h+1
    elif d==2:
        c=0
        h=0
        for i in range(0,n-1):
            A[i,c]=cua[i]
            A[i,c+1]=x[i]
            A[i,c+2]=1
            b[i]=y[i]
            c=c+3
            h=h+1
        c=0
        for i in range(1,n):
            A[h,c]=cua[i]
            A[h,c+1]=x[i]
            A[h,c+2]=1
            b[h]=y[i]
            c=c+3
            h=h+1
        c=0
        for i in range(1,n-1):
            A[h,c]=2*x[i]
            A[h,c+1]=1
            A[h,c+3]=-2*x[i]
            A[h,c+4]=-1
            b[h]=0
            c=c+4
            h=h+1
        A[h,0]=2
        b[h]=0
    elif d==3:
        c=0
        h=0
        for i in range(0,n-1):
            A[i,c]=cub[i]
            A[i,c+1]=cua[i]
            A[i,c+2]=x[i]
            A[i,c+3]=1
            b[i]=y[i]
            c=c+4
            h=h+1
        c=0
        for i in range(1,n):
            A[h,c]=cub[i]
            A[h,c+1]=cua[i]
            A[h,c+2]=x[i]
            A[h,c+3]=1
            b[h]=y[i]
            c=c+4
            h=h+1
        c=0
        for i in range(1,n-1):
            A[h,c]=3*cua[i]
            A[h,c+1]=2*x[i]
            A[h,c+2]=1
            A[h,c+4]=-3*cua[i]
            A[h,c+5]=-2*x[i]
            A[h,c+6]=-1
            b[h]=0
            c=c+4
            h=h+1
        c=0
        for i in range(1,n-1):
            A[h,c]=6*x[i]
            A[h,c+1]=2
            A[h,c+4]=-6*x[i]
            A[h,c+5]=-2
            b[h]=0
            c=c+4
            h=h+1
        A[h,0]=6*x[1]
        A[h,1]=2
        b[h]=0
        h=h+1
        A[h,c]=6*x[n-1]
        A[h,c+1]=2
        b[h]=0
    val=np.linalg.inv(A).dot(b)
    Tabla=np.reshape(val,(n-1,d+1))
    return Tabla.tolist()


def lagrange(puntos):
    x = sym.Symbol("x")
    size = np.size(puntos, 0)
    producto = 0
    arreglo_x = [i[0] for i in puntos]
    arreglo_y = [i[1] for i in puntos]
    ls = []
    for k in range(size):
        l = 1
        for i in range(size):
            if i != k:
                l = l * ((x - arreglo_x[i]) / (arreglo_x[k] - arreglo_x[i])) 
        ls.append(l)    
        producto = producto + l * (arreglo_y[k])
    producto = sym.simplify(sym.expand(producto))
    return producto, ls

def r_espectral(matriz_t, tipo):
    
    if tipo == 1:
        T = m_transicionJacobi(matriz_t)
    elif tipo == 2:
        T = m_transicionGS(matriz_t)
    else:
        eigenvalues, _ = np.linalg.eig(matriz_t)
        spectral_radius = np.max(np.abs(eigenvalues))

        if spectral_radius <= 0.89:
            msj = 'El radio espectral es menor a 1, por ende, el método convergerá.'
        else:
            msj = 'El radio espectral es muy cercano a 1, por ende, no se garantiza la convergencia del método.'

        return spectral_radius, msj

    print('MATRIZ D TRANSICION')
    print(T)
    eigenvalues, _ = np.linalg.eig(T)
    spectral_radius = np.max(np.abs(eigenvalues))

    if spectral_radius <= 0.89:
        msj = 'El radio espectral es menor a 1, por ende, el método convergerá.'
    else:
        msj = 'El radio espectral es muy cercano a 1, por ende, no se garantiza la convergencia del método.'

    return spectral_radius, msj

# Función para obtener la matriz de transición en el método de Jacobi
def m_transicionJacobi(a):
    size = a.shape[0]
    diagonal = np.diag(np.diag(a))
    lower = -np.tril(a, -1)
    upper = -np.triu(a, 1)

    # Calcular la matriz de transición T = D^(-1) * (L + U)
    inv_diagonal = np.linalg.inv(diagonal)
    matrix_T = np.dot(inv_diagonal, lower + upper)

    return matrix_T

def m_transicionGS(a):
    size = a.shape[0]
    diagonal = np.diag(np.diag(a))
    lower = -np.tril(a, -1)
    upper = -np.triu(a, 1)

    # Calcular la matriz de transición T = (D - L)^(-1) * U
    d_l = diagonal - lower
    inv_diagonal_minus_lower = np.linalg.inv(d_l)
    matrix_T = np.dot(inv_diagonal_minus_lower, upper)

    return matrix_T
