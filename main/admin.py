from django.contrib import admin
from .models import (
    Profile,
    Project,
    Education,
    Certification,
    Internship,
    Contact,
    Resume,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "linkedin", "github")
    search_fields = ("name", "title", "bio")

    fields = (
        "name",
        "title",
        "photo",
        "linkedin",
        "github",
        "bio",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "year", "cgpa")
    search_fields = ("degree", "institution")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "year")
    search_fields = ("title", "provider")


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ("company", "role")
    search_fields = ("company", "role")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    readonly_fields = ("created_at",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("uploaded_at", "file")
    readonly_fields = ("uploaded_at",)