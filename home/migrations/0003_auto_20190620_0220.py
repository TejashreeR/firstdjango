# Generated by Django 2.2.2 on 2019-06-19 20:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190620_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='Name of Author', max_length=100, null=True)),
                ('total_book_written', models.CharField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Birth')),
                ('date_of_death', models.DateField(blank=True, null=True, verbose_name='Death')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_author',
        ),
        migrations.AddField(
            model_name='book',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='generated unique id for book', primary_key=True, serialize=False, verbose_name='Book Id'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='Book Author', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='genre of book', to='home.Genre'),
        ),
    ]
