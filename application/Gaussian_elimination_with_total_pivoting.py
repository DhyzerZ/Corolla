class GaussianEliminationTP:
    def elimination_with_total_pivoting(A, b):
        """
        Realiza la eliminación gaussiana con pivoteo total en la matriz A con el vector b.

        Args:
            A: Matriz de coeficientes (lista de listas).
            b: Vector de términos independientes (lista).

        Returns:
            Una lista con los valores de las variables del sistema de ecuaciones.
        """
        n = len(A)
        # Mantener un registro de los cambios de columna
        column_changes = list(range(n))

        for i in range(n):
            # Pivoteo total
            max_row, max_col = max(
                ((r, c) for r in range(i, n) for c in range(i, n)),
                key=lambda rc: abs(A[rc[0]][rc[1]])
            )
            if A[max_row][max_col] == 0:
                raise ValueError("La matriz es singular y no puede resolverse")

            # Intercambiar filas
            if i != max_row:
                A[i], A[max_row] = A[max_row], A[i]
                b[i], b[max_row] = b[max_row], b[i]

            # Intercambiar columnas
            if i != max_col:
                for row in A:
                    row[i], row[max_col] = row[max_col], row[i]
                column_changes[i], column_changes[max_col] = column_changes[max_col], column_changes[i]

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

        # Revertir los cambios de columna
        final_result = [0 for _ in range(n)]
        for i in range(n):
            final_result[column_changes[i]] = x[i]

        return final_result
