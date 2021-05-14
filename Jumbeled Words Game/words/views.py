from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random


word = [
    "database",
    "function",
    "data",
    "integers",
    "string",
    "django",
    "flask",
]

def rword():
    global jword,ranword
    ranword = random.choice(word)
    jumbel = random.sample(ranword, len(ranword))
    jword = "".join(jumbel)

msg = ""

def homepage(request):
    rword()
    global jword,msg
    return render(request, 'index.html', {'jum_word': jword , 'msg':msg})

def checkans(request):
    global ranword,msg,jword
    user_answer = request.GET['answer']
    if user_answer == ranword:
        msg = "That was a correct answer."
        homepage(request)
    else:
        msg = "Sorry! Wrong answer"
    return render(request, 'index.html', {'jum_word': jword , 'msg':msg})