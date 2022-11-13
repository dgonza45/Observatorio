"""FRONT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from obsfront import views as pagina

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina.index),
    path('index.html', pagina.index),
    path('donaciones.html', pagina.donaciones),
   
    path('vih.html', pagina.vih),
    path('mapa_vih.html', pagina.mapa_vih),
    path('mapa_sexo_vih.html', pagina.mapa_sexo_vih),
    path('mapa_edad_vih.html', pagina.mapa_edad_vih),
    
    path('parotiditis.html', pagina.parotiditis),
    path('mapa_parotiditis.html', pagina.mapa_parotiditis),
    path('mapa_sexo_parotiditis.html', pagina.mapa_sexo_parotiditis),
    path('mapa_edad_parotiditis.html', pagina.mapa_edad_parotiditis),
    
    path('hepatitisa.html', pagina.hepatitisa),
    path('mapa_hepatitisa.html', pagina.mapa_hepatitisa),
    path('mapa_sexo_hepatitisa.html', pagina.mapa_sexo_hepatitisa),
    path('mapa_edad_hepatitisa.html', pagina.mapa_edad_hepatitisa),
   
    path('hepatitisc.html', pagina.hepatitisc),
    path('mapa_hepatitisc.html', pagina.mapa_hepatitisc),
    path('mapa_sexo_hepatitisc.html', pagina.mapa_sexo_hepatitisc),
    path('mapa_edad_hepatitisc.html', pagina.mapa_edad_hepatitisc),
   
    path('dengue.html', pagina.dengue),
    path('mapa_dengue.html', pagina.mapa_dengue),
    path('mapa_sexo_dengue.html', pagina.mapa_sexo_dengue),
    path('mapa_edad_dengue.html', pagina.mapa_edad_dengue),
   
    path('intentoSuicidio.html', pagina.intentoSuicidio),
    path('mapa_intentoSuicidio.html', pagina.mapa_intentoSuicidio),
    path('mapa_sexo_intentoSuicidio.html', pagina.mapa_sexo_intentoSuicidio),
    path('mapa_edad_intentoSuicidio.html', pagina.mapa_edad_intentoSuicidio),
   
    path('cancerDeMama.html', pagina.cancerDeMama),
    path('mapa_cancerDeMama.html', pagina.mapa_cancerDeMama),
    path('mapa_sexo_cancerDeMama.html', pagina.mapa_sexo_cancerDeMama),
    path('mapa_edad_cancerDeMama.html', pagina.mapa_edad_cancerDeMama),
]
