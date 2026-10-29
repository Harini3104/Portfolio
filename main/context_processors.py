from .models import Resume


def portfolio_data(request):
    resume = Resume.objects.last()

    return {
        "resume": resume,
    }
