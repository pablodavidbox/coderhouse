from secrets import choice
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
           question_text = models.CharField(max_length=255)
           pub_date = models.DateField(auto_now_add=True)

           def __str__(self):
                   return self.question_text

           def was_published_recently(self):
                   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)         

class Choice(models.Model):
           question =models.ForeignKey(Question, on_delete=models.CASCADE)
           choice_text = models.CharField(max_length=255)
           votes = models.IntegerField(default=0)

           def __str__(self):
                   return self.choice_text