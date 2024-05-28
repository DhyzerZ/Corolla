"""corolla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views as applicationViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', applicationViews.home),
    path('bisection/', applicationViews.bisection),
    path('false-position/', applicationViews.false_position),
    path('fixed-point/', applicationViews.fixed_point),
    path('gauss-seidel/', applicationViews.gauss_seidel),
    path('jacobi/', applicationViews.jacobi),
    path('multiple-roots/', applicationViews.multiple_roots),
    path('newton-raphson/', applicationViews.newton_raphson),
    path('secant/', applicationViews.secant),
    path('sor/', applicationViews.sor),
    path('newton/', applicationViews.newton),
    path('spline/', applicationViews.spline),
    path('vandermonde/', applicationViews.vandermonde),
    path('incremental-search/',applicationViews.incremental_search),
    path('gaussian-elimination/',applicationViews.gaussian_elimination),
    path('gaussian-elimination-with-pivoting/',applicationViews.gaussian_elimination_with_pivoting),
    path('gaussian-elimination-with-total-pivoting/',applicationViews.gaussian_elimination_with_total_pivoting),
    path('lu-factorization/',applicationViews.lu_factorization),
    path('crout-factorization/',applicationViews.crout_factorization),
    path('cholesky-factorization/',applicationViews.cholesky_factorization),
    path('doolittle-factorization/',applicationViews.doolittle_factorization),

]
