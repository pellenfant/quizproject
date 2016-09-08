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
	context = {
		"quizzes":quizzes,
	}
	return render(request,"quiz/start.html", context)

def quiz(request, quiz_number):
	context ={
		"quiz": quizzes[int(quiz_number)-1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
	"question_number": question_number,
	"question": "Vilken av följande äppelsorter är röda?",
	"answer1":"Granny Smith",
	"answer2":"Royal Gala",
	"answer3":"Transparante Blanche",
	"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)


def completed(request, quiz_number):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number,
	}
	return render (request, "quiz/results.html", context)




