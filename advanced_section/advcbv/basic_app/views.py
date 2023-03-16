from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models
# Create your views here.
# def index(request):
#     return render(request, 'index.html')


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL")


class IndexView(TemplateView):
    template_name = 'index.html'
    print('start index')
    def get_context_data(self, **kwargs):
        print('context0')
        context = super().get_context_data(**kwargs)
        print('context')
        context['injectme'] = 'BASIC INJECTION!'
        print('context1')
        return context
# class IndexView(TemplateView):
#     template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = "school_list"
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
