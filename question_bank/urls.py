"""question_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from questions.views import CategoryViewSet, ChoiceQuestionViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('questions.urls', namespace='questions')),
    path('category/<int:pk>/',
         CategoryViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'post': 'update'}),
         name='category-detail'),
    path('choice-question/<int:pk>/',
         ChoiceQuestionViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}),
         name='choicequestion-detail'),
]
