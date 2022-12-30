from django.db import models

# Create your models here.
class Recipes(models.Model):
    rname = models.CharField(max_length=30, unique=True)
    rdescription = models.TextField(max_length=100)
    ringredients = models.TextField()
    rthumbnail = models.ImageField(upload_to='Image', default = None)
    rstep1 = models.TextField()
    rstep2 = models.TextField()
    rstep3 = models.TextField()
    rstep4 = models.TextField()
    rstep5 = models.TextField()

    def __str__(self):
        return self.rname

class UserData(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    user_email = models.EmailField(max_length=30, unique=True)
    user_password = models.CharField(max_length=30)

    def __str__(self):
        return self.user_name