from django.shortcuts import  render, get_object_or_404,redirect
from .models import Question
from django.utils import timezone

def detail(request, question_id):
    #question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    context={'question': question}
    return render(request, 'pybo/question_detail.html', context)

def index(request):
    question_list=Question.objects.order_by("-create_date") #-:내림차순
    context={'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

    #return render(request , 템플릿 , 질문리스트->딕셔너리 구조)
#render함수 : 질문리스트(python구조)에 템플릿(html 형식)을 적용해서 html문서로 변환하는 함수
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")