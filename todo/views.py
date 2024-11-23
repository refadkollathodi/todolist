from django.shortcuts import render,redirect
from todo.models import todo
from todo.forms import TodoForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404


def todolist(request):
    task=todo.objects.all()
    form=TodoForm()
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
          form.save()
        return  redirect('/')

    context={
        "task":task,
        "form":form,
    }
    return render(request,'todo_app.html',context=context)

def updateTask(request,pk):
    task=get_object_or_404(todo,id=pk)
    form=TodoForm(instance=task)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'update_task.html',context=context)


def deleteTask(request,pk):
    task=get_object_or_404(todo,id=pk)
    if request.method=='POST':
            task.delete()
            return redirect('/')
    context={
        'task':task
    }
    return render(request,'delete.html',context=context)




def checklist(request, pk):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('tasks')
        task=todo.objects.filter(id__in=selected_ids)
        if selected_ids:
            task.delete()
    return redirect('/', pk=pk)
