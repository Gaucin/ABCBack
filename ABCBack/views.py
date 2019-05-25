from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EventSerializer, EventListByCategorySerializer, CategorySerializer
from .models import Event, Category


class EventListView(ListCreateAPIView):
    queryset = Event.objects.order_by('-initial_date')
    serializer_class = EventSerializer


class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EventListByCategoryView(ListAPIView):
    serializer_class = EventListByCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(pk=self.kwargs['pk'])
