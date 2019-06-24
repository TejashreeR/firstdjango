from django.shortcuts import render,redirect
from .forms import BookForms,SearchForm,ModelBookForms
from home1.models import Book
from django.contrib import messages
#from django.utils import timezone
# Create your views here.
def form_view(request):
    context = None
    msg=None
    form = None
    #book=Book.objects.all()
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            #book = Book(
            #    name=form.cleaned_data.get('name'),
            #    purchase_date=form.cleaned_data.get('pur_date'),
            #    genre=form.cleaned_data.get('genre'),
            #    author=form.cleaned_data.get('author')
            #)
            book = Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                #genre=form.cleaned_data.get('genre'),
                author=form.cleaned_data.get('author')
            )
            book.save()
            msg ='Book Added Successfully!!'
        else:
            msg = form.errors
            
        
    else:
        form = BookForms()
    return render(request,'forms.html',{"msg":msg,"forms":form})

def html_form(request):
    value = ''
    if request.method=='POST':
        value = request.POST.get('name')
        return render(request,'values.html',{'values':value})

    else:
        value == 'worng input'
    return render(request,'design.html')

def booksearch(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            book=Book.objects.filter(name__contains=q)
            return render(request,'showtables.html',{'book':book})
    else:
        form=SearchForm()
        book=Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})

def deletebook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+'Successfully!')
    return redirect('/')

def editbook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Updated Successfully!!')
            return redirect('/')
    else:
        form = ModelBookForms(instance=book)
    return render(request,'editbook.html',{'form':form})