from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Counter
from .serializers import CounterSerializer

@api_view(['GET'])
def get_counter(request):
    counter_instance = Counter.objects.first()
    if counter_instance is None:
        counter_instance = Counter.objects.create(value=50)
    serializer = CounterSerializer(counter_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def increment_counter(request):
    counter = get_object_or_404(Counter, pk=1)
    counter.value += 1
    counter.save()
    return Response({'message': 'Counter incremented successfully'})

@api_view(['POST'])
def decrement_counter(request):
    counter = get_object_or_404(Counter, pk=1)
    counter.value -= 1
    counter.save()
    return Response({'message': 'Counter decremented successfully'})

@api_view(['POST'])
def reset_counter(request):
    counter = get_object_or_404(Counter, pk=1)
    counter.value = 0
    counter.save()
    return Response({'message': 'Counter reset successfully'})