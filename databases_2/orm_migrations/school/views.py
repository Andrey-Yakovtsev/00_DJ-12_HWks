from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # students_data = Student.objects.all().order_by('group')
    students_data = Student.objects.prefetch_related('teacher').all().order_by('group')
    context = {'object_list': students_data}

    return render(request, template, context)
