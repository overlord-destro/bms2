from django.urls import path
from . import views





urlpatterns = [
    path('all_books/', views.BooksView.as_view()),
    path('get_book/<int:pk>', views.GetOneView.as_view()),
    path("create_book/", views.CreateBookView.as_view()),
    path("update_book/<int:pk>", views.UpdateBookView.as_view()),
    path("delete_book/<int:pk>", views.DeleteBookView.as_view()),
    path("num_of_books/", views.num_of_books),
    path("check_out_a_book", views.AccessorView.as_view())
]