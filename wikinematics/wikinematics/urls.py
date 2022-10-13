"""wikinematics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('intro/',views.intro,name='intro'),
    path('forces/',views.forces,name='forces'),
    path('gravity/',views.gravity,name='gravity'),
    path('forcemoments/',views.force_moments,name='forcemoments'),
    path('speed_basics/',views.speed_basics,name='speed_basics'),
    path('speed_rm/',views.speed_rm,name='speed_rm'),
    path('speed_cm/',views.speed_cm,name='speed_cm'),
    path('acceleration_basics/',views.acceleration_basics,name='acceleration_basics'),
    path('acceleration_rm/',views.acceleration_rm,name='acceleration_rm'),
    path('acceleration_cm/',views.acceleration_cm,name='acceleration_cm'),
    path('projectile/',views.projectile,name="projectile"),
    path('energy_basics',views.energy_basics,name='energy_basics'),
    path('energy_kinetic',views.energy_kinetic,name='energy_kinetic'),
    path('energy_potential',views.energy_potential,name='energy_potential'),
    path('energy_mechanical',views.energy_mechanical,name='energy_mechanical'),
    path('tuto',views.tuto,name="tuto"),
]
