from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE, HTTPResponse
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth.models import User


def home(request):
    courses = Course.objects.all()
    context = {'courses' : courses}
    return render(request, 'home.html', context)

def get_quiz(request, id):
    raw_questions = Question.objects.filter(course=id)
    questions = []

    for raw_question in raw_questions:
        question = {}
        question['id'] = raw_question.id
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        question['marks'] = raw_question.marks
        options=[]
        options.append(raw_question.option1)
        options.append(raw_question.option2)
        options.append(raw_question.option3)
        options.append(raw_question.option4)

        question['options'] = options

        questions.append(question)

    return JsonResponse(questions, safe=False)

def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score': score}
    return render(request, 'score.html',context)

def take_quiz(request, id):
    context = {'id' : id}
    return render(request, 'quiz.html', context)