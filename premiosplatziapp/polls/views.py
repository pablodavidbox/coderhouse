from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
"""
def index(request):
    latest_question_list = Question.objects.all()
    return render(request,"polls/index.html", {
        "latest_question_list": latest_question_list
    })

def detail(request,question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request,"polls/detail.html",{
        "question": question
    })

def result(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/result.html",{
        "question": question
    })
"""

class IndexView(generic.ListView):
        template_name = "polls/index.html"
        context_object_name = "latest_question_list"

        """
        def get_queryset(self):
            queryset = super(Question, self).get_queryset()
            queryset = queryset # TODO
            return queryset"""
        
        def get_queryset(self):
            return Question.objects.order_by("-pub_date")[:5]
        

class DetailView(generic.DetailView):
    model =  Question
    template_name = "polls/detail.html"
        

class ResultView(generic.DetailView):
    model =  Question
    template_name = "polls/result.html"


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk= request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{
                     "question":question,
                     "error_message":"No elegiste un respuesta"
        })
    else:
         selected_choice.votes += 1
         selected_choice.save()
         return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
    
