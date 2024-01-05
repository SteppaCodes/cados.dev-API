from django.db import models

class Advocate(models.Model):
    name = models.CharField(max_length = 200)
    bio = models.TextField(blank = True, null=True, max_length=250)

    def __str__(self):
        return self.name
