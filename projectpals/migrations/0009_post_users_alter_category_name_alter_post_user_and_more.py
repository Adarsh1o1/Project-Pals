# Generated by Django 4.2 on 2023-04-04 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectpals', '0008_category_post_delete_embedded'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th')], default='1st', max_length=3),
        ),
        migrations.DeleteModel(
            name='data_science',
        ),
    ]
