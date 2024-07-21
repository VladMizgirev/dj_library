from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)
    """получите список книг из БД
    отсериализуйте и верните ответ
    """
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Книга успешно создана')


class BookDetailsView(RetrieveAPIView):
    def get(self, request, pk):
        try:
            phone = Book.objects.get(id=pk)
            serializer = BookSerializer(phone)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"message": "Книга не найдена"}, status=status.HTTP_404_NOT_FOUND)
    # реализуйте логику получения деталей одного объявления
    ...


class BookUpdateView(UpdateAPIView):
    def patch(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            serializer = BookSerializer(book, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"message": "Книга не найдена"}, status=status.HTTP_404_NOT_FOUND)
    # реализуйте логику обновления объявления
    ...


class BookDeleteView(DestroyAPIView):
    def delete(self, request, pk):
        try:
            phone = Book.objects.get(id=pk)
            phone.delete()
            return Response({"message": "Запись успешно удалена"})
        except Book.DoesNotExist:
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)
    # реализуйте логику удаления объявления
    ...


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # реализуйте CRUD для заказов
    ...
