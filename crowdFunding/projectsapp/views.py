from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Category, Project, Projects_pictures
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
                #return HttpResponse("Enter Valid Data title should Be unique")
                categories = Category.objects.all()
                return render(r, 'createProject.html', {'categories': categories, 'error': e})
        else:
            # Replace This  With Flash or redirect to loginPage
            return HttpResponse("You Should Login First")
    # If Not Post
    categories = Category.objects.all()
    return render(r, 'createProject.html', {'categories': categories})
