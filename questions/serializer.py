from .models import Category, ChoiceQuestion
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    choice_questions = serializers.HyperlinkedRelatedField(many=True,
                                                           view_name='choicequestion-detail',
                                                           read_only=True)
    class Meta:
        model = Category
        fields = ['url', 'name', 'choice_questions']


class ChoiceQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChoiceQuestion
        fields = ['url', 'content', 'category', 'option_a', 'option_b', 'option_c', 'option_d', 'answer', 'solution']
