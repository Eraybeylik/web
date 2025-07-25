from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
from .forms import ContactForm
from .models import Contact


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
            #         subject=f'Yeni İletişim Formu: {contact_message.subject}',
            #         message=f'''
            #         Ad: {contact_message.name}
            #         Email: {contact_message.email}
            #         Telefon: {contact_message.phone}
            #         Hizmet Türü: {contact_message.get_inquiry_type_display()}
            #         Konu: {contact_message.subject}
            #         Mesaj: {contact_message.message}
            #         ''',
            #         from_email=settings.DEFAULT_FROM_EMAIL,
            #         recipient_list=['info@myworlddanismanlik.com'],
            #         fail_silently=True,
            #     )
            # except Exception as e:
            #     pass  # Handle email sending errors gracefully
            
            # Redirect back to contact page with success message
            return redirect('contact')
        else:
            messages.error(
                request, 
                _('Lütfen formdaki hataları düzeltin ve tekrar deneyin.')
            )
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})
