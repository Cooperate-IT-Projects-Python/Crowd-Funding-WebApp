from django.shortcuts import render
from projectsapp.models import Project, ProjectRating
from users.models import CustomUser


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
