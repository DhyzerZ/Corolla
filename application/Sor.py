import numpy as np

class SOR():
    def sor(a, b, x0, w, tol, n):
        
        a = np.array(a)
        b = np.array(b)

        tableListData = []
        tempMapIterData = {}
        cont = 0
        phi = x0[:]
        error = np.max(np.abs(np.matmul(a, phi) - b))
        while error > tol and cont < n:
            for i in range(a.shape[0]):
                sigma = 0
                for j in range(a.shape[1]):
                    if j != i:
                        sigma += a[i, j] * phi[j]
                phi[i] = (1 - w) * phi[i] + (w / a[i, i]) * (b[i] - sigma)
            error = np.max(np.abs(np.matmul(a, phi) - b))
            cont += 1

            phi = np.around(phi, decimals=10)

            tempMapIterData['iteracion'] = str(cont)
            tempMapIterData['E'] = '{:.1e}'.format(error).replace('e-0', 'e-')
            tempMapIterData['xn'] = str(phi)
            tableListData.append(tempMapIterData.copy())
            tempMapIterData.clear()

        
        return tableListData, f'It converges at point = {str(phi)}'
