from django.db import models

# Create your models here.
class beritaComment(models.Model):
    forBerita = models.CharField(max_length = 255)
    user = models.CharField(max_length = 255)
    comment = models.CharField(max_length = 255)

    def __str__(self):
        return '{}, {}'.format(self.id,self.forBerita)
