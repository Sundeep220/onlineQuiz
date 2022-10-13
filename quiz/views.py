from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE, HTTPResponse
import json
from telnetlib import LOGOUT
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    courses = Course.objects.all()
    context = {'courses' : courses}
    return render(request, 'home.html', context)

@login_required(login_url='/user/login')
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


@login_required(login_url='/user/login')
def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score': score}
    return render(request, 'score.html',context)


def take_quiz(request, id):
    context = {'id' : id}
    return render(request, 'quiz.html', context)


@login_required(login_url='/user/login')
@csrf_exempt
def check_score(request):
    data = json.loads(request.body)
    course_id = data.get('course_id')
    user = request.user
    solutions = json.loads(data.get('data'))
    course = Course.objects.get(id=course_id)
    score = 0
    
    for solution in solutions:
        question = Question.objects.filter(id=solution.get('question_id')).first()
        if question.answer == solution.get('option'):
            score = score +  question.marks
    score_board = ScoreBoard(course=course,user=user,score=score)
    score_board.save()
    return JsonResponse({'message': 'success' , 'status': True})

@login_required(login_url='/user/login')
@csrf_exempt
def leaderboard(request):
    # user = request.user
    # score = ScoreBoard.objects.filter(user=user)
    # print(score)
    return render(request, 'leaderboard.html')
