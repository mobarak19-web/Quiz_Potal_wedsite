from django.contrib import admin

# Register your models here.


from .models import QuizModel, Question, Option, Participant, Attempt

admin.site.register(QuizModel)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Participant)
admin.site.register(Attempt)

class QuizModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question')
    search_fields = ('quiz__title', 'question')
   
    
class OptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option', 'is_correct')
    search_fields = ('question__question', 'option')
    
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'age', 'gender', 'institution', 'score')
    search_fields = ('name', 'student_class', 'age', 'gender', 'institution')

class AttemptAdmin(admin.ModelAdmin):
    list_display = ('participant', 'quiz', 'score')
    search_fields = ('participant__name', 'quiz__title', 'score')