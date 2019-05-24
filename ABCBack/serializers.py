from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import Category, Event


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','description',)


class EventSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('name','category','place','address','initial_date','end_date','is_on_site')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        print("category data ",category_data)
        category = CategorySerializer(data=category_data)
        event = Event.objects.create(**validated_data, category=category)
        return event

    def update(self, instance, validated_data):
        return instance


class EventDetailSerializer(EventSerializer):
    category = CategorySerializer()

    def update(self, instance, validated_data):
        instance.save()
        return instance


class EventListByCategorySerializer(ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('description','events')
