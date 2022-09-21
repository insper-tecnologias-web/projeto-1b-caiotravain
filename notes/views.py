from re import T
from django.shortcuts import render, redirect
from .models import Note, Tag

def index(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        tag = request.POST.get("tag")
        all_tags = Tag.objects.all()
        tem = False
        
        for t in all_tags:
            if tag == str(t):
                tag2 = t
                tem = True
                
                break
            else:
                ''                  
        if not tem:      
            tag2 = Tag(Tag= tag)
            tag2.save()
        novo = Note(title=title, content=content, tag = tag2)
        
       
        if modo == "1":
            novo.save()
        tag2.note_set.add(novo)    
        
        return redirect('index')
    else:
        
        all_notes = Note.objects.all()
       
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
        tag = request.POST.get('tag')
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
        tag = request.POST.get('tag')
        all_tags = Tag.objects.all()
        tem = False
        for t in all_tags:
            if tag == str(t):
                tag2 = t
                tem = True
                
                break
            else:
                ''     
        
        if modo == "A":
            if not tem:
                if tag =="":
                    Note.objects.filter(id = id).update(title=title, content=content)
                else:
                    tag2 = Tag(Tag= tag)
                    tag2.save()
                    Note.objects.filter(id = id).update(title=title, content=content, tag = tag2)

            else:
                Note.objects.filter(id = id).update(title=title, content=content, tag = tag2)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})

def tags(request):
    all_notes = Note.objects.all()
    if len(all_notes) != 0:
        lista = []
        ant = all_notes[0]
        nomes = []
        lista.append(ant)
        nomes.append((ant.tag))
        
        for n in all_notes:
            if n.tag in nomes:
                ''
            else:
                if str(n.tag) != '':
                    nomes.append((n.tag))
                    lista.append(n)
                ant = n
    else:
        lista = []
    return render(request, 'notes/tag.html', {'notes': lista})

def unica(request):
    if request.method == 'POST':
        tag = request.POST.get("tag")
        listas_tags= [tag]
        lista = []
        all_tags = Tag.objects.all()
        for t in all_tags:
            if str(t)== tag:
                tag2 = t
                break
        
        lista = tag2.note_set.all()
        
        return render(request, 'notes/unica.html', {'notes': lista , 'tags' : listas_tags})
    else:
        all_notes = Note.objects.all()
        
    return redirect('index')