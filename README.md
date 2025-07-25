# Permit Consultancy Website

A professional Django website for a consultancy company specializing in work permit and residence permit services. The website features a modern, responsive design with a blue-toned color scheme and comprehensive functionality for client engagement.

## Features

### 🏠 **Homepage**
- Professional hero section with call-to-action
- Services overview with interactive cards
- Company statistics and achievements
- Step-by-step process explanation
- Client testimonials and success stories

### 🔧 **Services Page**
- Detailed work permit services information
- Comprehensive residence permit solutions
- Expert consultation offerings
- Transparent pricing packages
- FAQ section with common questions

### 📧 **Contact System**
- Professional contact form with validation
- Multiple inquiry types (Work Permit, Residence Permit, etc.)
- Contact information and business hours
- Office location with map placeholder
- Success page with next steps information

### 👨‍💼 **Admin Panel**
- Django admin integration for managing contact submissions
- Contact message tracking with response status
- User-friendly admin interface with filtering and search
- Secure access for staff members

### 🎨 **Design Features**
- Modern, professional blue-toned design
- Fully responsive and mobile-friendly
- Semantic HTML5 structure
- CSS Grid and Flexbox layouts
- Font Awesome icons integration
- Smooth animations and transitions

## Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **Icons**: Font Awesome 6.0
- **Styling**: Custom CSS with CSS variables

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 1. Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd permit-consultancy

# Or extract the downloaded files to your desired directory
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```
Or use the pre-created admin user:
- Username: `admin`
- Email: `admin@permitconsultancy.com`
- Password: `admin123`

### 6. Run Development Server
```bash
python manage.py runserver
```

The website will be available at: `http://127.0.0.1:8000/`

## Usage

### Accessing the Website
- **Homepage**: `http://127.0.0.1:8000/`
- **Services**: `http://127.0.0.1:8000/services/`
- **Contact**: `http://127.0.0.1:8000/contact/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### Contact Form Features
- **Name**: Required field for client identification
- **Email**: Required field with email validation
- **Phone**: Optional phone number field
- **Inquiry Type**: Dropdown selection (Work Permit, Residence Permit, General Inquiry, Consultation Request)
- **Subject**: Required subject line
- **Message**: Required detailed message field

### Admin Panel Features
- View all contact form submissions
- Filter messages by inquiry type, response status, and date
- Search through messages by name, email, subject, or content
- Mark messages as responded
- Professional contact management interface

## Project Structure

```
permit_consultancy/
├── main/                   # Main Django app
│   ├── models.py          # Contact model
│   ├── forms.py           # Contact form
│   ├── views.py           # View functions
│   ├── urls.py            # App URL patterns
│   ├── admin.py           # Admin configuration
│   └── migrations/        # Database migrations
├── permit_consultancy/     # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   └── main/              # App-specific templates
│       ├── home.html      # Homepage
│       ├── services.html  # Services page
│       ├── contact.html   # Contact page
│       └── contact_success.html  # Success page
├── static/                # Static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/                # JavaScript files
│   └── images/            # Image assets
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Customization

### Styling
- Edit `static/css/style.css` to modify the design
- CSS variables in `:root` allow easy color scheme changes
- Responsive breakpoints can be adjusted in media queries

### Content
- Update company information in templates
- Modify contact details in `templates/base.html`
- Customize service offerings in `templates/main/services.html`

### Functionality
- Add new form fields in `main/models.py` and `main/forms.py`
- Extend admin functionality in `main/admin.py`
- Add new pages by creating views, templates, and URL patterns

## Deployment Considerations

For production deployment:

1. **Security Settings**
   - Change `SECRET_KEY` in settings
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`

2. **Database**
   - Switch to PostgreSQL or MySQL
   - Configure database settings

3. **Static Files**
   - Configure `STATIC_ROOT` for production
   - Set up static file serving

4. **Email Configuration**
   - Configure email backend for contact form notifications
   - Uncomment email sending code in views.py

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is created for educational and professional use. Please respect any licensing requirements for included assets and fonts.

## Support

For questions or issues with the website:
- Check the Django documentation
- Review the code comments for guidance
- Test the contact form functionality
- Verify admin panel access

---

**Note**: This is a demonstration website. For production use, ensure proper security measures, database configuration, and hosting setup are implemented.