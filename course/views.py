from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse 
from .models import Course
from .forms import CourseForm
from django.views import View

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id_ = self.kwargs.get("id")
        obj = get_object_or_404(self.model ,  id = id_)
        return obj

class CourseCreateView(View):
    template_name = 'course_create.html'
    def get(self,request, *args , **kwargs):
        form_class = CourseForm(request.POST or None, request.FILES or None)
        context = {
            'form' : form_class
        }
        return render(request , self.template_name , context)
    def post(self, request , *args , **kwarg):
        form_class = CourseForm(request.POST , request.FILES or None)
        if form_class.is_valid():
            form_class.save()
            form_class = CourseForm()
        context = {
            'form': form_class
        }
        return render(request , self.template_name , context)

class CourseListView(View):
    template_name = 'course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseDetailView(CourseObjectMixin, View):
    template_name = 'course_detail.html'

    def get(self, request , *args , **kwargs):
        object = self.get_object()

        context = {
            'object' : object
        }         
        return render(request, self.template_name , context)

class CourseUpdateView(CourseObjectMixin , View):
    template_name = 'course_create.html'

    def get(self,request, *args , **kwargs):
        obj = self.get_object()
        form_class = CourseForm(request.POST or None, request.FILES or None, instance= obj)
        context = {
            'form' : form_class
        }
        return render(request , self.template_name , context)

    def post(self, request , *args , **kwarg):
        obj = self.get_object()
        form_class = CourseForm(request.POST or None,request.FILES or None, instance= obj)
        if form_class.is_valid():
            form_class.save()
            form_class = CourseForm()

        context = {
            'form': form_class
        }
        return render(request , self.template_name , context)

class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'course_delete.html'
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/course/')
        return render(request, self.template_name, context)