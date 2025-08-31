from django.contrib import admin
from .models import Profile,Project, Education,Certification,Internship, Contact
admin.site.register(Project)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "year", "cgpa")
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "year")
admin.site.register(Contact)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Internship)