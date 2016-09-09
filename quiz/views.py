from django.shortcuts import render

from quiz.models import Quiz 
	

# Create your views here.
def startpage(request):
	context = {
		"quizzes":Quiz.objects.all(),
	}
	return render(request,"quiz/start.html", context)

def quiz(request, quiz_number):
	context ={
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
	"question_number": question_number,
	"question": "Vilken av följande äppelsorter är röda?",
	"answer1":"Granny Smith",
	"answer2":"Ingrid Marie",
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




