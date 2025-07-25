from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact


def home(request):
    """Homepage view"""
    return render(request, 'main/home.html')


def services(request):
    """Services page view"""
    return render(request, 'main/services.html')


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            # Add success message
            messages.success(
                request, 
                'Thank you for your message! We will get back to you within 24 hours.'
            )
            
            # Optionally send email notification (uncomment if email is configured)
            # try:
            #     send_mail(
            #         subject=f'New Contact Form Submission: {contact_message.subject}',
            #         message=f'''
            #         Name: {contact_message.name}
            #         Email: {contact_message.email}
            #         Phone: {contact_message.phone}
            #         Inquiry Type: {contact_message.get_inquiry_type_display()}
            #         Subject: {contact_message.subject}
            #         Message: {contact_message.message}
            #         ''',
            #         from_email=settings.DEFAULT_FROM_EMAIL,
            #         recipient_list=['admin@permitconsultancy.com'],
            #         fail_silently=True,
            #     )
            # except Exception as e:
            #     pass  # Handle email sending errors gracefully
            
            return redirect('contact_success')
        else:
            messages.error(
                request, 
                'Please correct the errors below and try again.'
            )
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})


def contact_success(request):
    """Contact form success page"""
    return render(request, 'main/contact_success.html')
