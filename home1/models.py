from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.UUIDField('Book Id',primary_key=True, default = uuid.uuid4, help_text="generated unique id for book")
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    purchase_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', help_text='genre of book')
    author = models.ForeignKey('Author',on_delete=models.SET_NULL ,help_text='Book Author', null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Author(models.Model):
    author_name = models.CharField(max_length=100, help_text='Name of Author',null=True)
    numChoice = (
        ('1','One'),
        ('2','Two'),
        ('3','Three'),
        ('4','Four'),
        ('5', 'Five')
    )
    total_book_written = models.CharField(max_length=1, choices=numChoice, blank=True)
    date_of_birth = models.DateField('Birth',null=True, blank=True)
    date_of_death = models.DateField('Death',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author_name

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    
class Customer(models.Model):
    #id = models.UUIDField('Customer Id',primary_key=True, default = uuid.uuid4, help_text="generated unique id for customer")
    # id = models.AutoField(primary_key=True)
    C_name = models.CharField(max_length=100, help_text='Book Name',null=True)
    C_purchase_date = models.DateTimeField(null=True, blank=True)
    C_return_date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100, help_text='Book Name',null=True)
    genre = models.ManyToManyField('Genre', help_text='genre of book')
    author = models.ForeignKey('Author',on_delete=models.SET_NULL ,help_text='Book Author', null=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.C_name 
  

