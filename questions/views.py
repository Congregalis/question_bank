from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, ChoiceQuestion
from .serializer import CategorySerializer, ChoiceQuestionSerializer
from .permissions import IsAdminOrReadOnly
from .utils import Utf8JSONRenderer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    # renderer_classes = [Utf8JSONRenderer]


class ChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer
    permission_classes = [IsAdminOrReadOnly]
    # renderer_classes = [Utf8JSONRenderer]


@api_view(['GET'])
def choice_question_count(request):
    """
    获得选择题的数量
    """
    return Response(ChoiceQuestion.objects.count())
