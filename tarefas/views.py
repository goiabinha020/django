from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 


class NovaTarefa(forms.Form):
    task = forms.CharField(label= "Nova tarefa")
    priority = forms.IntegerField(label="Prioridade", min_value=1, max_value=5 )

# Create your views here.
def index(request):
    if "tarefas" not in request.session:
        request.session["tarefas"] = []
    return render(request, "tarefas/index.html", {"tarefas" : request.session["tarefas"], })

def add(request):
    if request.method == "POST":
        form = NovaTarefa(request.POST) #todos os dados do post do formulário vai para essa var
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tarefas"] += [task]
            return HttpResponseRedirect(reverse("tarefas:index"))
        else:
            return render(request, "tarefas/add.html", {"form" : form})
    else:
        return render(request, "tarefas/add.html",{"form" : NovaTarefa})
