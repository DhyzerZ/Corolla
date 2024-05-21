import numpy as np
from numpy.linalg import inv, eigvals, norm

class Seidel():
    def seidel(a, b, x0, n, tol):
        tableListData = []
        tempMapIterData = {}

        l = -np.tril(a, -1)
        u = -np.triu(a, 1)
        d = a + l + u
        t = np.matmul(inv(d - l), u)
        c = np.matmul(inv(d - l), b)

        if np.max(abs(eigvals(t))) > 1:
            return tableListData , "The function doesn't converge"
        
        if np.linalg.det(a) == 0:
            return tableListData, "det(A) is 0. The method cannot be executed."

        xn = np.matmul(t, x0) + c
        cont = 1
        error = np.max(np.abs(x0 - xn))

        tempMapIterData['iteracion'] = str(cont)
        tempMapIterData['x0'] = str(x0)
        tempMapIterData['xn'] = str(xn)
        tempMapIterData['E'] = '{:.1e}'.format(error).replace('error-0', 'error-')
        tableListData.append(tempMapIterData.copy())
        tempMapIterData.clear()

        while (x0 != xn).all() and cont < n and error > tol:
            x0 = xn
            xn = np.matmul(t, x0) + c
            cont += 1
            error = np.max(np.abs(x0 - xn))

            xn = np.around(xn, decimals=10)

            tempMapIterData['iteracion'] = str(cont)
            tempMapIterData['x0'] = str(x0)
            tempMapIterData['xn'] = str(xn)
            tempMapIterData['E'] = '{:.1e}'.format(error).replace('error-0', 'error-')
            tableListData.append(tempMapIterData.copy())
            tempMapIterData.clear()

        return tableListData, f'It converges at point = {str(xn)}'

