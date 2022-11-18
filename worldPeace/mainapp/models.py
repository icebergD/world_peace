from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title

class MUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    photo = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    language1 = models.CharField(max_length=250, blank=True, null=True)
    language2 = models.CharField(max_length=250, blank=True, null=True)
    study_name = models.CharField(max_length=250, blank=True, null=True)
    study_end_year = models.CharField(max_length=250, blank=True, null=True)
    study_grade = models.CharField(max_length=250, blank=True, null=True)
    faculty = models.CharField(max_length=250, blank=True, null=True)
    speciality = models.CharField(max_length=250, blank=True, null=True)


class Busines(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

class Vacancy(models.Model):
    busines = models.ForeignKey(Busines, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bussy = models.CharField(max_length=250, blank=True, null=True)


class Tutorial(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    video = models.CharField(max_length=250, blank=True, null=True)

class Achive(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    descriprion = models.CharField(max_length=250, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
