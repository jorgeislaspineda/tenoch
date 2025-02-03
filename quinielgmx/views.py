from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Jornada, Partido, Prediccion, UsuarioQuiniela
from .forms import PrediccionForm

@login_required
def listar_jornadas(request):
    jornadas = Jornada.objects.all()
    return render(request, 'quinielgmx/listar_jornadas.html', {'jornadas': jornadas})

@login_required
def ver_partidos_jornada(request, jornada_id):
    jornada = get_object_or_404(Jornada, id=jornada_id)
    partidos = jornada.partidos.all()
    return render(request, 'quinielgmx/ver_partidos_jornada.html', {'jornada': jornada, 'partidos': partidos})

@login_required
def realizar_prediccion(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            prediccion, created = Prediccion.objects.update_or_create(
                usuario=request.user,
                partido=partido,
                defaults={
                    'goles_local_pred': form.cleaned_data['goles_local_pred'],
                    'goles_visitante_pred': form.cleaned_data['goles_visitante_pred']
                }
            )
            return redirect('ver_partidos_jornada', jornada_id=partido.jornada.id)
    else:
        form = PrediccionForm()
    return render(request, 'quinielgmx/realizar_prediccion.html', {'form': form, 'partido': partido})

@login_required
def ver_ganadores_jornada(request, jornada_id):
    jornada = get_object_or_404(Jornada, id=jornada_id)
    # Lógica para calcular ganadores (puedes implementarla según tus reglas)
    return render(request, 'quinielgmx/ver_ganadores_jornada.html', {'jornada': jornada})