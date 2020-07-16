from django.db import models

# Create your models here.
class kulturPost(models.Model):
    judul = models.CharField(max_length = 255)
    postby = models.CharField(max_length = 255)
    lokasi = models.CharField(max_length = 255)
    body = models.TextField()
    category = models.CharField(max_length = 255)
    media = models.FileField(upload_to='post/')
    likes = models.CharField(max_length = 255)
    slug = models.SlugField()

    def __str__(self):
        return '{}, {}'.format(self.id,self.judul)