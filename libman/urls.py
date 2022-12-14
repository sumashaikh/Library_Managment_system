from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^book/$', views.view_books, name='view_books'),
    re_path(r'^book/add/$', views.add_book, name='add_book'),
    re_path(r'^student/$', views.view_student, name='view_student'),
    re_path(r'^student/add/$', views.add_student, name='add_student'),
    re_path(r'^employer/$', views.view_employer, name='view_employer'),
    re_path(r'^employer/add/$', views.add_employer, name='add_employer'),
    #url(r'^profile/$', views.view_profile, name='profile'),
    re_path(r'^issue/$', views.view_issue, name='view_issue'),
    re_path(r'^issue/new/$', views.new_issue, name='new_issue'),
    re_path(r'^return_book/$', views.return_book, name='return_book'),
    #url(r'^delete_book/$', views.ViewDeletePost, name='delete_book'),
    #url(r'^update_book/$', views.ViewUpdatePost.as_view(), name='update_book'),
    #url(r'^book/search/$', views.search_books, name='search_books'),
]