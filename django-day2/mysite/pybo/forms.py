from django import  forms
from pybo.models import Question
#장고 웹프레임웍에서는 일반폼과 모델폼(ex.Question 모델과 작성한 데이터를 연결하여 저장)을 제공한다
#모델폼을 이용하여 질문 모델과 질문 작성글을 연결하여 db에 저장

class QuestionForm(forms.ModelForm):#모델폼
    class Meta:
        model=Question
        fields=['subject','content'] #QuestionForm 모델폼에서 사용할 Question속성
