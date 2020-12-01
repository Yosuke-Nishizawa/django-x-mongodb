from polls.models import Choice, Question

# Question取得
q = Question.objects.get(id=1)
print(f'Question id=1 : {q}')
# Choiceデータ設定
q.choice_set.create(choice_text='選択肢1', votes=0)
q.choice_set.create(choice_text='選択肢2', votes=1)
q.choice_set.create(choice_text='選択肢3', votes=2)
# 確認
for c in q.choice_set.all():
    print(c)
