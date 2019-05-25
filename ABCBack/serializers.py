from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import PrimaryKeyRelatedField
from .models import Category, Event


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id','description',)


class EventSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Event
        fields = ('name','category','place','address','initial_date','end_date','is_on_site')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.get(description=category_data['description'])
        event = Event.objects.create(**validated_data, category=category)
        return event

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        if(category_data['description'] != instance.category.description):
            instance.category = Category.objects.get(description=category_data['description'])
        instance.name = validated_data.get('name', instance.name)
        instance.place = validated_data.get('place', instance.place)
        instance.address = validated_data.get('address', instance.address)
        instance.initial_date = validated_data.get('initial_date', instance.initial_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_on_site = validated_data.get('is_on_site', instance.is_on_site)
        instance.save()
        return instance


class EventListByCategorySerializer(ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('description','events')
