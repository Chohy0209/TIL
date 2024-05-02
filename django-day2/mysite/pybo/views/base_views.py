from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Question


def detail(request, question_id):
    #question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def index(request):
    #요청 페이지가 있다면 페이지 번호를 저장하고, 요청 페이가 없다면 1을 저장
    page = request.GET.get('page', 1) #기본 요청 페이지 : 1
    question_list = Question.objects.order_by('-create_date')
    kw = request.GET.get('kw', '')  # 검색어
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator=Paginator(question_list, 10) #페이지당 10개
    page_obj=paginator.get_page(page) #요청 페이지(page)의 내용을 가져와서 page_obj에 저장
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

    #return render(request , 템플릿 , 질문리스트->딕셔너리 구조)
#render함수 : 질문리스트(python구조)에 템플릿(html 형식)을 적용해서 html문서로 변환하는 함수
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")