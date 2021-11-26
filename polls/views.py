from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.
def index(request):
    # 1
    # return HttpResponse("Hello, world. You're at the polls index.")  # index view가 호출되면 클라이언트에게 "Hello, wold-"라는 respose를 반환해준다

    # 2
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Question 데이터 중 출판일자(pub-date)를 정렬하여 5개까지 가져오고,
    # output = ', '.join([q.question_text for q in latest_question_list])  # (,)로 연결하여 str으로 반환해준다
    # return HttpResponse(output)

    # 3
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')  # polls/index.html 템플릿을 불러온다
    # context = {
    #     'latest_question_list': latest_question_list,  # context를 통해 데이터를 전달한다
    # }
    # return HttpResponse(template.render(context, request))

    # 4
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # (1) 
    # return HttpResponse("You're looking at question %s." % question_id)

    # (2) 404 에러 만들기
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")  # 없는 데이터를 조회하면 예외메세지를 반환해준다
    # return render(request, 'polls/detail.html', {'question': question})

    # (3) get_object_or_404 단축기능 사용하기
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# view는 클라이언트로 부터 request를 받게되면, 다시 response를 해준다.
# request에는 여러가지 정보들이 담겨있다.