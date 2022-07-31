from django.contrib import admin

# Register your models here.
from mysite.models import User,Sregister,Tregister

admin.site.register(User)

class RecruiterFilter(admin.ModelAdmin):
    list_display=['username','subject','ctaught','idno','contact','password'] # used to display the table columns
    list_display_links=['idno'] # used to display the elements trough links
    list_editable=['username','subject','ctaught','contact','password'] # table columns to edit
    list_filter=['username','contact'] # used to filter the table with the column name
admin.site.register(Tregister,RecruiterFilter)

class StudentFilter(admin.ModelAdmin):
    list_display=['sname','rollno','standard','stream','pass1']
    list_display_links=['stream']
    list_editable=['sname','rollno','standard','pass1']
    list_filter=['sname','rollno']
admin.site.register(Sregister,StudentFilter)
