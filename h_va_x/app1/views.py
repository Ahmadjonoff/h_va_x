from django.shortcuts import render
from .models import *

def home(request):
    q_soz = request.GET.get('q_soz')
    try:
        correct = togri.objects.get(t_soz = q_soz)
        uncorrects = notogri.objects.filter(togrisi = correct)
    except:
        try:
            uncorrects = notogri.objects.get(n_soz=q_soz)
            correct = togri.objects.get(id = uncorrects.togrisi.id)
            uncorrects = notogri.objects.filter(togrisi=correct)
        except:
            correct = 'Bunday so`z bazamizda mavjud emas'
            uncorrects = ''

    return render(request, 'result.html', {'correct' : correct, 'uncorrect' : uncorrects})