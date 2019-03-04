from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):

    blogTitle=models.CharField(max_length=200)
    blogEntry=models.TextField()  #a textfield for a blog
    username=models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank = True)   #sets the user as a foreign key

    def __str__(self):
        return self.blogTitle