from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    auth = models.CharField(null= True, blank= True, max_length=50)
    title = models.CharField(null=True, blank= True, max_length=100)
    content = models.TextField(blank= True)
    cover_image = models.FileField(upload_to='cover_image',null= True)
    url_image = models.URLField(null= True, blank= True)
    createtime = models.DateField(auto_now= True)

    def __str__(self):
        return self.auth + ' '+ self.title

class Comment(models.Model):
    name = User.username
    comment = models.TextField(null= True, blank= True)
    createtime = models.DateField(auto_now=True)
    belong_article = models.ForeignKey(to=Article, related_name="under_comment")
    belong_user = models.ForeignKey(to = User, related_name="comment")
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to = User, related_name="profile")
    profile_image = models.FileField(upload_to='profile_image', blank= True)
