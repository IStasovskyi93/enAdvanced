# Generated by Django 4.2.5 on 2023-10-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_desribe_course_describe_lesson_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Price'),
        ),
    ]
