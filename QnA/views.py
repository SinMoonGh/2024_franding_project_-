from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FAQ
from django.contrib.auth.models import User

# Create your views here.

def question_list(request, item_id):
    # questions = Question.objects.filter(item_id=item_id)
    questions = Question.objects.all().order_by('-created_at')  # 모든 질문을 가져옵니다.
    return render(request, 'QnA/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'GET':
        form = AnswerForm(request.GET)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('QnA:question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'QnA/question_detail.html', {'question': question, 'form': form})

def question_create(request, item_id):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user_id_id= request.user.id
            question.item_id.id = item_id
            question.save()            
            return redirect(reverse('QnA:question_list', args=[item_id]))
            # return redirect(reverse('QnA:question_list'))
            
    else:
        form = QuestionForm(initial={'item_id': item_id})
    return render(request, 'QnA/question_form.html', {'form': form})


def home(request):
    questions = Question.objects.filter(user_id=request.user).order_by('-created_at')  # 모든 질문을 가져옵니다.
    return render(request, 'QnA/home.html', {'questions': questions})
