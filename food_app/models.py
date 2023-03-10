from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipes(models.Model):
    rname = models.CharField(max_length=30, unique=True)
    rdescription = models.TextField(max_length=100)
    ringredients = models.JSONField(default=list())
    rthumbnail = models.ImageField(upload_to='Image', default = None)
    rstep1 = models.TextField()
    rstep2 = models.TextField()
    rstep3 = models.TextField()
    rstep4 = models.TextField()
    rstep5 = models.TextField()
    rauthor = models.ForeignKey(to = User,on_delete=models.CASCADE,default = None)

    def __str__(self):
        return self.rname
