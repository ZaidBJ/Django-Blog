from django.db import models
from django.conf import settings
# Create your models here.
User =  settings.AUTH_USER_MODEL

class Post(models.Model):
    title =  models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey('Author',on_delete='CASCADE')
    image = models.ImageField(upload_to='post')
    slug = models.SlugField()


    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_pics')


    def __str__(self):
        return self.user.username