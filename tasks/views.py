from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Tasks
from .forms import CreateTaskForm

# Create your views here.
class ListTask(ListView):
    model = Tasks
    template_name = 'tasks/listtask.html'
    context_object_name = 'tasks'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tasks'] = self.object_list
    #     return context

class CreateTask(CreateView):
    model = Tasks
    form_class = CreateTaskForm 
    template_name = 'tasks/createtask.html'
    success_url = "/"
    print(form_class)

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)