from sympy import sympify

class NewtonRaphson():

    def newton_raphson(f, df, x0, tol, max_iterations):
        """
        Encuentra una raíz de la función f(x) utilizando el método de Newton-Raphson.

        Args:
        f: Cadena de texto que representa la función f(x) que se evalúa.
        df: Cadena de texto que representa la derivada de la función f(x).
        x0: Valor inicial para comenzar la iteración.
        tol: Tolerancia para el error absoluto entre las aproximaciones sucesivas. Debe ser un número positivo.
        max_iterations: Número máximo de iteraciones permitidas. Debe ser un entero positivo.

        Returns:
        Una tupla con dos elementos. El primer elemento es una lista de listas con los resultados de cada iteración,
        donde cada lista contiene el número de iteración, el valor de x en la iteración actual, el valor de f(x) en la
        iteración actual y el error absoluto entre las aproximaciones sucesivas. El segundo elemento es un mensaje
        indicando si se encontró una raíz o si se alcanzó el número máximo de iteraciones.
        """

        def eval_f(x):
            return float(sympify(f).evalf(subs={sympify('x'): x}))

        def eval_df(x):
            return float(sympify(df).evalf(subs={sympify('x'): x}))

        results = []
        x = x0
        fx = eval_f(x)
        dfx = eval_df(x)
        iteration = 0
        error = tol + 1
        results.append([iteration, '{:.10f}'.format(x), '{:.1e}'.format(fx).replace('e-0', 'e-'),'NaN'])
        while fx != 0 and dfx != 0 and error > tol and iteration < max_iterations:
            x_prev = x
            x -= fx / dfx
            fx = eval_f(x)
            dfx = eval_df(x)
            error = abs(x_prev - x)
            iteration += 1
            results.append([iteration, '{:.10f}'.format(x), '{:.1e}'.format(fx).replace('e-0', 'e-'), '{:.1e}'.format(error).replace('e-0', 'e-')])
        if fx == 0:
            return results, f"An approximation of the roof was found for m = {x}"
        elif error <= tol:
            return results, f"An approximation of the roof was found for m = {x}"
        else:
            return results, "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"