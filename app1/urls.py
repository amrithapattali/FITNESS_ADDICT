from django import urls
from django.urls import path
from .views import PlanListView,PlanDetailView,EquipmentListView,EquipmentDetailView,HomePageView,MyProfileView,ContactPageView,AboutPageView,EditProfile,CreateProfile,CreateEnquiry

urlpatterns = [
    path('list',PlanListView.as_view(), name='list'),
    path('details/<int:pk>/',PlanDetailView.as_view(), name='details'),
    path('list1',EquipmentListView.as_view(), name='list1'),
    path('details1/<int:pk>/',EquipmentDetailView.as_view(), name='details1'),
    path('home',HomePageView.as_view(), name='home'),
    path('myprofile/', MyProfileView.as_view(), name='myprofile'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('create/', CreateProfile.as_view(), name='create'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit'),
    path('enquiry/', CreateEnquiry.as_view(), name='enquiry'),

    ]