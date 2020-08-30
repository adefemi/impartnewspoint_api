# Generated by Django 3.0.6 on 2020-08-30 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarkettingBanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('marketting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banners', to='user.Marketting')),
            ],
        ),
    ]