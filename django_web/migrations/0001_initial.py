# Generated by Django 2.1.2 on 2018-11-26 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info_one',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('memo', models.TextField(blank=True)),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=2)),
            ],
        ),
    ]
