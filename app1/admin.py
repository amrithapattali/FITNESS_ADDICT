from django.contrib import admin

# Register your models here.
from .models import Plan, Equipment, Member, MyProfile, Enquiry

admin.site.register(Plan)
admin.site.register(Equipment)
admin.site.register(Member)
admin.site.register(MyProfile)
admin.site.register(Enquiry)
