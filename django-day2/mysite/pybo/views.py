from django.shortcuts import  render, get_object_or_404,redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.http import HttpResponseNotAllowed
def detail(request, question_id):
    #question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def index(request):
    #요청 페이지가 있다면 페이지 번호를 저장하고, 요청 페이가 없다면 1을 저장
    page = request.GET.get('page', 1) #기본 요청 페이지 : 1
    question_list = Question.objects.order_by('-create_date')
    paginator=Paginator(question_list, 10) #페이지당 10개
    page_obj=paginator.get_page(page) #요청 페이지(page)의 내용을 가져와서 page_obj에 저장
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def question_create(request):
    if request.method == "POST": #post 방식 ->질문작성 후 -> 저장하기 -> 저장
        form = QuestionForm(request.POST)
        if form.is_valid(): #폼에 값이 올바르게 저장되었다면
            question = form.save(commit=False) #임시저장
            question.author=request.user #author 속성에 로그인 계정 저장
            question.create_date=timezone.now() #작성일자 저장
            question.save() #실제 저장
            return redirect('pybo:index')

    else: #get방식(초기화면에서 '질문등록하기' 눌렀을때) -> 질문폼
        form = QuestionForm()
    return render(request,'pybo/question_form.html',{'form':form})


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


    #return render(request , 템플릿 , 질문리스트->딕셔너리 구조)
#render함수 : 질문리스트(python구조)에 템플릿(html 형식)을 적용해서 html문서로 변환하는 함수
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")