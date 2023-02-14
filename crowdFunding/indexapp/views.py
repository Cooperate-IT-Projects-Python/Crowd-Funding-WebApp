from django.shortcuts import render
from projectsapp.models import Project, ProjectRating
from users.models import CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.
def index(r):
    # Get New Projects
    projects = Project.objects.all().order_by('-id')[:5]
    # userid = r.session['userId']
    userid = 3
    for project in projects:
        try:
            rating = ProjectRating.objects.get(ProjectId=project, owner_id=userid)
            projects.user_rating = rating.rating if rating else 0
        except:
            projects.user_rating = 0
    return render(r, "index.html", {'projects': projects})


def rate(r, project_id: int, rating: int):
    # userid = r.session['userId']
    userid = 3
    project = Project.objects.get(id=project_id)
    user = CustomUser.objects.get(id=userid)
    ProjectRating.objects.filter(ProjectId=project, owner_id=user).delete()
    ProjectRating.objects.create(ProjectId=project, owner_id=user, rating=rating)
    return index(r)



@login_required
def user_profile(request):
    user = request.user
    projects = Project.objects.filter(owner_id=user)
    ratings = ProjectRating.objects.filter(owner_id=user)
    context = {
        'user': user,
        'projects': projects,
        'ratings': ratings
    }
    return render(request, 'user_profile.html', context)

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.mobile = request.POST['mobile']
        user.birthday = request.POST['birthday']
        user.country = request.POST['country']
        user.facebook_profile = request.POST['facebook_profile']
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('user_profile')
    else:
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'edit_user_profile.html', context)

@login_required
def delete_user_profile(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')
        if user.check_password(password):
            user.delete()
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('/')
        else:
            messages.error(request, 'Wrong password. Please try again.')
            return redirect('delete_user_profile')
    else:
        return render(request, 'delete_user_profile.html')
