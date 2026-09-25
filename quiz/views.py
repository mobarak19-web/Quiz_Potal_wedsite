from django.shortcuts import render, redirect
# from django import HttpResponse
from .models import QuizModel, Question, Option, Participant, Attempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.db.models import Q



# Create your views here.

# Dashboard View ##########

def dashboard(request):
    quizzes = QuizModel.objects.all()
    return render(request, 'dashboard.html', {'quizzes': quizzes})


### Quiz Detail View ##########

def quiz_detail(request, quiz_id):
    quiz = QuizModel.objects.get(id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})

### Quiz Attempt View ##########

def quiz_attempt(request, quiz_id):
    quiz = QuizModel.objects.get(id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0

        for question in questions:
            selected_option_id = request.POST.get(str(question.id))

            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)

                if selected_option.is_correct:
                    score += 1

        participant, created = Participant.objects.get_or_create(
            user=request.user,
            defaults={
                'name': request.user.username,
                'student_class': 'Not Provided',
                'age': 0,
                'gender': 'Other',
                'institution': 'Not Provided',
            }
        )

        participant.score += score
        participant.save()
        
        
        ####change attempt ekoi user bar bar quiz answer korte parbe 
        
        previous_attempt = Attempt.objects.filter(
            participant=participant,
            quiz=quiz
        ).first()

        if previous_attempt:
           return redirect('quiz_results', quiz_id=quiz.id)
       
       #====================
        

        Attempt.objects.create(
            participant=participant,
            quiz=quiz,
            score=score,
            total=questions.count()
        )

        return redirect('quiz_results', quiz_id=quiz.id)

    return render(
        request,
        'quiz_attempt.html',
        {
            'quiz': quiz,
            'questions': questions
        }
    )




### Quiz Results View ##########

def quiz_results(request, quiz_id):
    quiz = QuizModel.objects.get(id=quiz_id)
    attempts = Attempt.objects.filter(quiz=quiz)
    return render(request, 'quiz_results.html', {'quiz': quiz, 'attempts': attempts})


#### User Authentication Views ##########

def user_logout(request):
    logout(request)
    return redirect('dashboard')



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})



def user_register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            # Create User
            user = form.save()

            # Create Participant
            Participant.objects.create(
                user=user,
                name=user.username,
                student_class=form.cleaned_data['student_class'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                institution=form.cleaned_data['institution']
            )

            # Login after registration
            login(request, user)

            return redirect('dashboard')

    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})





def cleanForm(request):
    if request.method == 'POST':
        form = cleanForm(request.POST)
        if form.is_valid():
            # Process the cleaned data
            return redirect('dashboard')
    else:
        form = cleanForm()
    
    return render(request, 'clean_form.html', {'form': form})




# def participant_list(request):
#     participants = Participant.objects.all()
#     return render(request, 'participant_list.html', {'participants': participants})




def participant_list(request):

    search = request.GET.get('search')

    if search:
        participants = Participant.objects.filter(
            Q(name__icontains=search) |
            Q(age__icontains=search) |
            Q(institution__icontains=search)
        )
    else:
        participants = Participant.objects.all()

    return render(
        request,
        'participant_list.html',
        {'participants': participants}
    )

### User Profile Views ##########




# #### participant search ########
# #===============================#
# def searchparticipant(reuest):
#     participant = []
#     if reuest.method == "GET":
#         search = reuest.GET.get('search')
#         if search:
#             if Participant.objects.filter(
#                 Q(name__icontains = search)|
#                 Q(age_icontains = search)|
#                 Q(institution__icontains = search)
                
#              ):
#                 participant = Participant.objects.filter(
#                 Q(name__icontains = search)|
#                 Q(age_icontains = search)|
#                 Q(institution__icontains = search))
#                 return render(request,'participantsearch.html',msg)
#             else:
#                 msg ={
#                     'error' : "NO participant found"
#                  }
#                 return render(request, 'participantsearch.html',msg)
#         else:
#             msg ={
#                'error' : "NO participant found"
#                  }
#             return render(request, 'participantsearch.html',msg) 
            
            
     
     # ######## participant search ########
# ====================================

def searchparticipant(request):
    participant = []

    if request.method == "GET":
        search = request.GET.get('search')

        if search:
            if Participant.objects.filter(
                Q(name__icontains=search) |
                Q(age__icontains=search) |
                Q(institution__icontains=search)
            ).exists():

                participant = Participant.objects.filter(
                    Q(name__icontains=search) |
                    Q(age__icontains=search) |
                    Q(institution__icontains=search)
                )

                msg = {
                    'participant': participant
                }

                return render(
                    request,
                    'participantsearch.html',
                    msg
                )

            else:
                msg = {
                    'error': 'NO participant found'
                }

                return render(
                    request,
                    'participantsearch.html',
                    msg
                )

        else:
            msg = {
                'error': 'NO participant found'
            }

            return render(
                request,
                'participantsearch.html',
                msg
            )                 