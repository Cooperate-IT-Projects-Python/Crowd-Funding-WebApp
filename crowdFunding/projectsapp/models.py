from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=10, unique=True)
    details = models.CharField(max_length=50)
    rate = models.IntegerField(default=0)
    total_target = models.IntegerField(null=False, blank=False)
    current_donation = models.IntegerField(default=0)
    start_campaign = models.DateField(default=datetime.now, blank=True)
    end_campaign = models.DateField(null=False, blank=False)
    created_at = models.DateField(default=datetime.now, blank=True)
    selected_at_by_admin = models.BooleanField(default=False)
    category_id = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    owner_id = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Projects_pictures(models.Model):
    image = models.ImageField(upload_to='media/Projects/%y/%m/%d', null=False, blank=False)
    ProjectId = models.ForeignKey(to="Project", on_delete=models.PROTECT)

    def __str__(self):
        return self.ProjectId.title
