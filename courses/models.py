from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course', unique=True,)
    desribe = models.TextField(verbose_name='Describe')
    #teacher = ForeignKey(Teacher, on_delete=models.DO_NOTHING) 
    price = models.IntegerField(verbose_name='Price')
    duration = models.DurationField()
    slug = models.SlugField(max_length=50, blank=True)
    quantity = models.IntegerField(blank=True)

class Lesson(models.Model):
    name = models.CharField(max_length=200, verbose_name='Titel')
    describe = models.TextField(verbose_name='Describe')
    #teacher = ForeignKey(Techer, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()

class Schedule(models.Model):
    time_lesson = models.DateTimeField()
    #student = models.ForeignKey(persons.Student, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(persons.Teacher, on_delete=models.CASCADE)
