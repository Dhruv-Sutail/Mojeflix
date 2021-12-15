from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import now

class Subscription(models.Model):
    subscription_type = models.CharField(max_length=20)

    def __str__(self):
        return self.subscription_type

class Genre(models.Model):
    genre_type = models.CharField(max_length=30)

    def __str__(self):
        return self.genre_type

class Ott_type(models.Model):
    ott_type = models.CharField(max_length=30)

    def __str__(self):
        return self.ott_type

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Images", null=True )
    video = models.FileField(upload_to="Videos",null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    slug = models.SlugField(unique=True,db_index=True)
    ott_type = models.ForeignKey(Ott_type, on_delete=models.SET_NULL,null=True, related_name="otttype")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,null=True, related_name="genretype")
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL,null=True, related_name="subscriptiontype")

    def __str__(self):
        return self.title


class Usersubscription(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="user")
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL,null=True, related_name="subscriptiontypes")
    genre = models.CharField(max_length=200)
    date = models.DateField(default=now)

    def get_dept_values(self):
        ret = ''
        print(self.genre.all())
        
        for dept in self.dept.all():
            ret = ret + dept.dept_name + ','
        
        return ret[:-1]

class Comment(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="usern")
    comment = models.CharField(max_length=300)
    ratings = models.CharField(max_length=1)
    slug = models.CharField(max_length=200)
    date = models.DateField(default=now)
