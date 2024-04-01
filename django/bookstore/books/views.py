from django.shortcuts import render
from django.http import HttpResponse
import json





# Create your views here.

def hello(req):
    print (req)
    return HttpResponse('we are here')

def welcome(req):
    print(req)
    return HttpResponse("hello soso")

books =[
    {'id':1, 'name':'story1', 'price':'104 LE','image':"1.jpg"},
    {'id':2, 'name':'story2', 'price':'10 LE','image':"2.jpg"},
    {'id':3, 'name':'story3', 'price':'400 LE','image':"3.jpg"},
    {'id':4, 'name':'story4', 'price':'300 LE','image':"1.jpg"},
    {'id':5, 'name':'story5', 'price':'100 LE','image':"1.jpg"}
]

def getallbooks(req):
    print (req)
    return HttpResponse(books)


def getbookbyid(req, id):
    book_list = filter(lambda book: book['id'] == id, books)
    allbooks = list(book_list)
    if allbooks:
        book = allbooks[0]
        return render(req, "books/detailes.html", context={"book": book})

def home(request):
    return render(request, "books/home.html",
                  context = {"books": books},
                  status=200)  # render http response
    
def contactus(req):
    return render(req, "books/contactus.html",status=200)    
def aboutus(req):
    return render(req, "books/aboutus.html",status=200)    
    

