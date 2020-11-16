from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import employeeDB
from .forms import EmployeeForm, RegisterForm


# Create your views here.


class EmployeeListView(ListView):
    template_name = 'employee/list.html'
    queryset = employeeDB.objects.all()


class EmployeeCreate(LoginRequiredMixin, CreateView):
    template_name = 'employee/create.html'
    form_class = EmployeeForm
    success_url = '/employee/list/'


class EmployeeDetail(LoginRequiredMixin, DetailView):
    template_name = 'employee/details.html'
    queryset = employeeDB.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk is None:
            return self.queryset.get(pk=pk)
            # return get_object_or_404(employeeDB, pk=pk)


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'employee/create.html'
    form_class = EmployeeForm
    success_url = '/employee/list/'

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk is None:
            return get_object_or_404(employeeDB, pk=pk)


class RegisterView(LoginRequiredMixin, CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = "/login/"

    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)