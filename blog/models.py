from django.db import models

# Create your models here.

class AddUser(models.Model):

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.email}"
    

class Addblog(models.Model):

    author = models.ForeignKey(to=AddUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to='static/media')

    def __str__(self):
        return f"{self.author}"
    


