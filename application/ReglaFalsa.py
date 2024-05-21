from math import *

class ReglaFalsa():

    def false_position(f, a, b, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) en el intervalo [a, b] usando el método de la regla falsa.

        Args:
            f: Función que se evalúa.
            a: Límite inferior del intervalo en el que se busca la raíz.
            b: Límite superior del intervalo en el que se busca la raíz.
            tol: Tolerancia para el error relativo o absoluto. Debe ser un número positivo.
            max_iterations: Número máximo de iteraciones a realizar. Debe ser un entero positivo.

        Returns:
            Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
            donde cada lista contiene el número de iteración, el límite inferior del intervalo, el límite superior del
            intervalo, el valor de x en el que se evalúa f(x), el valor de f(x) y el error relativo o absoluto. El segundo
            elemento es un mensaje indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.

        """

        results = []

        a = float(a)
        b = float(b)

        valorX = { 'x' : a}

        f = f.replace('^', '**')

        fa = eval(f, globals(), valorX)   
        
        valorX['x'] = b

        fb = eval(f, globals(), valorX)  

        if fa == 0:
            return [], f"An approximation of the roof was found for m = {a}"
        elif fb == 0:
            return [], f"An approximation of the roof was found for m = {b}"
        elif fa * fb < 0:
            x = (a * fb - b * fa) / (fb - fa)

            valorX['x'] = x

            fx = eval(f, globals(), valorX)  

            iteration = 1
            error = tol + 1
            results.append([iteration, '{:.10f}'.format(a), '{:.10f}'.format(x), '{:.10f}'.format(b),'{:.1e}'.format(fx).replace('e-0', 'e-'), 'NaN'])
            while fx != 0 and error > tol and iteration < max_iterations:
                if fa * fx < 0:
                    b = x
                    fb = fx
                else:
                    a = x
                    fa = fx
                x_prev = x
                x = (a * fb - b * fa) / (fb - fa)

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
