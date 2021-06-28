"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

from django.contrib.auth import views as auth_views



from encuesta import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poll_views.inicio, name='inicio'), 
    path('home/<poll_id>', poll_views.home, name='home'), 
    path('sig/', poll_views.sig, name='sig'), 
    path('mejora/', poll_views.mejora, name='mejora'), 
    path('gracias/', poll_views.gracias, name='gracias'), 
    path('results/<poll_id>/', poll_views.results, name='results'),
    path('resultados/', login_required(poll_views.resultados), name='resultados'),
    path('accounts/login/', poll_views.loginPage, name='login'),
    path('logout/', poll_views.logoutUser, name='logout'),
    path('reporte/', poll_views.ReporteExcel, name='reporte'),
          

]