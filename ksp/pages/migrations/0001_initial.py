# Generated by Django 2.2 on 2019-07-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_name', models.CharField(max_length=50)),
                ('criminal_Img', models.ImageField(upload_to='ksp/static/images/')),
            ],
        ),
    ]