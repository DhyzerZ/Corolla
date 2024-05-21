import numpy as np

class Vandermonde():
    def vandermonde(x, y):
        xn = np.array(x)
        yn = np.array([y]).T
        A = np.vander(xn)
        Ainv = np.linalg.inv(A)

        a = np.dot(Ainv, yn)

        tableListData = A
        coeficientes = []

        for i in a:
            num = '{:.10f}'.format(round(i[0], 10))
            coeficientes.append(num)

        fun = ''
        size = len(a)-1

        for i in coeficientes:

            if i[0] != '-':
                fun += f' + {i}*x^{size} '
            else:
                fun += f'{i}*x^{size} '
            
            size -= 1

        fun = fun.replace('*x^1','*x').replace('*x^0', '')

        data = {
            'resultados' : tableListData,
            'coeficientes' : fun
        }

        return data

