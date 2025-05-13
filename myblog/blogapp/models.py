from django.db import models

# Create your models here.
class Blog(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=40)
    content = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/",default="images/default.png")

# class User(models.Model):
#     def __str__(self):
#         pass
#     username = models.CharField(max_length=50,primary_key=True)
#     password = models.CharField(max_length=20)