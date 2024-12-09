from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Area, Ala, Punto, RegAvance
from .forms import RegAvanceForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('registrar_avance')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    else:
        return render(request, 'login.html')

@login_required
def registrar_avance(request):
    user = request.user
    ala = user.ala
    area = ala.id_aaa if ala else None
    puntos = Punto.objects.filter(id_ala=ala) if ala else []

    if request.method == 'POST':
        form = RegAvanceForm(request.POST)
        if form.is_valid():
            reg_avance=form.save()

            #Actualizar el punto correspondiente

            punto=reg_avance.id_punto
            punto.avance_km=reg_avance.avance_km
            punto.avance_vol=reg_avance.avance_vol
            punto.estado=reg_avance.estado
            punto.save()


            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False, 'errors': form.errors})
    else:
        form = RegAvanceForm()

    context = {
        'form': form,
        'area': area,
        'ala': ala,
        'puntos': puntos,
    }
    return render(request, 'registrar_avance.html', context)

'''
def registrar_avance(request):
    if request.method == 'POST':
        form = RegAvanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegAvanceForm()
    areas = Area.objects.all()
    return render(request, 'registrar_avance.html', {'form': form, 'areas': areas})
'''


def load_alas(request):
    id_aaa = request.GET.get('id_aaa')
    alas = Ala.objects.filter(id_aaa_id=id_aaa).all()
    return JsonResponse(list(alas.values('id', 'ala')), safe=False)

def load_puntos(request):
    id_ala = request.GET.get('id_ala')
    puntos = Punto.objects.filter(id_ala_id=id_ala).all()
    return JsonResponse(list(puntos.values('id', 'cod')), safe=False)

def success(request):
    return render(request, 'success.html')


@login_required
def registrar_avance2(request):
    punto_id = request.GET.get('punto_id')
    punto = Punto.objects.get(id=punto_id)
    if request.method == 'POST':
        form = RegAvanceForm(request.POST)
        if form.is_valid():
            avance = form.save(commit=False)
            avance.punto = punto
            avance.save()
            return redirect('success')
    else:
        form = RegAvanceForm()
    return render(request, 'registro_avance_modal.html', {'form': form})
