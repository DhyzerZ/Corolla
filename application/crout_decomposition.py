class CroutDecomposition:
    def crout_factorization(A):
        """
        Realiza la factorización LU de la matriz A usando el método de Crout.

        Args:
            A: Matriz de coeficientes (lista de listas).

        Returns:
            Una tupla con dos elementos. El primer elemento es la matriz L y el segundo elemento es la matriz U.
        """
        n = len(A)
        L = [[0.0] * n for _ in range(n)]
        U = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                sum_ = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = A[j][i] - sum_

            U[i][i] = 1.0
            for j in range(i + 1, n):
                sum_ = sum(L[i][k] * U[k][j] for k in range(i))
                if L[i][i] == 0:
                    raise ValueError("División por cero")
                U[i][j] = (A[i][j] - sum_) / L[i][i]

        return L, U
