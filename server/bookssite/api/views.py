from django.shortcuts import render
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .models import Book
from .serializer import BookSerializer

class OneHundredsPerDayThrottle(UserRateThrottle):
    rate = '100/day'

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is called')
        return func(*args, **kwargs)
    return wrapper

@api_view(['GET'])
@throttle_classes([OneHundredsPerDayThrottle])
def get_books(request):
    books = Book.objects.all()
    serializedData = BookSerializer(books, many=True).data
    return Response(serializedData)

@api_view(['POST'])
@throttle_classes([OneHundredsPerDayThrottle])
def create_book(request):
    data = request.data
    serializer = BookSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@throttle_classes([OneHundredsPerDayThrottle])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        data = request.data
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

