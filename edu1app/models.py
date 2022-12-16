from django.db import models

# Create your models here.

class Blogmodel(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    image=models.CharField(max_length=250)
    author=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)
    numdis=models.IntegerField()

    def __str__(self):
        return self.title[:20]+"..."




