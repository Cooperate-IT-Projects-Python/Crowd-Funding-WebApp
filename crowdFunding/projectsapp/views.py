from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from users.models import CustomUser
from django.contrib.auth.decorators import login_required


# Create your views here.
def projectForm(r):
    if r.method == 'POST':
        # userid = r.session['userId']
        userid = 3
        if userid:
            try:
                # Create PROJECT
                projobject = Project()
                projobject.title = r.POST['title']
                projobject.details = r.POST['details']
                projobject.total_target = r.POST['target']
                projobject.start_campaign = r.POST['start']
                projobject.end_campaign = r.POST['end']
                category = Category.objects.get(name=r.POST['category'])
                projobject.category_id = category
                projobject.main_Image = r.FILES.get('mainImage')
                user = CustomUser.objects.get(id=userid)
                projobject.owner_id = user  # Session
                projobject.save()
                # Read Images
                images = r.FILES.getlist('images')
                # Table Projects_pictures
                for image in images:
                    projects_picturesobj = Projects_pictures()
                    projects_picturesobj.image = image
                    projects_picturesobj.ProjectId = projobject
                    projects_picturesobj.save()
            except Exception as e:
                # Replace This  With Flash
                categories = Category.objects.all()
                return render(r, 'createProject.html', {'categories': categories, 'error': e})
        else:
            # Replace This  With Flash or redirect to loginPage
            return HttpResponse("You Should Login First")
    # If Not Post
    categories = Category.objects.all()
    return render(r, 'createProject.html', {'categories': categories})


# -----------------Donate To Project -----------------
def make_donation(r, project_id):
    if r.method == 'POST':
        # userid = r.session['userId']
        userid = 3
        if userid:
            project = get_object_or_404(Project, id=project_id)
            project.current_donation += int(r.POST['donation'])
            project.save()
        else:
            # Replace This  With Flash or redirect to loginPage
            return HttpResponse("You Should Login First")

    project = Project.objects.get(id=project_id)
    max_donation_value = (project.total_target - project.current_donation)
    return render(r, 'donate.html', {'max_donation_value': max_donation_value, 'project_title': project.title})


def account(request):
    return render(request, 'user_profile.html')


def project_page(r, project_id):
    project = Project.objects.get(id=project_id)
    return render(r, 'project_page.html', {'project': project})


@login_required
def comment(r):
    project = Project.objects.get(id=r.POST['project_id'])
    Comment.objects.create(commentValue=r.POST['commentvalue'], ProjectId=project, owner_id=r.user)
    return project_page(r,r.POST['project_id'])


@login_required
def replay(r):
    commentobj = Comment.objects.get(id=r.POST['commentid'])
    Replay.objects.create(replayValue=r.POST['replayvalue'], commentId=commentobj, owner_id=r.user)
    return project_page(r,r.POST['project_id'])


@login_required
def report(r, kind, kind_id,project_id):
    if r.method == 'POST':
        if kind == "c":
            commentobj = get_object_or_404(Comment, id=kind_id)
            CommentReport.objects.create(reason=r.POST['reason'], commentId=commentobj, owner_id=r.user)
            return project_page(r, project_id)
        elif kind == "r":
            Replayobj = get_object_or_404(Replay, id=kind_id)
            ReplayReport.objects.create(reason=r.POST['reason'], replayId=Replayobj, owner_id=r.user)
            return project_page(r, project_id)
        elif kind == "p":
            projectobj = Project.objects.get(id=kind_id)
            ProjectReport.objects.create(reason=r.POST['reason'], ProjectId=projectobj, owner_id=r.user)
        return HttpResponseRedirect("/")
    return render(r, 'report.html')
#test