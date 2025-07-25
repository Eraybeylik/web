from django.db import models
from django.utils import timezone


class Contact(models.Model):
    """Model to store contact form submissions"""
    
    INQUIRY_TYPES = [
        ('work_permit', 'Work Permit'),
        ('residence_permit', 'Residence Permit'),
        ('general', 'General Inquiry'),
        ('consultation', 'Consultation Request'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES, default='general')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_responded = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
