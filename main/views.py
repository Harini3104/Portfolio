from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Contact
from .models import Project, Education,Internship,Certification
from .forms import ContactForm
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # redirect to same page or success page
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})


def home(request):
    return render(request, 'home.html')
def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})

def education_certifications(request):
    education = Education.objects.all()
    certifications = Certification.objects.all()
    internships = Internship.objects.all()

    return render(request, "education.html", {
        "education": education,
        "certifications": certifications,
        "internships": internships
    })

def Contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save in database (so visible in admin)
        Contact.objects.create(name=name, email=email, message=message)

        # Send to Gmail
        full_message = f"Message from {name} ({email}):\n\n{message}"
        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        return redirect("success")

    return render(request, "contact.html")