from django.shortcuts import render
from django.views.generic import TemplateView


def all_class(request):
    return render(request, 'class_template.html')


def all_func(request):
    return render(request, 'func_template.html')


class Class_r(TemplateView):
    template_name = 'second_task/class_v_2template.html'
