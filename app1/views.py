from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView,UpdateView,CreateView
from .models import Plan, Equipment, MyProfile, Enquiry


class HomePageView(TemplateView):
    template_name = 'home.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class PlanListView(ListView):
    model = Plan
    template_name = 'list.html'


class PlanDetailView(DetailView):
    model = Plan
    template_name = 'detail.html'


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'list1.html'


class EquipmentDetailView(ListView):
    model = Equipment
    template_name = 'detail1.html'


class MyProfileView(ListView):
    model = MyProfile
    context_object_name = 'myprofile'
    template_name = 'myprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myprofile'] = context['myprofile'].filter(user=self.request.user)
        return context

class CreateProfile(CreateView):
    model = MyProfile
    fields = '__all__'
    success_url = reverse_lazy('myprofile')
    template_name = 'editprofile.html'


class EditProfile(UpdateView):
    model = MyProfile
    fields = '__all__'
    success_url = reverse_lazy('myprofile')
    template_name = 'editprofile.html'

# class TaskDelete(DeleteView):
#     model = MyProfile
#     success_url = reverse_lazy('myprofile')
#     template_name = 'plandelete.html'

class CreateEnquiry(CreateView):
    model = Enquiry
    fields = '__all__'
    context_object_name = 'enquiry'
    success_url = reverse_lazy('home')
    template_name = 'enquiry.html'

