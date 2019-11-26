from django.urls import path, include

from rest_framework import routers
from .views import CategoryViewSet, ChoiceQuestionViewSet, choice_question_count

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'choice-questions', ChoiceQuestionViewSet)

app_name = 'questions'
urlpatterns = [
    path('', include(router.urls)),
    path('choice-question-count', choice_question_count)
]