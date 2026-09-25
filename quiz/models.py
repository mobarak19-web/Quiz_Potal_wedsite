from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuizModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    
    
    def __str__(self):
        return f"{self.quiz.title} => Question: {self.question}"
    
    
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name =  'options')
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.question.quiz.title} => Question: {self.question.question} => Option: {self.option}"
    
    
class Participant(models.Model):
    GENDER_CHOICES = [
                 ('Male', 'Male'),
                 ('Female', 'Female'),
                 ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    
    name = models.CharField(max_length=255)
    score = models.IntegerField(default=0)
    student_class = models.CharField(max_length=555)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    
    institution = models.CharField(max_length=255)
    
    def __str__(self):
        return (self.name)
    
    
    
class Attempt(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)

    score = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    submitted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('participant', 'quiz')

    def __str__(self):
        return f"{self.participant.name} - {self.quiz.title}"
        
        
        



