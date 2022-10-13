from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',)
def intro(request):
    return render(request,'intro.html')
def forces(request):
    return render(request,'forces.html')
def gravity(request):
    return render(request,'gravity.html')
def force_moments(request):
    return render(request,'forcemoments.html')
def speed_basics(request):
    return render(request,'speed_basics.html')
def speed_rm(request):
    return render(request,'speed_rm.html')
def speed_cm(request):
    return render(request,'speed_cm.html')
def acceleration_basics(request):
    return render(request,'acceleration_basics.html')
def acceleration_rm(request):
    return render(request,'acceleration_rm.html')
def acceleration_cm(request):
    return render(request,'acceleration_cm.html')
def projectile(request):
    return render(request,'projectile.html')
def energy_basics(request):
    return render(request,'energy_basics.html')
def energy_kinetic(request):
    return render(request,'energy_kinetic.html')
def energy_potential(request):
    return render(request,'energy_potential.html')
def energy_mechanical(request):
    return render(request,'energy_mechanical.html')
def tuto(request):
    return render(request,'tuto.html')
