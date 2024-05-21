from math import *

class PuntoFijo():

    def fixed_point(f, g, x0, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) utilizando el método del punto fijo.

        Args:
            f: Función que se evalúa.
            g: Función de iteración.
            x0: Valor inicial para comenzar la iteración.
            tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
            max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

        Returns:
            Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
            donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
            iteración actual, el valor de g(x) en la iteración actual y el error absoluto entre las aproximaciones
            sucesivas. El segundo elemento es un mensaje indicando si se encontró una raíz o si se alcanzó el número
            máximo de iteraciones.
        """

        results = []

        x = float(x0)

        valorX = { 'x' : x}
        f = f.replace('^', '**')
        g = g.replace('^', '**')

        fx = eval(f, globals(), valorX)

        iteration = 0
        error = tol + 1

        gx = eval(g, globals(), valorX)   

        results.append([iteration, '{:.10f}'.format(x), '{:.10f}'.format(gx), '{:.1e}'.format(fx).replace('e-0', 'e-'), 'NaN'])
        while fx != 0 and error > tol and iteration < max_iterations:

            x = gx

            valorX['x'] = x
            
            fx = eval(f, globals(), valorX)

            error = abs(float(results[-1][1]) - x)
            iteration += 1

            gx = eval(g, globals(), valorX) 

            results.append([iteration, '{:.10f}'.format(x), '{:.10f}'.format(gx), '{:.1e}'.format(fx).replace('e-0', 'e-'), '{:.10f}'.format(error)])
        if fx == 0:
            return results, f"An approximation of the roof was found for m = {x}"
        elif error <= tol:
            return results, f"An approximation of the roof was found for m = {x}"
        else:
            return results, "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"