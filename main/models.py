from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profile/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=200)       # e.g., B.E. Electronics & Communication
    institution = models.CharField(max_length=200)  # e.g., ABC College
    year = models.CharField(max_length=20)          # e.g., 2021–2025
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)  # e.g., 8.5

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Certification(models.Model):
    title = models.CharField(max_length=200)        # e.g., Python for Everybody
    provider = models.CharField(max_length=200)     # e.g., Coursera / NPTEL
    year = models.CharField(max_length=20, blank=True, null=True)  # e.g., 2024

    def __str__(self):
        return self.title
class Internship(models.Model):
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.role}"
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"