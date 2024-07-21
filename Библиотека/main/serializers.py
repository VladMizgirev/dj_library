from rest_framework import serializers
from main.models import Book, Order

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    # реализуйте сериализацию объектов модели Book
    ...

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['orders_count'] = ...
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
    # добавьте поля модели Order
    ...

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation
