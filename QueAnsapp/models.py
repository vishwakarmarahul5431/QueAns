from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    question=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    author=models.ForeignKey(User,related_name='question_post',on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to='images')
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    answer=models.TextField(blank=True,null=True)
    STATUS_CHOICE=(
    ('draft','DRAFT'),
    ('published','PUBLISHED')
    )
    status=models.CharField(choices=STATUS_CHOICE,max_length=100,default='draft')
    # jobtitle=models.ForeignKey(User,related_name='position',on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=20)
    # dob=models.DateField(null=True,blank=True)
    address=models.TextField()


