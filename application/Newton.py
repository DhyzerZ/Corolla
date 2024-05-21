import numpy as np
import warnings

class Newton():

    warnings.filterwarnings('error', category=RuntimeWarning)

    def newton(x, y):
        tableListData = []

        x = np.array(x)
        n = x.size
        y = np.array(y)
        try:
            D = np.zeros((n,n))
        except RuntimeWarning as e:
            raise ValueError(str(e))

        D[:,0]=y.T
        for i in range(1,n):
            aux0 = D[i-1:n,i-1]
            aux = np.diff(aux0)
            aux2 = x[i:n] - x[0:n-i]

            D[i:n,i] = aux/aux2.T  
            coeficientes = np.diag(D)

        tableListData.append(D.tolist())
        tableListData.append(coeficientes.tolist())

        matrix = []

        for i in tableListData[0]:

            arr = []

            for j in i:
                arr.append('{:.10f}'.format(j))

            matrix.append(arr)

        coef = []

        for i in tableListData[1]:

            coef.append('{:.10f}'.format(i))


        size = len(coef)

        fun = ''
        i = 0
        iterHechas = ''

        while i < size:
            
            if coef[i][0] != '-':
                fun += f'+ {coef[i]}'
            else:
                fun += f'{coef[i]}'

            iterHechas += f'*(x-{i}) '

            fun += iterHechas

            i += 1

        fun = fun.replace('*(x-0)','')
        

        data = {
            'resultados' : matrix,
            'coeficientes' : coef,
            'polinomio': fun
        }

        return data