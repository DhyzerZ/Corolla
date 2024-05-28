class DoolittleDecomposition:
    def doolittle_factorization(A):
        """
        Realiza la factorización LU de la matriz A usando el método de Doolittle.

        Args:
            A: Matriz de coeficientes (lista de listas).

        Returns:
            Una tupla con dos elementos. El primer elemento es la matriz L y el segundo elemento es la matriz U.
        """
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for k in range(i, n):
                sum_ = sum(L[i][j] * U[j][k] for j in range(i))
                U[i][k] = A[i][k] - sum_

            L[i][i] = 1.0
            for k in range(i + 1, n):
                sum_ = sum(L[k][j] * U[j][i] for j in range(i))
                if U[i][i] == 0:
                    raise ValueError("División por cero")
                L[k][i] = (A[k][i] - sum_) / U[i][i]

        return L, U
