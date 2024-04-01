from django.urls import path
from books.views import hello, getallbooks, welcome, getbookbyid,home,aboutus,contactus

urlpatterns = [
    path('helloworld/',hello,name="hellopage" ),
    path('welcomeso/',welcome,name = "welcome" ),
    path('land/', getallbooks, name='land'),
    path('book/<int:id>', getbookbyid, name='books.getbookbyid'),
    path('home/', home, name='books.home'),
    path('aboutus/', aboutus,name='books.aboutus'),
    path('contactus/', contactus,name='books.contactus')
]
