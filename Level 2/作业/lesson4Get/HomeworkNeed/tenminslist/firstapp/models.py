from django.db import models

# Create your models here.
class Article(models.Model):
    img_url = models.URLField(null = True,blank=True)
    title = models.CharField(null= True, blank=True, max_length=100)
    author = models.CharField(null = True, blank= True, max_length=100)
    content = models.TextField(null= True, blank=True)
    views = models.IntegerField(null= True, blank=True)
    favs = models.IntegerField(null= True, blank=True)
    createtime = models.DateField(auto_now=False, auto_now_add=False)
    TAG_CHOICES = (
        ("all","all"),
        ("new","new"),
    )
    tag = models.CharField(null = True, blank = True, max_length=5, choices = TAG_CHOICES)

    def __str__(self):
        return self.title
