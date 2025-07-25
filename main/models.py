from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    """Model to store contact form submissions"""
    
    INQUIRY_TYPES = [
        ('calisma_izni', _('Çalışma İzni')),
        ('ikamet_izni', _('İkamet İzni')),
        ('vatandaslik', _('Vatandaşlık')),
        ('saglik_sigortasi', _('Sağlık Sigortası')),
        ('genel', _('Genel Danışma')),
    ]
    
    name = models.CharField(_('Ad Soyad'), max_length=100)
    email = models.EmailField(_('E-posta'))
    phone = models.CharField(_('Telefon'), max_length=20, blank=True)
    inquiry_type = models.CharField(_('Hizmet Türü'), max_length=20, choices=INQUIRY_TYPES, default='genel')
    subject = models.CharField(_('Konu'), max_length=200)
    message = models.TextField(_('Mesaj'))
    created_at = models.DateTimeField(_('Oluşturulma Tarihi'), default=timezone.now)
    is_responded = models.BooleanField(_('Yanıtlandı mı?'), default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = _('İletişim Mesajı')
        verbose_name_plural = _('İletişim Mesajları')
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
