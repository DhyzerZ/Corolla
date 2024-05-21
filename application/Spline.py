import numpy as np
from scipy import linalg

class Spline():
    def splineLineal(x, y):
        x = np.array(x)
        y = np.array(y)
        n = x.size
        m = 2*(n-1) #factor m para la formula de los trazadores
        A = np.zeros((m, m))
        b = np.zeros((m, 1))
        Coef = np.zeros((n-1, 2))
        i = 0
        # Interpolating condition
        while i < x.size-1:
            A[i+1, [2*i+1-1, 2*i+1]] = [x[i+1], 1]  #Realiza la formula de interpolacion de superficie 
            b[i+1] = y[i+1]
            i = i+1

        A[0, [0, 1]] = [x[0], 1]
        b[0] = y[0]
        i = 1
        # Condition of continuity
        while i < x.size-1:
            A[x.size-1+i, 2*i-2:2*i+2] = np.hstack((x[i], 1, -x[i], -1))
            b[x.size-1+i] = 0
            i = i+1
        Saux = linalg.solve(A, b)
        # Order Coefficients
        i = 0
        while i < x.size-1:
            Coef[i, :] = [Saux[2*i], Saux[2*i+1]]
            i = i+1

        output = Coef
        return output
    
    def splineCubica(x, y):
        x = np.array(x)
        y = np.array(y)
        n = x.size
        m = 4*(n-1)
        A = np.zeros((m,m))
        b = np.zeros((m,1))
        Coef = np.zeros((n-1,4))
        i = 0

        #Interpolating condition
        while i < x.size-1:
            
            A[i+1,4*i:4*i+4]= np.hstack((x[i+1]**3,x[i+1]**2,x[i+1],1)) 
            b[i+1]=y[i+1]
            i = i+1

        A[0,0:4] = np.hstack((x[0]**3,x[0]**2,x[0]**1,1))
        b[0] = y[0]
        #Condition of continuity
        i = 1
        while i < x.size-1:
            A[x.size-1+i,4*i-4:4*i+4] = np.hstack((x[i]**3,x[i]**2,x[i],1,-x[i]**3,-x[i]**2,-x[i],-1))
            b[x.size-1+i] = 0
            i = i+1
        #Condition of smoothness
        i = 1
        while i < x.size-1:
            A[2*n-3+i,4*i-4:4*i+4] = np.hstack((3*x[i]**2,2*x[i],1,0,-3*x[i]**2,-2*x[i],-1,0))
            b[2*n-3+i] = 0
            i = i+1
        
        #Concavity condition
        i = 1
        while i < x.size-1:
            A[3*n-5+i,4*i-4:4*i+4] = np.hstack((6*x[i],2,0,0,-6*x[i],-2,0,0))
            b[n+5+i] = 0
            i = i+1
        
        #Boundary conditions  
        A[m-2,0:2]=[6*x[0],2]
        b[m-2]=0
        A[m-1,m-4:m-2]=[6*x[x.size-1],2]
        b[m-1]=0
        
        Saux = linalg.solve(A,b)
        #Order Coefficients
        i = 0
        j = 0
        while i < n-1:
            Coef[i,:] = np.hstack((Saux[j],Saux[j+1],Saux[j+2],Saux[j+3]))
            i = i+1
            j = j + 4

        output = Coef
        return output
        
