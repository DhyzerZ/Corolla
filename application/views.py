from django.shortcuts import render
from application.Biseccion import Biseccion
from application.ReglaFalsa import ReglaFalsa
from application.PuntoFijo import PuntoFijo
from application.Jacobi import Jacobi
from application.Gauss import Seidel
from application.Sor import SOR
from application.Vandermonde import Vandermonde
from application.MultipleRoots import MultipleRoots
from application.NewtonRaphson import NewtonRaphson
from application.Secante import Secante
from application.Newton import Newton
from application.Spline import Spline
from application.Graficar import Graficas

# Create your views here.

def home(request):

    grafica = datos = default = None
    graficas = Graficas()  

    if request.POST:
        funcion = request.POST['funcion']

        datos = {
            'fun' : funcion
        }

        funcion = funcion.replace('^', '**')

        graficas.set_function_text(funcion)  
        grafica = graficas.graph_function() 
    
    else:
        graficas.set_function_text('x') 
        default = graficas.graph_function()  

    return render(request, 'index.html', {'graph' : grafica, 'default': default, 'datos': datos})


def bisection(request):

    resultado = mensaje = datos = None

    if request.POST:
        funcion = request.POST['funcion']
        intervaloA = request.POST['intervaloA']
        intervaloB = request.POST['intervaloB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        intervaloA = int(intervaloA)
        intervaloB = int(intervaloB)

        if intervaloA < intervaloB:

            tolerancia = float(tolerancia)
            iteraciones = int(iteraciones)

            datos = {
                'fun' : funcion,
                'a' : intervaloA,
                'b' : intervaloB,
                'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                'iter' : iteraciones
            }

            funcion = funcion.replace('^', '**')

            resultado, mensaje = Biseccion.bisection(funcion, intervaloA, intervaloB, tolerancia, iteraciones)
        
        else:

            mensaje = f'Error: \'a\' has to be less than \'b\': a = {intervaloA} and b = {intervaloB}'

    return render(request, 'bisection.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def false_position(request):
    
    resultado = mensaje = datos = None

    if request.POST:
        funcion = request.POST['funcion']
        intervaloA = request.POST['intervaloA']
        intervaloB = request.POST['intervaloB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        intervaloA = int(intervaloA)
        intervaloB = int(intervaloB)

        if intervaloA < intervaloB:

            tolerancia = float(tolerancia)
            iteraciones = int(iteraciones)

            datos = {
                'fun' : funcion,
                'a' : intervaloA,
                'b' : intervaloB,
                'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                'iter' : iteraciones
            }

            funcion = funcion.replace('^', '**')

            resultado, mensaje = ReglaFalsa.false_position(funcion, intervaloA, intervaloB, tolerancia, iteraciones)
        
        else:

            mensaje = f'Error: \'a\' has to be less than \'b\': a = {intervaloA} and b = {intervaloB}'

    return render(request, 'false-position.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def fixed_point(request):

    resultado = mensaje = datos = None

    if request.POST:
        funcionf = request.POST['funcionf']
        funciong = request.POST['funciong']   
        x0 = request.POST['x0']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        x0 = float(x0)
        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        datos = {
            'funf' : funcionf,
            'fung' : funciong,
            'x0' : x0,
            'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
            'iter' : iteraciones
        }

        funcionf = funcionf.replace('^', '**')
        funciong = funciong.replace('^', '**')

        resultado, mensaje = PuntoFijo.fixed_point(funcionf, funciong, x0, tolerancia, iteraciones)

    return render(request, 'fixed-point.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def gauss_seidel(request):
        
    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        try:
            matrizA = matriz(matrizA)
            x0 = matriz1(x0)
            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):
                
                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                }

                resultado, mensaje = Seidel.seidel(matrizA, matrizB, x0, iteraciones, tolerancia)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred in the input."

    return render(request, 'gauss-seidel.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def jacobi(request):

    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        try:

            matrizA = matriz(matrizA)
            x0 = matriz1(x0)
            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):
                
                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                }

                resultado, mensaje = Jacobi.jacobi(matrizA, matrizB, x0, iteraciones, tolerancia)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred in the input."

    return render(request, 'jacobi.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def multiple_roots(request):
    resultado = mensaje = datos = None

    if request.POST:
        funcion = request.POST['funcion']
        dfuncion = request.POST['dfuncion']
        d2funcion = request.POST['d2funcion']
        x0 = request.POST['x0']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']

        x0 = float(x0)
        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)

        datos = {
            'fun': funcion,
            'dfun': dfuncion,
            'd2fun': d2funcion,
            'x0': x0,
            'tol': '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
            'iter': iteraciones
        }

        resultado, mensaje = MultipleRoots.multiple_roots(funcion, dfuncion, d2funcion, x0, tolerancia, iteraciones)


    return render(request, 'multiple-roots.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def newton_raphson(request):

    result = message = data = None

    if request.POST:
        functionf = request.POST['functionf']
        functiondf = request.POST['functiond'] 
        x0 = request.POST['x0']
        tolerance = request.POST['tolerance']
        iterations = request.POST['iterations']

        x0 = float(x0)
        tolerance = float(tolerance)
        iterations = int(iterations)

        data = {
            'funf' : functionf,
            'fundf' : functiondf,
            'x0' : x0,
            'tol' : '{:.1e}'.format(tolerance).replace('e-0', 'e-'),
            'iter' : iterations
        }
        result, message = NewtonRaphson.newton_raphson(functionf, functiondf, x0, tolerance, iterations)

    return render(request, 'newton-raphson.html', {'result': result, 'message': message, 'data': data})

def secant(request):
    result = message = data = None

    if request.POST:
        functionf = request.POST['functionf']
        x0 = request.POST['x0']
        x1 = request.POST['x1']
        tolerance = request.POST['tolerance']
        iterations = request.POST['iterations']

        x0 = float(x0)
        x1 = float(x1)
        tolerance = float(tolerance)
        iterations = int(iterations)

        data = {
            'funf' : functionf,
            'x0' : x0,
            'x1' : x1,
            'tol' : '{:.1e}'.format(tolerance).replace('e-0', 'e-'),
            'iter' : iterations
        }

        result, message = Secante.secante(functionf, x0, x1, tolerance, iterations)

    return render(request, 'secant.html', {'result': result, 'message': message, 'data': data})

def sor(request):
            
    resultado = mensaje = datos = None

    if request.POST:

        matrizA = request.POST['matrizA']
        x0 = request.POST['x0']
        matrizB = request.POST['matrizB']
        tolerancia = request.POST['tolerancia']
        iteraciones = request.POST['iteraciones']
        w = request.POST['relax']

        tolerancia = float(tolerancia)
        iteraciones = int(iteraciones)
        w = float(w)

        try:
            matrizA = matriz(matrizA)
            x0 = matriz1(x0)
            matrizB = matriz1(matrizB)

            if size(matrizA) and size(x0) and size(matrizB) and len(matrizA) == len(x0) and len(matrizA) == len(matrizB):

                datos = {
                    'matrizA' : matrizA,
                    'matrizB' : matrizB,
                    'x0' : x0,
                    'tol' : '{:.1e}'.format(tolerancia).replace('e-0', 'e-'),
                    'iter' : iteraciones,
                    'relajacion' : w
                }

                resultado, mensaje = SOR.sor(matrizA, matrizB, x0, w, tolerancia, iteraciones)

            else:
                mensaje = "The matrixes had different sizes."

        except:
            mensaje = "An error has occurred in the input."

    return render(request, 'sor.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def vandermonde(request):
    
    resultado = mensaje = datos = None

    if request.POST:

        x = request.POST['arrayx']
        y = request.POST['arrayy']

        try:
            x = funcion(x)
            y = funcion(y)

            resultado = Vandermonde.vandermonde(x,y)

            datos = {
                'arrx' : x,
                'arry' : y
            }
        
        except:

            mensaje = 'An error has occurred in the input.'


    return render(request, 'vandermonde.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def newton(request):
    resultado = mensaje = datos = None

    if request.POST:

        x = request.POST['arrayx']
        y = request.POST['arrayy']

        try:
            x = funcion(x)
            y = funcion(y)

            resultado = Newton.newton(x,y)

            datos = {
                'arrx' : x,
                'arry' : y
            }
        
        except:

            mensaje = 'An error has occurred in the input.'

    return render(request, 'newton.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def spline(request):
    resultado = mensaje = datos = None

    if request.POST:

        x = request.POST['arrayx']
        y = request.POST['arrayy']
        op = request.POST.get('opcion')

        op = int(op)

        try:
            x = funcion(x)
            y = funcion(y)

            if op == 12: #Lineal
                resultado = Spline.splineLineal(x,y)
            
            else: #Cubico
                resultado = Spline.splineCubica(x,y)
                
            datos = {
                'arrx' : x,
                'arry' : y,
                'op' : op
            }
        
        except:

            mensaje = 'An error has occurred in the input.'


    return render(request, 'spline.html', {'resultado': resultado, 'mensaje': mensaje, 'datos': datos})

def matriz(mtz):

    mtz = mtz.split(' ')

    arr = []
    arr2 = []

    i = 0
    while i < len(mtz):
        if mtz[i] == ';':
            arr.append(arr2)
            arr2 = []
            i += 1
            continue

        arr2.append(float(mtz[i]))
        i += 1

    arr.append(arr2)

    return arr

def matriz1(mtz):
    
    mtz = mtz.split(' ')

    arr = []

    i = 0
    while i < len(mtz):
        arr.append(float(mtz[i]))
        i += 2

    return arr

def size(mtz):
    try:
        subarray_sizes = [len(subarr) for subarr in mtz]
        return all(size == subarray_sizes[0] for size in subarray_sizes)
    except:
        return True
    
def funcion(func):
    func = func.split(',')

    arr = []

    i = 0
    while i < len(func):
        arr.append(float(func[i]))
        i += 1
    
    return arr

