from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

# view는 클라이언트로 부터 request를 받게되면, 다시 response를 해준다.
# request에는 여러가지 정보들이 담겨있다.

def index(request):
    # 1
    # return HttpResponse("Hello, world. You're at the polls index.")  # index view가 호출되면 클라이언트에게 "Hello, wold-"라는 respose를 반환해준다

    # 2. 뷰에 기능넣기
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]  # Question 데이터 중 출판일자(pub-date)를 정렬하여 5개까지 가져오고,
    # output = ', '.join([q.question_text for q in latest_question_list])  # (,)로 연결하여 str으로 반환해준다
    # return HttpResponse(output)

    # 3. 템플릿 분리하기
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')  # polls/index.html 템플릿을 불러온다
    # context = {
    #     'latest_question_list': latest_question_list,  # context를 통해 데이터를 전달한다
    # }
    # return HttpResponse(template.render(context, request))

    # 4. render() shortcuts 사용하기
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 1 
    # return HttpResponse("You're looking at question %s." % question_id)

    # 2. 404 에러 만들기
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")  # 없는 데이터를 조회하면 예외메세지를 반환해준다
    # return render(request, 'polls/detail.html', {'question': question})

    # 3. get_object_or_404 shortcuts 사용하기
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # 1
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # 2. 사용자로 부터 데이터를 받아와 결과페이지 만들기
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):  # 뷰를 호출할때 question_id를 넘겨받는다
    # 1
    # return HttpResponse("You're voting on question %s." % question_id)

    # 2. form 만들기
    question = get_object_or_404(Question, pk=question_id)  # question_id를 넘겨받아 question데이터를 조회한다
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # question에 대해 외래키를 갖는 choice를 가져오는데 이때 choice 중 pk값이 템플릿에서 넘겨받은 값을 조회한다
    except (KeyError, Choice.DoesNotExist):  # 조회했을 때 데이터가 없으면 예외가 발생
        return render(request, 'polls/detail.html', {  # 예외가 발생했을때 다시 detail(상세페이지)로 response를 해준다
            'question': question,  # context 데이터로 question과 error_message를 보내준다
            'error_message': "You didn't select a choice.",
        })
    else:  # 조회했을 때 데이터가 있으면
        selected_choice.votes += 1  # choice를 1 올려주고
        selected_choice.save()  # 저장

        # POST 데이터로 뷰가 호출된 경우에는 HttpResponseRedirect로 반환해준다
        # 이유는 데이터가 두번 게시되는 것을 방지할 수 있기 때문이다
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # reverse()함수를 통해 results 뷰를 호출한다