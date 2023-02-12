from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid
import os
from taggit.managers import TaggableManager
from django.core.validators import RegexValidator


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.TextField()
    target = models.PositiveIntegerField()
    tags = TaggableManager()
    reports = models.PositiveSmallIntegerField(default=0)
    featured = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('projects/', filename)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.project.title


class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class Comment(models.Model):
    rate = models.PositiveSmallIntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reports = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.comment[:20]


class ReportedProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} reported {self.project}"

class ReportedComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(
        max_length=11,
        validators=[RegexValidator('(01)[0-9]{9}',
                                   message="phone number is not valid")])
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

def __str__(self):
    return self.user.username
