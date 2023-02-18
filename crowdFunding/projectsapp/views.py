from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Category, Project, Projects_pictures, Tags
from users.models import CustomUser


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
        averageRating = Project.average_rating(project)
        goal_percentage = Project.goal_percentage(project)
        projectsPictures = Projects_pictures.objects.all()
        tags = Tags.objects.filter(ProjectId=project.id)

        tagList=[]
        for tag in tags:
            tagList.append(tag.name_tag)

        similar_tags = Tags.objects.filter(name_tag__in=tagList).exclude(ProjectId=project).distinct()[:4]

        similar_projects = []
        for proj in similar_tags:
            similar_projects.append(proj.ProjectId)

        context = {
            'project': project,
            'average_rating': averageRating,
            'project_pictures': projectsPictures,
            'goal_percentage': goal_percentage,
            'tags': tags,
            'similar_projects': similar_projects,
        }

        return render(r, 'project_page.html',context)
