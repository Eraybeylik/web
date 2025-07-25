from django.shortcuts import render


def home(request):
    """Homepage view"""
    return render(request, 'main/home.html')


def services(request):
    """Services page view"""
    return render(request, 'main/services.html')


def service_work_permit(request):
    """Work permit detailed service page"""
    return render(request, 'services/work_permit.html')


def service_residence_permit(request):
    """Residence permit detailed service page"""
    return render(request, 'services/residence_permit.html')


def service_citizenship(request):
    """Citizenship detailed service page"""
    return render(request, 'services/citizenship.html')


def contact(request):
    """Contact page view - simplified without form"""
    return render(request, 'main/contact.html')
