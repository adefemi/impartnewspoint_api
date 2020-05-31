# Generated by Django 3.0.6 on 2020-05-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200509_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='author',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='name',
            field=models.CharField(default='Annoymous', max_length=255),
        ),
    ]
