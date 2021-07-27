# Generated by Django 3.2.5 on 2021-07-25 00:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='内容')),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='期日')),
            ],
            options={
                'verbose_name': 'Todoリスト',
                'verbose_name_plural': 'Todoリスト',
            },
        ),
    ]
