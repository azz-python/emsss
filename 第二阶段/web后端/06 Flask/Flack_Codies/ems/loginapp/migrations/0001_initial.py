# Generated by Django 2.2.2 on 2019-07-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('headpic', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
