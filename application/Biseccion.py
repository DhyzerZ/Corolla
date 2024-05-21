from math import *

class Biseccion():
    def bisection(f, a, b, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) en el intervalo [a, b] utilizando el método de bisección.

        Args:
            f: Función que se evalúa.
            a: Límite inferior del intervalo [a, b].
            b: Límite superior del intervalo [a, b].
            tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
            max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

        Returns:
            Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
            donde cada lista contiene el número de iteración, el límite inferior del intervalo, el valor medio del
            intervalo, el límite superior del intervalo, el valor de f(x) en el valor medio y el error absoluto entre las
            aproximaciones sucesivas. El segundo elemento es un mensaje indicando si se encontró una raíz o si se alcanzó
            el número máximo de iteraciones.
        
        """
        results = []
        a = float(a)
        b = float(b)

        valorX = { 'x' : a}

        fa = eval(f, globals(), valorX)   
        
        valorX['x'] = b

        fb = eval(f, globals(), valorX)  

        if fa == 0:
            return [], f"An approximation of the roof was found for m = {a}"
        elif fb == 0:
            return [], f"An approximation of the roof was found for m = {b}"
        elif fa * fb < 0:
            x = (a + b) / 2
            valorX['x'] = x

            fx = eval(f, globals(), valorX) 

            iteration = 1
            error = tol + 1
            results.append([iteration, '{:.10f}'.format(a), '{:.10f}'.format(x), '{:.10f}'.format(b), '{:.1e}'.format(fx).replace('e-0', 'e-'),'NaN'])

            while fx != 0 and error > tol and iteration < max_iterations:
                if fa * fx < 0:
                    b = x
                    fb = fx
                else:
                    a = x
                    fa = fx
                x_prev = x
                x = (a + b) / 2

                valorX['x'] = x
                fx = eval(f, globals(), valorX) 

                error = abs(x - x_prev)
                iteration += 1
                results.append([iteration, '{:.10f}'.format(a), '{:.10f}'.format(x), '{:.10f}'.format(b), '{:.1e}'.format(fx).replace('e-0', 'e-'),'{:.1e}'.format(error).replace('e-0', 'e-')])
            if fx == 0:
                return results, f"An approximation of the roof was found for m = {x}"
            elif error <= tol:
                return results, f"An approximation of the roof was found for m = {x}"
            else:
                return results, "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"

        else:
            return results, "Error: There was no found a root in the interval of the function"
