# imports
from django.shortcuts import render, redirect
from .forms import TarefaForm
from django.contrib import messages
from django.utils.timezone import datetime
from .models import Tarefa
#begin

def new_tarefa(request):
    if request.method == "POST":
        import pdb;pdb.set_trace()
        form = TarefaForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            # algumas modificações futuras
            post.save()
            messages.success(request,'Compromisso marcado com sucesso.')
            return redirect('cliente_list')
    else:
        form = TarefaForm()

    return render(request, 'calendario/new_tarefa.html', {'form': form})

def today_task(request):
    tarefas = Tarefa.objects.filter(data_tarefa__date=datetime.now().date())
    return render(request, 'calendario/tarefas_hoje.html', {'tarefas': tarefas})
