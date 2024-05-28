class GaussianElimination:
    def simple_elimination(A, b):
        """
        Realiza la eliminación gaussiana simple en la matriz A con el vector b.

        Args:
            A: Matriz de coeficientes (lista de listas).
            b: Vector de términos independientes (lista).

        Returns:
            Una lista con los valores de las variables del sistema de ecuaciones.
        """
        n = len(A)
        for i in range(n):
            # Escalonar la matriz
            for j in range(i+1, n):
                if A[i][i] == 0:
                    raise ValueError("División por cero")
                ratio = A[j][i] / A[i][i]
                for k in range(n):
                    A[j][k] -= ratio * A[i][k]
                b[j] -= ratio * b[i]

        # Sustitución regresiva
        x = [0 for _ in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = b[i]
            for j in range(i+1, n):
                x[i] -= A[i][j] * x[j]
            if A[i][i] == 0:
                raise ValueError("División por cero")
            x[i] /= A[i][i]

        return x