from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def manifesto(request):
    return render(request, 'manifesto.html')

from .models import Storia

def diario(request):
    storie = Storia.objects.order_by('-data_creazione')
    return render(request, 'diario.html', {'storie': storie})

def contatto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        messaggio = request.POST.get("messaggio")
        print(f"📨 Messaggio ricevuto da {nome}: {messaggio}")
        # Qui in futuro puoi salvare o inviare il messaggio via email
        return render(request, 'contatto.html', {"conferma": True})
    return render(request, 'contatto.html')
