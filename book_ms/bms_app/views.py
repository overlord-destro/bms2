from .models import Books, Accessor
from .serializers import BooksSerializer, AccessorSerializer
from django.http import HttpResponse
#from django.http.response import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

total_books = len(Books.objects.all())
class BooksView(APIView):
    ##for getting all books
    def get(self, request):
        all_books = Books.objects.all()
        serializer = BooksSerializer(all_books, many=True)
        return Response({"all books": serializer.data})
    

class GetOneView(APIView):    
    ##for getting single book
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        serializer = BooksSerializer(book, many=False)
        return Response({"That one book": serializer.data})
    
    
    ##for creating a book
class CreateBookView(APIView):
    def post(self, request):
        book = request.data.get('book')

        serializer = BooksSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"Success": "Book '{}' created successfully".format(book_saved)})
    

##for updating book
class UpdateBookView(APIView):
    def put(self, request, pk):
        existing_book = get_object_or_404(Books.objects.all(), pk=pk)
        data = request.data.get('book')
        serializer = BooksSerializer(instance=existing_book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"Success": "Book '{}' updated successfully".format(book_saved)})
    
##for deleting a book
class DeleteBookView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Books.objects.all(), pk=pk)
        book.delete()
        return Response("Book deleted successfully")
    
book_list = Books.objects.all()
new_list = []
for elem in book_list:
    new_list.append(elem.title)

    
#for checking number of books
def num_of_books(request):
    total_num = total_books
    a = Accessor.objects.all()
    for elem in a:
        if elem.book_title in new_list:
            new_list.remove(elem.book_title)
            total_num -= 1
    return HttpResponse(f"There a total of {total_num} books in this library")





class AccessorView(APIView):
    #creating a checker outer
    def post(self, request):
        accessor = request.data.get('accessor')

        serializer = AccessorSerializer(data=accessor)
        if serializer.is_valid(raise_exception=True):
            details_saved = serializer.save()
            return Response({"Success": "{}' checked out book successfully".format(details_saved)})
