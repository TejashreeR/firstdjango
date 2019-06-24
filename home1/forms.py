"""from django import forms

class CustomForms(forms.Form):
    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(
            attrs = {'placehodler':'Your username',
            'class':'form-control',
            'max':'20'
            }
        )
    )

    email = forms.EmailField(label="Your Email",widget=forms.EmailInput(attrs={'placeholder':'ac@mail.com','class':'form-control'}))"""
from django import forms
from home1.models import Book,Author,Genre

class BookForms(forms.Form):
    title = forms.CharField(label='Book Name',
        widget = forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    author = forms.ModelChoiceField(
                    queryset=Author.objects.all(),
                    empty_label='Author', widget= forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))
    #isbn = forms.CharField(label='ISBN Number',
    #                        widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
    #                       'class':'form-control','name':'isbn','id':'isbn'}))
    #genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
    #                       widget=forms.CheckboxSelectMultiple)
    pur_date = forms.DateField(label='',
                            widget = forms.DateInput(attrs={'placeholder':'Purchase date','name':'pur_date',
                            'id':'pur_date','class':'form-control'}))

class ModelBookForms(forms.ModelForm):
    #  title = forms.CharField(label='Book Name',
    #     widget = forms.TextInput(attrs={'maxlength':'30','placeholder':'Book Name','class':'form-control'}))
    # author = forms.ModelChoiceField(
    #                 queryset=Author.objects.all(),
    #                 empty_label='Author', widget= forms.Select(attrs={'name':'author','id':'author','class':'custom-select'}))
    # summary = forms.CharField(label='Summary',
    #                         widget = forms.Textarea(attrs={'placeholder':'Summary','name':'summary',
    #                         'id':'summary','class':'form-control'}))
    # isbn = forms.CharField(label='ISBN Number',
    #                         widget=forms.TextInput(attrs={'placeholder':'ISBN Number',
    #                         'class':'form-control','name':'isbn','id':'isbn'}))
    # genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
    #                         widget=forms.CheckboxSelectMultiple)
    # pur_date = forms.DateField(label='',
    #                         widget = forms.DateInput(attrs={'placeholder':'Purchase date','name':'pur_date',
    #                         'id':'pur_date','class':'form-control'}))
    
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ('name','genre','purchase_date','author')
    
class SearchForm(forms.Form):
    q = forms.CharField(label='',widget = forms.TextInput(attrs={'maxlength':'30','placeholde':'Search','class':'form-control','minlength':'2'}))
    
