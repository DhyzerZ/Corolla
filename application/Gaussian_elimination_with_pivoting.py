class GaussianEliminationPP:
    def elimination_with_pivoting(A, b):
        """
        Realiza la eliminación gaussiana con pivoteo en la matriz A con el vector b.

        Args:
            A: Matriz de coeficientes (lista de listas).
            b: Vector de términos independientes (lista).

        Returns:
            Una lista con los valores de las variables del sistema de ecuaciones.
        """
        n = len(A)
        for i in range(n):
            # Pivoteo parcial
            max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
            if i != max_row:
                A[i], A[max_row] = A[max_row], A[i]
                b[i], b[max_row] = b[max_row], b[i]

            # Escalonar la matriz
            for j in range(i + 1, n):
                if A[i][i] == 0:
                    raise ValueError("División por cero")
                ratio = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= ratio * A[i][k]
                b[j] -= ratio * b[i]

        # Sustitución regresiva
        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = b[i]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]
            if A[i][i] == 0:
                raise ValueError("División por cero")
            x[i] /= A[i][i]

        return x
