from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('名字', max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category:detail', kwargs={'pk': self.pk})


class ChoiceQuestion(models.Model):
    content = models.CharField('题目', max_length=200)
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='分类', related_name='choice_questions', on_delete=models.CASCADE)
    option_a = models.CharField('A选项', max_length=100)
    option_b = models.CharField('B选项', max_length=100)
    option_c = models.CharField('C选项', max_length=100)
    option_d = models.CharField('D选项', max_length=100, blank=True)
    answer = models.CharField('答案', max_length=10)
    solution = models.CharField('解析', max_length=300, blank=True)

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.content

