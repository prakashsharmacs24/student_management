from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class School(models.Model):
    title = models.CharField(max_length=200)
    class Meta:
        ordering = ['title']


    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    school = models.ForeignKey(School,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    dob = models.DateField(verbose_name='Date of birth')
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.name

    @property
    def age(self):
        return timezone.now().year - self.dob.year

    @property
    def is_adult(self):
        return self.age >=18