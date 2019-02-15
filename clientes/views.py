from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm 
from django.shortcuts import redirect

def cliente_list(request):
    return render(request, 'clientes/teste.html')

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/')
    else:
        form = ClienteForm()
    return render(request,'clientes/cliente_edit.html',{'form':form})
