from django.contrib import admin
from app.models import *
from .models import User

# Register your models here.

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Membership_Applicants)
admin.site.register(Buyer_Applicants)
admin.site.register(Price_suggestion)
admin.site.register(Book)