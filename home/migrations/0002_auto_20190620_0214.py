# Generated by Django 2.2.2 on 2019-06-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_auther',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(help_text='Book author', max_length=100, null=True),
        ),
    ]
