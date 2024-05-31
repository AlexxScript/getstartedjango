from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Choice, Question
from django.template import loader
from django.db.models import F
from django.views import generic
from django.contrib.auth.decorators import login_required


class IndexView (generic.ListView):
    template_name = "myapp/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        user = self.request.user
        print(user.id)
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    context_object_name = "question" 
    template_name = "myapp/detail.html"

class ResultView(generic.DetailView):
    context_object_name = "question" 
    template_name = "myapp/results.html"
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'myapp/detail.html',
            {
                "question":question,
                "error_message":"you didn't select a choice"
            })
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("myapp:results", args=(question.id,)))

# def index (request):
#     latests_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list":latests_question_list,
#     }
#     return render(request,"myapp/index.html",context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,"myapp/detail.html",{"question":question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,"myapp/results.html",{"question":question})

