from django.shortcuts import render


def all_class(request):
    return render(request, 'class_template.html')


def all_func(request):
    return render(request, 'func_template.html')

