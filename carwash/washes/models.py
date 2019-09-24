from django.db import models


class Washes(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')
    owner = models.ForeignKey('auth.User', related_name='washes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
