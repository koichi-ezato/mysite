from django.db import models
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='質問')
    pub_date = models.DateField(verbose_name='日付')

    def get_absolute_url(self):
        return reverse('polls:update', kwargs={'pk': self.pk})


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='選択肢')
    votes = models.IntegerField(default=0, verbose_name='投票数')
