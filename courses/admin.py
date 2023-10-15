from django.contrib import admin
from .models import Course, Lesson, Schedule, Text, Image, \
File, URLVideo, Audio, Video


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	fields = [('title', 'price'), 'describe', 'duration', 'slug']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	prepoppulated_fields = {'slug': ('title')}


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	pass
	#list_filter = ('teacher', 'student')


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
	pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	pass


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
	pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	pass


@admin.register(URLVideo)
class URLVideoAdmin(admin.ModelAdmin):
	pass
