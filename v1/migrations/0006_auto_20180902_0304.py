# Generated by Django 2.0.6 on 2018-09-02 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_course_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='v1.Game'),
        ),
        migrations.AlterField(
            model_name='course',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='scores',
            field=models.ManyToManyField(blank=True, related_name='_game_scores_+', to='v1.Score'),
        ),
    ]
