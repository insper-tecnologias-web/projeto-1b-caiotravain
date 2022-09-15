from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        novo = Note(title=title, content=content)
        if modo == "1":
            novo.save()
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
    return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        novo = Note(title=title, content=content)
        if modo == "D":
            instance = Note.objects.get(id=id)
            instance.delete()
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
    return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        novo = Note(title=title, content=content)
        if modo == "U":
            instance = Note.objects.get(id=id)
        return render(request, 'notes/update.html', {"note":instance})
    else:
        all_notes = Note.objects.all()
        print(all_notes)
    
def atualiza(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        if modo == "A":
            Note.objects.filter(id = id).update(title=title, content=content)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
    return render(request, 'notes/index.html', {'notes': all_notes})
