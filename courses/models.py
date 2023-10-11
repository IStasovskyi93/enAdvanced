from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course', unique=True,)
    desribe = models.TextField(verbose_name='Describe')
    #teacher = ForeignKey(Teacher, on_delete=models.DO_NOTHING) 
    price = models.IntegerField(verbose_name='Price')
    duration = models.DurationField(verbose_name='Duration of course')
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
	    return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titel')
    describe = models.TextField(verbose_name='Describe')
    #teacher = ForeignKey(Techer, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField(verbose_name='Duration of lesson')

    def __str__(self):
	    return self.title


class Schedule(models.Model):
    time_lesson = models.DateTimeField(verbose_name='Time of lesson')
    #student = models.ForeignKey(persons.Student, on_delete=models.CASCADE)
    #teacher = models.ForeignKey(persons.Teacher, on_delete=models.CASCADE)

    def __str__(self):
	    return self.f'Schedule'


class Content(models.Model):
	title = CharField(max_length=100, verbose_name='description object')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title


class Text(Content):
	text = models.TextField()


class File(Content):
	file = models.FileField(upload_to='files', verbose_name='file as pdf')


class Image(Content):
	image = models.FileField(upload_to='images', verbose_name='image')


class URLVideo(Content):
	url_video = models.URLField()


class Audio(Content):
	audio = models.FileField(upload_to='audies', verbose_name='audio')


class Video(Content):
	video = models.FileField(upload_to='videos', verbose_name='video')
