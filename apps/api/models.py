from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField(blank = True, null=True, max_length=250)

    def __str__(self):
        return self.name

class Advocate(models.Model):
    name = models.CharField(max_length = 200)
    bio = models.TextField(blank = True, null=True, max_length=250)
    company = models.ForeignKey(Company, null=True, blank=True, 
                                on_delete=models.SET_NULL, related_name="employees")

    def __str__(self):
        return self.name
