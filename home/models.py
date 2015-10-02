from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    interests = models.TextField()
    registered_date = models.DateField(auto_now_add = True, auto_now = False)
    last_update = models.DateField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return self.full_name


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    floor = models.CharField(max_length=200)
    has_poduim = models.BooleanField()
    commission_date = models.DateField(auto_now = True,auto_now_add = False)
    created_at = models.DateField(auto_now_add = True, auto_now = False)
    updated_at = models.DateField(auto_now = True,auto_now_add = False)

    def __str__(self):
        return self.name
