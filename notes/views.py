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
        
        all_tags = Tag.objects.all()
        tag3 = (all_tags.filter(Tag=tag))
        
        if len(tag3) != 0 :
            tem = True 
            tag2 = tag3[0]               
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
        all_tags = Tag.objects.all()
        
        all_notes = Note.objects.all()
        for a in all_tags:
            a.delete()

        for b in all_notes:
            b.delete()
    return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        tag = request.POST.get('tag')
        novo = Note(title=title, content=content)
        all_tags = Tag.objects.all()
        T = all_tags.filter(Tag=tag)
        
        if modo == "D":
            instance = Note.objects.get(id=id)
            instance.delete()
            
            if len(T) == 1 :
                t = T[0]
                lista = t.note_set.all()
                if len(lista)<1:
                    t.delete()
                
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        tag = request.POST.get('tag')
        novo = Note(title=title, content=content)
        all_tags = Tag.objects.all()
        
        tag3 = (all_tags.filter(Tag=tag))
        
        if len(tag3) != 0 :
            tag2 = tag3[0]  
        
        if modo == "U":
            instance = Note.objects.get(id=id)
        return render(request, 'notes/update.html', {"note":instance})
    else:
        all_notes = Note.objects.all()
        #print(all_notes)
    
def atualiza(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        modo = request.POST.get('modo')
        tag = request.POST.get('tag')
        antigo = request.POST.get("antigo")
        all_tags = Tag.objects.all()
        tem = False
        tag3 = (all_tags.filter(Tag=tag))
        tag4 = (all_tags.filter(Tag=antigo))
        
        apaga = False
        if len(tag4) >= 1 :
            tag5 = tag4[0] 
            lista = tag5.note_set.all()
        if len(lista) == 1:
             
            apaga= True

        
        if len(tag3) != 0 :
            tem = True 
            tag2 = tag3[0]               
        
        if modo == "A":
            if not tem:
                
                if tag =="":
                    tag2 = Tag(Tag= tag)
                    tag2.save()
                    Note.objects.filter(id = id).update(title=title, content=content,tag = tag2)
                                  
                else:
                    tag2 = Tag(Tag= tag)
                    tag2.save()
                    Note.objects.filter(id = id).update(title=title, content=content, tag = tag2)
                     

            else:
                Note.objects.filter(id = id).update(title=title, content=content, tag = tag2)
        if apaga:
            tag5.delete() 
                
        return redirect('index')
    else:
        all_notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': all_notes})

def tags(request):
    all_notes = Note.objects.all()
    if len(all_notes) != 0:
        lista = []
        lista = Tag.objects.distinct().exclude(Tag__isnull=True).exclude(Tag__exact='')

    return render(request, 'notes/tag.html', {'tags': lista})

def unica(request):
    if request.method == 'POST':
        tag = request.POST.get("tag")
        listas_tags= [tag]
        lista = []
        all_tags = Tag.objects.all()
        tag3 = (all_tags.filter(Tag=tag))
        tag2 = tag3[0]
        
        lista = tag2.note_set.all()
        
        return render(request, 'notes/unica.html', {'notes': lista , 'tags' : listas_tags})
    else:
        all_notes = Note.objects.all()
        
    return redirect('index')