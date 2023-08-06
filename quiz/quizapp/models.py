from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(self):
        return self.cname
class Question(models.Model):
    question=models.CharField(max_length=100)

    def __str__(self):
        return self.question
    
choose=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
]

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=10,choices=choose)
    marks=models.IntegerField(default=10)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
    
class Attemtnumber(models.Model):
    marks=models.IntegerField()
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    noattempt=models.IntegerField(editable=False)
    totalattemptquestion=models.IntegerField(blank=True,null=True)
    toatalquestion=models.IntegerField(blank=True,null=True)
    category=models.CharField(max_length=20,null=True,blank=True)
    


    