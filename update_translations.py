#!/usr/bin/env python
"""
Script to update translation files with appropriate translations
"""

import os
import re

def update_english_translations():
    """Update English translation file with appropriate translations"""
    
    en_po_path = "/home/xera/Documents/web/locale/en/LC_MESSAGES/django.po"
    
    # Dictionary of Turkish to English translations
    translations = {
        # Home page content
        "Çeşitli ülkeler ve vize kategorileri için çalışma izni başvurularında uzman yardım. Karmaşık evrak işlerini üstlenir ve her adımda size rehberlik ederiz.": "Expert assistance with work permit applications for various countries and visa categories. We handle the complex paperwork and guide you through every step.",
        "Daha Fazla Bilgi": "Learn More",
        "İkamet izni başvuruları, yenilemeler ve aile birleşimi süreçleri için kapsamlı destek. Yeni ülkenizi eviniz gibi hissettirin.": "Complete support for residence permit applications, renewals, and family reunification processes. Make your new country feel like home.",
        "Uygunluğunuzu değerlendirmek, belgelerinizi incelemek ve göçmenlik hedefleriniz için stratejik bir plan oluşturmak için kişiselleştirilmiş danışmanlık seansları.": "Personalized consultation sessions to assess your eligibility, review documents, and create a strategic plan for your immigration goals.",
        "Randevu Al": "Book Consultation",
        "Neden Hizmetlerimizi Seçmelisiniz?": "Why Choose Our Services?",
        "Yıllarca deneyim ve mükemmellik taahhüdü ile göçmenlik hedeflerinize ulaşmanızda güvenilir ortağınızız.": "With years of experience and a commitment to excellence, we're your trusted partner in achieving your immigration goals.",
        "Yüksek Başarı Oranı": "High Success Rate",
        "Dikkatli hazırlık ve süreç boyunca uzman rehberlik ile izin başvurularında %95'in üzerinde başarı oranı.": "Over 95% success rate in permit applications with careful preparation and expert guidance throughout the process.",
        "Hızlı İşlem": "Fast Processing",
        "Bekleme sürelerini en aza indirmek ve başvurularınızı hızlandırmak için akıcı süreçler ve verimli belge hazırlığı.": "Streamlined processes and efficient document preparation to minimize waiting times and expedite your applications.",
        "Güvenli ve Gizli": "Secure & Confidential",
        "Kişisel bilgileriniz ve belgeleriniz en yüksek güvenlik ve gizlilik düzeyinde işlenir.": "Your personal information and documents are handled with the highest level of security and confidentiality.",
        "Başarı Geçmişimiz": "Our Track Record",
        "Uzmanlığımızı ve müşteri başarısına olan bağlılığımızı anlatan rakamlar.": "Numbers that speak for our expertise and commitment to client success.",
        "Başarılı Başvurular": "Successful Applications",
        "Başarıyla işlenen izin ve vizeler": "Permits and visas successfully processed",
        "Başarı Oranı": "Success Rate",
        "İlk denemede onaylanan başvurular": "Of applications approved on first attempt",
        "Yıllık Deneyim": "Years Experience",
        "Göçmenlik ve izin hizmetlerinde": "In immigration and permit services",
        "Nasıl Çalışıyoruz": "How We Work",
        "Göçmenlik yolculuğunuzu mümkün olduğunca kolay hale getirmek için tasarlanmış şeffaf, adım adım bir süreç.": "A transparent, step-by-step process designed to make your immigration journey as smooth as possible.",
        "İlk Danışmanlık": "Initial Consultation",
        "Durumunuzu değerlendiriyoruz, hedeflerinizi tartışıyoruz ve özel ihtiyaçlarınız için en iyi göçmenlik yolunu belirliyoruz.": "We assess your situation, discuss your goals, and determine the best immigration pathway for your specific needs.",
        "Belge Hazırlığı": "Document Preparation",
        "Gerekli tüm belgeleri toplama, düzenleme ve hazırlama konusunda size yardımcı oluyoruz, başvurunuzun tüm gereksinimleri karşıladığından emin oluyoruz.": "We help you gather, organize, and prepare all required documents to ensure your application meets all requirements.",
        "Başvuru Gönderimi": "Application Submission",
        "Başvurunuzu gönderiyoruz ve ilerlemesini takip ediyoruz, onaylanana kadar her adımda sizi bilgilendiryoruz.": "We submit your application and monitor its progress, keeping you informed every step of the way until approval.",
        "Göçmenlik Yolculuğunuza Başlamaya Hazır mısınız?": "Ready to Start Your Immigration Journey?",
        "Karmaşık göçmenlik süreçlerinin sizi engellemesine izin vermeyin. Bugün bir danışmanlık için bizimle iletişime geçin ve göçmenlik hedeflerinize ulaşmak için ilk adımı atın.": "Don't let complex immigration processes hold you back. Contact us today for a consultation and take the first step towards achieving your immigration goals.",
        "Danışmanlık Randevusu": "Schedule Consultation",
        "Tüm Hizmetleri Görüntüle": "View All Services",
        
        # Contact page content
        "Type of Inquiry": "Type of Inquiry",
        "Get in Touch": "Get in Touch",
        "Our team of immigration experts is here to help you navigate the complex world of permits and visas. Contact us using any of the methods below.": "Our team of immigration experts is here to help you navigate the complex world of permits and visas. Contact us using any of the methods below.",
        
        # Services page content
        "Hizmetlerimiz - İzin Danışmanlığı": "Our Services - Permit Consultancy",
        "Kapsamlı çalışma izni ve ikamet izni hizmetleri. Uzman vize danışmanlığı, belge incelemesi ve tüm göçmenlik ihtiyaçlarınız için başvuru desteği.": "Comprehensive work permit and residence permit services. Expert visa consultation, document review, and application support for all your immigration needs.",
        "Profesyonel Göçmenlik Hizmetleri": "Professional Immigration Services",
        "Tüm çalışma izni, ikamet izni ve vize danışmanlığı ihtiyaçlarınız için kapsamlı çözümler. Uzmanlarımızın karmaşık göçmenlik dünyasında size rehberlik etmesine izin verin.": "Comprehensive solutions for all your work permit, residence permit, and visa consultation needs. Let our experts guide you through the complex world of immigration.",
        "Çalışma İzni Hizmetleri": "Work Permit Services",
        "Çeşitli ülkeler ve istihdam kategorileri için çalışma izni başvurularında uzman yardım.": "Expert assistance with work permit applications for various countries and employment categories.",
    }
    
    # Read the file
    with open(en_po_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update translations
    for turkish, english in translations.items():
        # Find the msgid and replace empty msgstr
        pattern = re.compile(
            r'(msgid\s+"' + re.escape(turkish) + r'"\s*\n)msgstr\s+""',
            re.MULTILINE | re.DOTALL
        )
        replacement = r'\1msgstr "' + english + '"'
        content = pattern.sub(replacement, content)
    
    # Write the updated content back
    with open(en_po_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("English translations updated successfully!")

def update_russian_translations():
    """Update Russian translation file with appropriate translations"""
    
    ru_po_path = "/home/xera/Documents/web/locale/ru/LC_MESSAGES/django.po"
    
    # Dictionary of Turkish to Russian translations
    translations = {
        # Basic navigation
        "İzin Danışmanlığı": "Консультации по разрешениям",
        "Anasayfa": "Главная",
        "Hizmetler": "Услуги",
        "İletişim": "Контакты",
        
        # Home page content
        "Uzman İkamet ve Vize Danışmanlığı Hizmetleri": "Экспертные услуги по консультированию по проживанию и визам",
        "Göçmenlik sürecinizde güvenle ilerleyin. Çalışma izni, ikamet izni ve vize başvurularında uzman rehberlik sunuyoruz.": "Уверенно продвигайтесь в своем иммиграционном процессе. Мы предоставляем экспертное руководство по разрешениям на работу, видам на жительство и визовым заявлениям.",
        "Uzman Danışmanlık Alın": "Получить экспертную консультацию",
        "Profesyonel Hizmetlerimiz": "Наши профессиональные услуги",
        "Size özel tasarlanmış kapsamlı göçmenlik çözümleri. İlk danışmanlıktan başarılı başvuru onayına kadar.": "Комплексные иммиграционные решения, адаптированные под ваши потребности. От первичной консультации до успешного одобрения заявления.",
        "Çalışma İzinleri": "Разрешения на работу",
        "İkamet İzinleri": "Виды на жительство",
        "Uzman Danışmanlık": "Экспертная консультация",
        "Daha Fazla Bilgi": "Подробнее",
        "Randevu Al": "Записаться на прием",
        
        # Footer content
        "Çalışma izni ve ikamet izni hizmetleri için güvenilir ortağınız. Göçmenlik yolculuğunuz boyunca uzman rehberlik ve destek sağlıyoruz.": "Ваш надежный партнер в услугах разрешений на работу и видов на жительство. Мы предоставляем экспертное руководство и поддержку на протяжении всего вашего иммиграционного пути.",
        "Hızlı Bağlantılar": "Быстрые ссылки",
        "Hizmetlerimiz": "Наши услуги",
        "Bize Ulaşın": "Связаться с нами",
        "Hakkımızda": "О нас",
        "Referanslar": "Отзывы",
        "Vize Danışmanlığı": "Визовая консультация",
        "Belge İncelemesi": "Обзор документов",
        "Başvuru Desteği": "Поддержка заявлений",
        "İletişim Bilgileri": "Контактная информация",
        "123 İş Merkezi": "123 Бизнес-центр",
        "Profesyonel Şehir, PS 12345": "Профессиональный город, ПГ 12345",
        "Pzt-Cum: 09:00 - 18:00": "Пн-Пт: 09:00 - 18:00",
        "Cmt: 10:00 - 16:00": "Сб: 10:00 - 16:00",
        "İzin Danışmanlık Hizmetleri. Tüm hakları saklıdır.": "Консультационные услуги по разрешениям. Все права защищены.",
        "Gizlilik Politikası": "Политика конфиденциальности",
        "Hizmet Şartları": "Условия обслуживания",
        
        # Contact page
        "İletişim - İzin Danışmanlığı": "Контакты - Консультации по разрешениям",
        "Göçmenlik Uzmanlarımızla İletişime Geçin": "Свяжитесь с нашими экспертами по иммиграции",
        "Bize Mesaj Gönderin": "Отправьте нам сообщение",
        "Aşağıdaki formu doldurun, size 24 saat içinde geri döneceğiz.": "Заполните форму ниже, и мы свяжемся с вами в течение 24 часов.",
        
        # Contact success page
        "Teşekkürler - İzin Danışmanlığı": "Спасибо - Консультации по разрешениям",
        "Bize Ulaştığınız İçin Teşekkürler!": "Спасибо, что связались с нами!",
        "Bundan Sonra Ne Olacak?": "Что происходит дальше?",
    }
    
    # Read the file
    with open(ru_po_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update translations
    for turkish, russian in translations.items():
        # Find the msgid and replace empty msgstr
        pattern = re.compile(
            r'(msgid\s+"' + re.escape(turkish) + r'"\s*\n)msgstr\s+""',
            re.MULTILINE | re.DOTALL
        )
        replacement = r'\1msgstr "' + russian + '"'
        content = pattern.sub(replacement, content)
    
    # Write the updated content back
    with open(ru_po_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Russian translations updated successfully!")

if __name__ == "__main__":
    update_english_translations()
    update_russian_translations()
    print("All translations updated!")
