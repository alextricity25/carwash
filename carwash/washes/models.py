from django.db import models

class Washes(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.title
    

