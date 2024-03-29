# Generated by Django 3.2.11 on 2022-07-26 21:14

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('styles', '0003_auto_20220317_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, help_text='Introduce your class or club. Be sure to mention qualifications and cost.', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='series',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text="Enter single word or 'quoted strings' to be used to find your class or club.", through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags to be searched to find your series'),
        ),
    ]
