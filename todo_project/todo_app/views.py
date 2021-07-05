from django.shortcuts import render,redirect
from .models import Task
from .forms import ModelForm
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvtask')
        # return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url=reverse_lazy('cbvtask')



# def task_view(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         date=request.POST.get('date')
#         obj1=Task(name=name,priority=priority,date=date)
#         obj.save();
#     return render(request,'task_view.html',{'obj1':obj})
# def delete(request,taskid):
#     task=Task.objects.get(id=taskid)
#     if request.method=='POST':
#         task.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'task':task})
# def update(request,id):
#     obj=Task.objects.get(id=id)
#     form=ModelForm(request.POST or None,instance=obj)
#     if form.is_valid():
#         form.save();
#         return redirect('/')
#     return render(request,'edit.html',{'form':form,'obj':obj})