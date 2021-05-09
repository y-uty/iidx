# Generated by Django 2.2.20 on 2021-05-02 05:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('ver_no', models.IntegerField()),
                ('ver_name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('score', models.IntegerField()),
                ('pgreat', models.IntegerField()),
                ('great', models.IntegerField()),
                ('misscount', models.IntegerField()),
                ('cleartype', models.CharField(max_length=200)),
                ('djlevel', models.CharField(max_length=3)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('ver_no', models.IntegerField()),
                ('ver_name', models.CharField(max_length=100)),
                ('difficulty', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('score', models.IntegerField()),
                ('pgreat', models.IntegerField()),
                ('great', models.IntegerField()),
                ('misscount', models.IntegerField()),
                ('cleartype', models.CharField(max_length=200)),
                ('djlevel', models.CharField(max_length=3)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]