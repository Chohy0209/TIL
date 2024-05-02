

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question',null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date=models.DateTimeField(null=True, blank=True)
    voter=models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject
class Answer(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer',null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
# 장고모델(질문,답변...)
#
# 마이그레이션(변경 작업 지시서)
# makemigrations : model에 적용한 변경내용을 바탕으로 새로운 migrations (변경사항 지시서) 를 만듬 즉,모델의 변경사항을 기록하는 역할 수행
# migrate : migrations(변경사항지시서)을 적용/적용해제, 해당마이그레이션 파일을 읽어서 DB에 반영/저장.
# DB