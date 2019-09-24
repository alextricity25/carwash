from django.db import models
from washes.models import Washes


class Tools(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    use = models.CharField(max_length=50)
    # The wash the tool is associated with. Tools can be associated
    # with multiple washes.
    wash = models.ManyToManyField(Washes, related_name='tools')
    # The owner of the tool
    owner = models.ForeignKey('auth.User', related_name='tools', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
