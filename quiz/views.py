from django.shortcuts import render

quizzes = [
{
	"quiz_number":1,
	"name":"Äpplen",
	"description":"Vad kan du om äpplen?"
},

{
	"quiz_number":2,
	"name":"Elefanter",
	"description":"Elefantkunskap 1.0"
},
{
	"quiz_number":3,
	"name": "Internet",
	"description": "Kan du din internetkuriosa?"
},
{
	"quiz_number":4,
	"name": "Quizquiz",
	"description": "Det lilla meta-quizet"
},
]

# Create your views here.
def startpage(request):
	return render(request,"quiz/start.html")
def quiz(request):
	return render(request, "quiz/quiz.html")
def question(request):
	return render(request, "quiz/question.html")
def completed(request):
	return render (request, "quiz/results.html")
