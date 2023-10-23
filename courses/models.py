from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Course', 
                            unique=True, help_text='Name of course')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=4, decimal_places=2, 
                                verbose_name='Price')
    duration = models.CharField(max_length=50, verbose_name='Duration of course')
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
	    return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titel', unique=True)
    description = models.TextField(verbose_name='Description')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.CharField(max_length=50, verbose_name='Duration of lesson')
    slug = models.SlugField(max_length=50, blank=True)
    
    def __str__(self):
	    return self.title


class Schedule(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE)
    time_lesson = models.DateTimeField(verbose_name='Time of lesson')
    #student = models.OneToOneField(persons.Student, on_delete=models.CASCADE)
    #teacher = models.OneToOneField(persons.Teacher, on_delete=models.CASCADE)

    def __str__(self):
	    return f'{self.lesson} in {self.time_lesson}'


class Content(models.Model):
	title = models.CharField(max_length=200, verbose_name='description object')
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
	image = models.FileField(upload_to='images')


class URLVideo(Content):
	url_video = models.URLField(help_text='URL adress for video from internet')


class Audio(Content):
	audio = models.FileField(upload_to='audies')


class Video(Content):
	video = models.FileField(upload_to='videos')
