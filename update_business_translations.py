#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation update script for My World Danışmanlık
This script updates the English and Russian translation files with appropriate translations.
"""

import re
import os


def update_translation_file(file_path, translations):
    """Update a .po file with new translations"""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update each translation
    for turkish, translation in translations.items():
        # Pattern to match msgid followed by empty msgstr
        pattern = rf'msgid "{re.escape(turkish)}"\nmsgstr ""'
        replacement = f'msgid "{turkish}"\nmsgstr "{translation}"'
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
        
        # Also update if msgstr already has content
        pattern = rf'(msgid "{re.escape(turkish)}"\nmsgstr ")[^"]*(")'
        replacement = rf'\1{translation}\2'
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# English translations
english_translations = {
    # Navigation and Common
    "Anasayfa": "Home",
    "Hizmetler": "Services", 
    "Hizmetlerimiz": "Our Services",
    "İletişim": "Contact",
    "Bize Ulaşın": "Contact Us",
    "Detaylar": "Details",
    "Hemen Başlayın": "Get Started Now",
    "İletişim Formu": "Contact Form",
    "Tüm Hizmetler": "All Services",
    
    # Business Name and Meta
    "My World Danışmanlık - Yabancılar İçin İkamet ve Çalışma İzni Danışmanlığı": "My World Consultancy - Residence and Work Permit Consultancy for Foreigners",
    "Yabancılar için profesyonel ikamet izni ve çalışma izni danışmanlık hizmetleri. Uzman rehberlik ile Türkiye'deki yasal süreçlerinizi kolaylaştırın.": "Professional residence permit and work permit consultancy services for foreigners. Simplify your legal processes in Turkey with expert guidance.",
    
    # Hero Section
    "Yabancılar İçin Profesyonel Danışmanlık Hizmetleri": "Professional Consultancy Services for Foreigners",
    "Türkiye'de yaşam ve çalışma hayalinizi gerçekleştirmek için güvenilir ortağınız. İkamet izni, çalışma izni, vatandaşlık ve sağlık sigortası konularında uzman danışmanlık.": "Your trusted partner to realize your dreams of living and working in Turkey. Expert consultancy on residence permits, work permits, citizenship and health insurance.",
    "Ücretsiz Danışmanlık Al": "Get Free Consultation",
    
    # Services
    "Türkiye'deki yasal süreçlerinizi kolaylaştırmak için kapsamlı danışmanlık çözümleri sunuyoruz.": "We offer comprehensive consultancy solutions to simplify your legal processes in Turkey.",
    "Çalışma İzni": "Work Permit",
    "Türkiye'de çalışma izni başvuru sürecinizde profesyonel destek alın.": "Get professional support in your work permit application process in Turkey.",
    "İkamet İzni": "Residence Permit", 
    "İkamet izni başvurusu, yenileme ve aile birleşimi süreçlerinde uzman yardımı.": "Expert assistance in residence permit application, renewal and family reunification processes.",
    "Vatandaşlık": "Citizenship",
    "Türk vatandaşlığı başvuru sürecinizde kapsamlı rehberlik hizmetleri.": "Comprehensive guidance services in your Turkish citizenship application process.",
    "Sağlık Sigortası": "Health Insurance",
    "Özel sağlık sigortası ve SGK işlemlerinizde danışmanlık hizmetleri.": "Consultancy services for private health insurance and social security procedures.",
    
    # Contact Information
    "İletişim Bilgileri": "Contact Information",
    "Hizmetlerimiz hakkında bilgi almak için bize ulaşın. Telefon ile hızlı danışmanlık alabilirsiniz.": "Contact us for information about our services. You can get quick consultation by phone.",
    "Türkçe Destek": "Turkish Support",
    "Türkiye telefon numarası": "Turkey phone number",
    "English Support": "English Support",
    "İngilizce telefon numarası": "English phone number",
    "Русская поддержка": "Russian Support", 
    "Rusça telefon numarası": "Russian phone number",
    "[Ofis adresi buraya gelecek]": "[Office address will be here]",
    
    # Services Page
    "Çalışma izni, ikamet izni, vatandaşlık ve sağlık sigortası danışmanlık hizmetleri. Yabancılar için profesyonel yasal destek.": "Work permit, residence permit, citizenship and health insurance consultancy services. Professional legal support for foreigners.",
    "Türkiye'deki yasal süreçlerinizde ihtiyacınız olan tüm danışmanlık hizmetlerini sunuyoruz.": "We provide all the consultancy services you need in your legal processes in Turkey.",
    "Türkiye'de çalışma izni almak için gereken tüm süreçlerde uzman desteği.": "Expert support in all processes required to obtain a work permit in Turkey.",
    "Çalışma İzni Başvurusu": "Work Permit Application",
    "İlk kez çalışma izni başvuru sürecinizde kapsamlı danışmanlık ve başvuru desteği.": "Comprehensive consultancy and application support in your first-time work permit application process.",
    "Çalışma İzni Yenileme": "Work Permit Renewal", 
    "Mevcut çalışma izninizin yenilenmesi için gerekli işlemler ve belge hazırlığı.": "Required procedures and document preparation for renewal of your existing work permit.",
    "İşveren Desteği": "Employer Support",
    "İşverenlere çalışma izni süreçlerinde danışmanlık ve yasal yükümlülükler konusunda bilgilendirme.": "Consultancy for employers on work permit processes and information on legal obligations.",
    "Türkiye'de yasal ikamet için gerekli tüm izin türlerinde profesyonel destek.": "Professional support for all types of permits required for legal residence in Turkey.",
    "Kısa Dönem İkamet İzni": "Short-Term Residence Permit",
    "Kısa süreli ikamet için başvuru süreçleri ve gerekli belge hazırlığı.": "Application processes and necessary document preparation for short-term residence.",
    "Uzun Dönem İkamet İzni": "Long-Term Residence Permit",
    "Uzun süreli ikamet izni başvurusu ve süreç yönetimi.": "Long-term residence permit application and process management.",
    "Aile Birleşimi": "Family Reunification",
    "Aile birleşimi kapsamında ikamet izni başvuru süreçleri.": "Residence permit application processes within the scope of family reunification.",
    "Türk vatandaşlığı başvuru süreçlerinde kapsamlı danışmanlık hizmetleri.": "Comprehensive consultancy services in Turkish citizenship application processes.",
    "Olağan Vatandaşlık": "Ordinary Citizenship",
    "Genel şartlara göre vatandaşlık başvuru süreçleri ve şart değerlendirmesi.": "Citizenship application processes and condition assessment according to general conditions.",
    "İstisnaî Vatandaşlık": "Exceptional Citizenship",
    "Özel durumlar için istisnaî vatandaşlık başvuru süreçleri.": "Exceptional citizenship application processes for special situations.",
    "Vatandaşlık Sınavı Hazırlığı": "Citizenship Exam Preparation",
    "Vatandaşlık sınavına hazırlık sürecinde danışmanlık ve kaynak desteği.": "Consultancy and resource support in the citizenship exam preparation process.",
    "Türkiye'de sağlık güvencesi için gerekli sigorta işlemlerinde danışmanlık.": "Consultancy on insurance procedures required for health security in Turkey.",
    "Özel Sağlık Sigortası": "Private Health Insurance",
    "Yabancılar için özel sağlık sigortası seçenekleri ve başvuru süreçleri.": "Private health insurance options and application processes for foreigners.",
    "SGK İşlemleri": "Social Security Procedures",
    "Sosyal Güvenlik Kurumu'na kayıt ve prim ödeme işlemlerinde destek.": "Support in registration and premium payment procedures to the Social Security Institution.",
    "Sağlık Güvence Belgesi": "Health Assurance Certificate", 
    "İkamet izni başvuruları için gerekli sağlık güvence belgesi işlemleri.": "Health assurance certificate procedures required for residence permit applications.",
    "Danışmanlık Almaya Hazır mısınız?": "Are You Ready for Consultation?",
    "Uzmanlarımızla görüşün ve yasal süreçlerinizde ilk adımı atın.": "Meet with our experts and take the first step in your legal processes.",
    
    # Contact Page
    "My World Danışmanlık ile iletişime geçin. Türkiye'deki yasal süreçlerinizde uzman desteği almak için arayın.": "Contact My World Consultancy. Call to get expert support in your legal processes in Turkey.",
    "Hizmetlerimiz hakkında bilgi almak ve danışmanlık sürecini başlatmak için bizimle iletişime geçin.": "Contact us to get information about our services and start the consultation process.",
    "Aşağıdaki iletişim bilgilerinden bizimle doğrudan iletişime geçebilirsiniz.": "You can contact us directly using the contact information below.",
    "Türkçe Destek Hattı": "Turkish Support Line",
    "Türkçe danışmanlık ve bilgi için": "For Turkish consultation and information",
    "English Support Line": "English Support Line",
    "For English consultation and information": "For English consultation and information",
    "Линия поддержки на русском": "Russian Support Line",
    "Для консультации и информации на русском языке": "For consultation and information in Russian",
    "Ofis Adresimiz": "Our Office Address",
    "[Şehir, Posta Kodu]": "[City, Postal Code]",
    "E-posta": "Email",
    "Genel bilgi ve sorularınız için": "For general information and your questions",
    "Çalışma Saatleri": "Working Hours",
    "Pazartesi - Cuma: 09:00 - 18:00": "Monday - Friday: 09:00 - 18:00",
    "Cumartesi: 10:00 - 16:00": "Saturday: 10:00 - 16:00",
    "Pazar: Kapalı": "Sunday: Closed",
    "Bize Mesaj Gönderin": "Send Us a Message",
    "Hızlı yanıt için telefon ile aramayı öneririz. Alternatif olarak aşağıdaki formu doldurabilirsiniz.": "We recommend calling by phone for a quick response. Alternatively, you can fill out the form below.",
    "Hemen Arayın!": "Call Now!",
    "Telefon ile direkt konuşarak en hızlı şekilde bilgi alın ve sürecinizi başlatın.": "Get information in the fastest way by talking directly on the phone and start your process.",
    
    # Form Fields  
    "Ad Soyad": "Full Name",
    "E-posta Adresiniz": "Your Email Address",
    "Telefon Numaranız (İsteğe bağlı)": "Your Phone Number (Optional)",
    "Konu": "Subject",
    "Mesajınız": "Your Message",
    "Mesaj Gönder": "Send Message",
    "Ad en az 2 karakter olmalıdır.": "Name must be at least 2 characters.",
    
    # Contact Model
    "Çalışma İzni": "Work Permit",
    "İkamet İzni": "Residence Permit", 
    "Vatandaşlık": "Citizenship",
    "Sağlık Sigortası": "Health Insurance",
    "Genel Danışma": "General Consultation",
    "Hizmet Türü": "Service Type",
    "Telefon": "Phone",
    "Mesaj": "Message",
    "Oluşturulma Tarihi": "Creation Date",
    "Yanıtlandı mı?": "Responded?",
    "İletişim Mesajı": "Contact Message",
    "İletişim Mesajları": "Contact Messages",
    
    # Footer
    "Yabancılar için ikamet ve çalışma izni danışmanlık hizmetlerinde güvenilir ortağınız. Göçmenlik yolculuğunuz boyunca uzman rehberlik ve destek sağlıyoruz.": "Your trusted partner in residence and work permit consultancy services for foreigners. We provide expert guidance and support throughout your immigration journey.",
    "Hızlı Bağlantılar": "Quick Links",
    "Tüm hakları saklıdır.": "All rights reserved.",
    "Gizlilik Politikası": "Privacy Policy",
    "Hizmet Şartları": "Terms of Service",
    
    # Messages
    "Mesajınız için teşekkürler! 24 saat içinde size dönüş yapacağız. Hızlı yanıt için telefon ile aramayı unutmayın.": "Thank you for your message! We will get back to you within 24 hours. Don't forget to call by phone for a quick response.",
    "Lütfen formdaki hataları düzeltin ve tekrar deneyin.": "Please correct the errors in the form and try again.",
    
    # Language/Country References
    "Türkçe": "Turkish",
    "English": "English", 
    "Русский": "Russian",
    "TR Telefon": "TR Phone",
    "EN Telefon": "EN Phone",
    "RU Telefon": "RU Phone",
}

# Russian translations
russian_translations = {
    # Navigation and Common
    "Anasayfa": "Главная",
    "Hizmetler": "Услуги",
    "Hizmetlerimiz": "Наши услуги", 
    "İletişim": "Контакты",
    "Bize Ulaşın": "Свяжитесь с нами",
    "Detaylar": "Подробности",
    "Hemen Başlayın": "Начать сейчас",
    "İletişim Formu": "Контактная форма",
    "Tüm Hizmetler": "Все услуги",
    
    # Business Name and Meta
    "My World Danışmanlık - Yabancılar İçin İkamet ve Çalışma İzni Danışmanlığı": "My World Консультации - Консультации по виду на жительство и разрешению на работу для иностранцев",
    "Yabancılar için profesyonel ikamet izni ve çalışma izni danışmanlık hizmetleri. Uzman rehberlik ile Türkiye'deki yasal süreçlerinizi kolaylaştırın.": "Профессиональные консультационные услуги по виду на жительство и разрешению на работу для иностранцев. Упростите свои правовые процессы в Турции с помощью экспертного руководства.",
    
    # Hero Section
    "Yabancılar İçin Profesyonel Danışmanlık Hizmetleri": "Профессиональные консультационные услуги для иностранцев",
    "Türkiye'de yaşam ve çalışma hayalinizi gerçekleştirmek için güvenilir ortağınız. İkamet izni, çalışma izni, vatandaşlık ve sağlık sigortası konularında uzman danışmanlık.": "Ваш надежный партнер для осуществления мечты о жизни и работе в Турции. Экспертные консультации по вопросам вида на жительство, разрешения на работу, гражданства и медицинского страхования.",
    "Ücretsiz Danışmanlık Al": "Получить бесплатную консультацию",
    
    # Services
    "Türkiye'deki yasal süreçlerinizi kolaylaştırmak için kapsamlı danışmanlık çözümleri sunuyoruz.": "Мы предлагаем комплексные консультационные решения для упрощения ваших правовых процессов в Турции.",
    "Çalışma İzni": "Разрешение на работу",
    "Türkiye'de çalışma izni başvuru sürecinizde profesyonel destek alın.": "Получите профессиональную поддержку в процессе подачи заявления на разрешение на работу в Турции.",
    "İkamet İzni": "Вид на жительство",
    "İkamet izni başvurusu, yenileme ve aile birleşimi süreçlerinde uzman yardımı.": "Экспертная помощь в процессах подачи заявления на вид на жительство, продления и воссоединения семьи.",
    "Vatandaşlık": "Гражданство",
    "Türk vatandaşlığı başvuru sürecinizde kapsamlı rehberlik hizmetleri.": "Комплексные услуги руководства в процессе подачи заявления на турецкое гражданство.",
    "Sağlık Sigortası": "Медицинское страхование",
    "Özel sağlık sigortası ve SGK işlemlerinizde danışmanlık hizmetleri.": "Консультационные услуги по частному медицинскому страхованию и процедурам социального обеспечения.",
    
    # Contact Information
    "İletişim Bilgileri": "Контактная информация",
    "Hizmetlerimiz hakkında bilgi almak için bize ulaşın. Telefon ile hızlı danışmanlık alabilirsiniz.": "Свяжитесь с нами для получения информации о наших услугах. Вы можете получить быструю консультацию по телефону.",
    "Türkçe Destek": "Поддержка на турецком",
    "Türkiye telefon numarası": "Номер телефона в Турции",
    "English Support": "Поддержка на английском",
    "İngilizce telefon numarası": "Номер телефона на английском",
    "Русская поддержка": "Поддержка на русском",
    "Rusça telefon numarası": "Номер телефона на русском",
    "[Ofis adresi buraya gelecek]": "[Здесь будет адрес офиса]",
    
    # Services Page
    "Çalışma izni, ikamet izni, vatandaşlık ve sağlık sigortası danışmanlık hizmetleri. Yabancılar için profesyonel yasal destek.": "Консультационные услуги по разрешению на работу, виду на жительство, гражданству и медицинскому страхованию. Профессиональная правовая поддержка для иностранцев.",
    "Türkiye'deki yasal süreçlerinizde ihtiyacınız olan tüm danışmanlık hizmetlerini sunuyoruz.": "Мы предоставляем все консультационные услуги, которые вам нужны в ваших правовых процессах в Турции.",
    "Türkiye'de çalışma izni almak için gereken tüm süreçlerde uzman desteği.": "Экспертная поддержка во всех процессах, необходимых для получения разрешения на работу в Турции.",
    "Çalışma İzni Başvurusu": "Заявление на разрешение на работу",
    "İlk kez çalışma izni başvuru sürecinizde kapsamlı danışmanlık ve başvuru desteği.": "Комплексные консультации и поддержка заявления в процессе вашего первого заявления на разрешение на работу.",
    "Çalışma İzni Yenileme": "Продление разрешения на работу",
    "Mevcut çalışma izninizin yenilenmesi için gerekli işlemler ve belge hazırlığı.": "Необходимые процедуры и подготовка документов для продления вашего существующего разрешения на работу.",
    "İşveren Desteği": "Поддержка работодателя",
    "İşverenlere çalışma izni süreçlerinde danışmanlık ve yasal yükümlülükler konusunda bilgilendirme.": "Консультации для работодателей по процессам разрешения на работу и информирование о правовых обязательствах.",
    "Türkiye'de yasal ikamet için gerekli tüm izin türlerinde profesyonel destek.": "Профессиональная поддержка по всем типам разрешений, необходимых для легального проживания в Турции.",
    "Kısa Dönem İkamet İzni": "Краткосрочный вид на жительство",
    "Kısa süreli ikamet için başvuru süreçleri ve gerekli belge hazırlığı.": "Процессы подачи заявления и подготовка необходимых документов для краткосрочного проживания.",
    "Uzun Dönem İkamet İzni": "Долгосрочный вид на жительство",
    "Uzun süreli ikamet izni başvurusu ve süreç yönetimi.": "Заявление на долгосрочный вид на жительство и управление процессом.",
    "Aile Birleşimi": "Воссоединение семьи",
    "Aile birleşimi kapsamında ikamet izni başvuru süreçleri.": "Процессы подачи заявления на вид на жительство в рамках воссоединения семьи.",
    "Türk vatandaşlığı başvuru süreçlerinde kapsamlı danışmanlık hizmetleri.": "Комплексные консультационные услуги в процессах подачи заявления на турецкое гражданство.",
    "Olağan Vatandaşlık": "Обычное гражданство",
    "Genel şartlara göre vatandaşlık başvuru süreçleri ve şart değerlendirmesi.": "Процессы подачи заявления на гражданство и оценка условий согласно общим условиям.",
    "İstisnaî Vatandaşlık": "Исключительное гражданство",
    "Özel durumlar için istisnaî vatandaşlık başvuru süreçleri.": "Процессы подачи заявления на исключительное гражданство для особых случаев.",
    "Vatandaşlık Sınavı Hazırlığı": "Подготовка к экзамену на гражданство",
    "Vatandaşlık sınavına hazırlık sürecinde danışmanlık ve kaynak desteği.": "Консультации и поддержка ресурсов в процессе подготовки к экзамену на гражданство.",
    "Türkiye'de sağlık güvencesi için gerekli sigorta işlemlerinde danışmanlık.": "Консультации по страховым процедурам, необходимым для медицинского обеспечения в Турции.",
    "Özel Sağlık Sigortası": "Частное медицинское страхование",
    "Yabancılar için özel sağlık sigortası seçenekleri ve başvuru süreçleri.": "Варианты частного медицинского страхования и процессы подачи заявлений для иностранцев.",
    "SGK İşlemleri": "Процедуры социального обеспечения",
    "Sosyal Güvenlik Kurumu'na kayıt ve prim ödeme işlemlerinde destek.": "Поддержка в процедурах регистрации и уплаты взносов в Институт социального обеспечения.",
    "Sağlık Güvence Belgesi": "Справка о медицинском обеспечении",
    "İkamet izni başvuruları için gerekli sağlık güvence belgesi işlemleri.": "Процедуры получения справки о медицинском обеспечении, необходимой для заявлений на вид на жительство.",
    "Danışmanlık Almaya Hazır mısınız?": "Готовы к консультации?",
    "Uzmanlarımızla görüşün ve yasal süreçlerinizde ilk adımı atın.": "Встретьтесь с нашими экспертами и сделайте первый шаг в ваших правовых процессах.",
    
    # Contact Page
    "My World Danışmanlık ile iletişime geçin. Türkiye'deki yasal süreçlerinizde uzman desteği almak için arayın.": "Свяжитесь с My World Консультации. Звоните, чтобы получить экспертную поддержку в ваших правовых процессах в Турции.",
    "Hizmetlerimiz hakkında bilgi almak ve danışmanlık sürecini başlatmak için bizimle iletişime geçin.": "Свяжитесь с нами, чтобы получить информацию о наших услугах и начать процесс консультации.",
    "Aşağıdaki iletişim bilgilerinden bizimle doğrudan iletişime geçebilirsiniz.": "Вы можете связаться с нами напрямую, используя контактную информацию ниже.",
    "Türkçe Destek Hattı": "Линия поддержки на турецком",
    "Türkçe danışmanlık ve bilgi için": "Для консультаций и информации на турецком языке",
    "English Support Line": "Линия поддержки на английском",
    "For English consultation and information": "Для консультаций и информации на английском языке",
    "Линия поддержки на русском": "Линия поддержки на русском",
    "Для консультации и информации на русском языке": "Для консультации и информации на русском языке",
    "Ofis Adresimiz": "Адрес нашего офиса",
    "[Şehir, Posta Kodu]": "[Город, Почтовый индекс]",
    "E-posta": "Электронная почта",
    "Genel bilgi ve sorularınız için": "Для общей информации и ваших вопросов",
    "Çalışma Saatleri": "Рабочие часы",
    "Pazartesi - Cuma: 09:00 - 18:00": "Понедельник - Пятница: 09:00 - 18:00",
    "Cumartesi: 10:00 - 16:00": "Суббота: 10:00 - 16:00",
    "Pazar: Kapalı": "Воскресенье: Закрыто",
    "Bize Mesaj Gönderin": "Отправьте нам сообщение",
    "Hızlı yanıt için telefon ile aramayı öneririz. Alternatif olarak aşağıdaki formu doldurabilirsiniz.": "Мы рекомендуем звонить по телефону для быстрого ответа. В качестве альтернативы вы можете заполнить форму ниже.",
    "Hemen Arayın!": "Звоните сейчас!",
    "Telefon ile direkt konuşarak en hızlı şekilde bilgi alın ve sürecinizi başlatın.": "Получите информацию самым быстрым способом, говоря напрямую по телефону, и начните свой процесс.",
    
    # Form Fields
    "Ad Soyad": "Полное имя",
    "E-posta Adresiniz": "Ваш адрес электронной почты",
    "Telefon Numaranız (İsteğe bağlı)": "Ваш номер телефона (Необязательно)",
    "Konu": "Тема",
    "Mesajınız": "Ваше сообщение",
    "Mesaj Gönder": "Отправить сообщение",
    "Ad en az 2 karakter olmalıdır.": "Имя должно содержать не менее 2 символов.",
    
    # Contact Model
    "Çalışma İzni": "Разрешение на работу",
    "İkamet İzni": "Вид на жительство",
    "Vatandaşlık": "Гражданство",
    "Sağlık Sigortası": "Медицинское страхование",
    "Genel Danışma": "Общая консультация",
    "Hizmet Türü": "Тип услуги",
    "Telefon": "Телефон",
    "Mesaj": "Сообщение",
    "Oluşturulma Tarihi": "Дата создания",
    "Yanıtlandı mı?": "Отвечено?",
    "İletişim Mesajı": "Контактное сообщение",
    "İletişim Mesajları": "Контактные сообщения",
    
    # Footer
    "Yabancılar için ikamet ve çalışma izni danışmanlık hizmetlerinde güvenilir ortağınız. Göçmenlik yolculuğunuz boyunca uzman rehberlik ve destek sağlıyoruz.": "Ваш надежный партнер в консультационных услугах по виду на жительство и разрешению на работу для иностранцев. Мы обеспечиваем экспертное руководство и поддержку на протяжении всего вашего иммиграционного пути.",
    "Hızlı Bağlantılar": "Быстрые ссылки",
    "Tüm hakları saklıdır.": "Все права защищены.",
    "Gizlilik Politikası": "Политика конфиденциальности",
    "Hizmet Şartları": "Условия предоставления услуг",
    
    # Messages
    "Mesajınız için teşekkürler! 24 saat içinde size dönüş yapacağız. Hızlı yanıt için telefon ile aramayı unutmayın.": "Спасибо за ваше сообщение! Мы свяжемся с вами в течение 24 часов. Не забывайте звонить по телефону для быстрого ответа.",
    "Lütfen formdaki hataları düzeltin ve tekrar deneyin.": "Пожалуйста, исправьте ошибки в форме и попробуйте снова.",
    
    # Language/Country References
    "Türkçe": "Турецкий",
    "English": "Английский",
    "Русский": "Русский",
    "TR Telefon": "TR Телефон",
    "EN Telefon": "EN Телефон", 
    "RU Telefon": "RU Телефон",
}

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Update English translations
    en_file = os.path.join(base_dir, 'locale/en/LC_MESSAGES/django.po')
    if os.path.exists(en_file):
        print("Updating English translations...")
        update_translation_file(en_file, english_translations)
        print("English translations updated successfully!")
    else:
        print(f"English translation file not found: {en_file}")
    
    # Update Russian translations  
    ru_file = os.path.join(base_dir, 'locale/ru/LC_MESSAGES/django.po')
    if os.path.exists(ru_file):
        print("Updating Russian translations...")
        update_translation_file(ru_file, russian_translations)
        print("Russian translations updated successfully!")
    else:
        print(f"Russian translation file not found: {ru_file}")
    
    print("All translations updated!")

if __name__ == "__main__":
    main()
