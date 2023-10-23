from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    about = models.TextField(verbose_name='About me', help_text='Short information about you')
    foto = models.ImageField(upload_to='images/persons', blunk=True, null=True)
    email = models.EmailField(max_length=150)
    slug = models.SlugField(max_length=110)

    class Meta:
        ordering=['last_name', 'first_name']
        verbose_name_plural='teachers'

    def get_absolut_url(self):
        return reverse('teacher', args=[self.slug])

    def __str__(self):
        return f'Teacher {self.first_name} {self.last_name}'


class Student(models.Model):
