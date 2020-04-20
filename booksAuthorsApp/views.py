from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    return render(request, 'index.html')

def addBook(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'addBook.html', context)

def addAuthor(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'addAuthor.html', context)

def submitBook(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        return redirect('/addBook')

def submitAuthor(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        return redirect('/addAuthor')

def book(request, id):
    request.session['bookID'] = id
    context = {
        'book': Book.objects.get(id=id),
        'authors': Author.objects.exclude(books=id),
    }
    return render(request, 'book.html', context)

def author(request, id):
    request.session['authorID'] = id
    context = {
        'author' : Author.objects.get(id=id),
        'books' : Book.objects.exclude(authors=id)
    }
    return render(request, 'author.html', context)

def bookAddAuthor(request):
    addedAuthor = Author.objects.get(id = request.POST['authors'])
    bookID = request.session['bookID']
    if request.method == "POST":
        Book.objects.get(id=bookID).authors.add(addedAuthor)
        return redirect(f'/book/{bookID}')

def authorAddBook(request):
    addedBook = Book.objects.get(id = request.POST['books'])
    authorID = request.session['authorID']
    if request.method == "POST":
        Author.objects.get(id=authorID).books.add(addedBook)
        return redirect(f'/author/{authorID}')