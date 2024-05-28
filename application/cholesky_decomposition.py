class CholeskyDecomposition:
    def cholesky_factorization(A):
        """
        Realiza la factorización de Cholesky de la matriz A.

        Args:
            A: Matriz de coeficientes (lista de listas).

        Returns:
            La matriz triangular inferior L tal que A = L * L^T.
        """
        import math
        n = len(A)
        L = [[0.0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                sum_ = sum(L[i][k] * L[j][k] for k in range(j))
                
                if i == j:  # Diagonal elements
                    if A[i][i] - sum_ <= 0:
                        raise ValueError("La matriz no es definida positiva.")
                    L[i][j] = math.sqrt(A[i][i] - sum_)
                else:
                    L[i][j] = (A[i][j] - sum_) / L[j][j]

        return L
