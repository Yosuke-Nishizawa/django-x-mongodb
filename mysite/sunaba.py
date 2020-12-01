from polls.models import Question
from django.utils import timezone
# Questionにデータ設定
q1 = Question(question_text='質問1', pub_date=timezone.now())
q1.save()
q2 = Question(question_text='質問2', pub_date=timezone.now())
q2.save()
q3 = Question(question_text='質問3', pub_date=timezone.now())
q3.save()
# Questionの内容確認
for q in Question.objects.all():
   print(q)