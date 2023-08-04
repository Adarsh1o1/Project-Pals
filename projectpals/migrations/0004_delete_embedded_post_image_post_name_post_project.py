# Generated by Django 4.1.7 on 2023-04-01 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpals', '0003_rename_project_name_post_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='embedded',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='projectpals/images'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.CharField(default='', max_length=10),
        ),
    ]
