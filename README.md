
# Ziply Dilevery - Parcel Tracking System

A Django-based REST API for parcel tracking using MongoDB as the database backend. Built for efficient package management and real-time tracking capabilities.

## Features

- **Parcel Management**: Create, track, and manage parcels through REST API
- **MongoDB Integration**: NoSQL database with optimized indexes for performance
- **Real-time Tracking**: Complete status history for each parcel
- **Health Monitoring**: Built-in health check endpoints
- **Geographic Optimization**: Location-based queries for delivery routing

## Technology Stack

- **Backend**: Django 5.2.8 with Django REST Framework
- **Database**: MongoDB with Djongo ORM bridge
- **API**: RESTful JSON API
- **Environment**: Python 3.14+

## Quick Start

### Prerequisites

- Python 3.14 or higher
- MongoDB instance (local or cloud)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/High-Level-Prgrmng-Languages/ziply-delivery-service
cd ziply-delivery-service
```

2. **Create virtual environment**
```bash
python3.14 -m venv myproject-env
# Alternative: python -m venv myproject-env
source myproject-env/bin/activate  
```

3. **Install dependencies**
```bash
pip install -r src/requirements.txt
```

4. **Environment setup**
```bash
cp src/ziply_delivery/.env.example src/ziply_delivery/.env
# Edit src/ziply_delivery/.env with your MongoDB connection details
```

5. **Initialize database**
```bash
cd src/ziply_delivery
python manage.py init_database
```

6. **Run the server**
```bash
cd src/ziply_delivery
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Core Endpoints
- `GET /` - API documentation and available endpoints
- `GET /health/` - System health check and database connectivity

### Parcel Management
- `GET /api/parcels/` - List all parcels
- `POST /api/parcels/` - Create new parcel
- `GET /api/parcels/{tracking_number}/` - Get specific parcel details

### Example Usage

**Create a new parcel:**
```bash
curl -X POST http://localhost:8000/api/parcels/ \
  -H "Content-Type: application/json" \
  -d '{
    "sender_name": "Jyot Harshadkumar Bhavsar",
    "recipient_name": "Carson Fujita",
    "estimated_delivery": "2025-11-29T15:00:00Z",
    "current_location_address": "Warehouse A"
  }'
```

**Track a parcel:**
```bash
curl http://localhost:8000/api/parcels/TRK123456789/
```

## Environment Variables

Create a `.env` file in the project root:

```env
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB_NAME=delivery_service
DEBUG=True
SECRET_KEY=your-secret-key-here
```

## Database Schema

The system uses MongoDB with two main collections:

### Parcels Collection
- Unique tracking numbers
- Embedded status history
- Geographic location data
- Sender/recipient information

### Pages Collection
- Content management
- Metadata and analytics
- Tag-based organization

See `/database/README.md` for detailed schema documentation.

## Development

### Project Structure
```
ziply-delivery-service/
├── src/
│   ├── ziply_delivery/           # Main Django project
│   │   ├── parcels/              # Parcel tracking app
│   │   │   ├── models.py         # Parcel data models with status tracking
│   │   │   ├── views.py          # API views for parcel management
│   │   │   ├── urls.py           # Parcel API URL routing
│   │   │   └── management/       # Database management commands
│   │   │       └── commands/
│   │   │           └── init_database.py  # MongoDB index initialization
│   │   ├── api/                  # REST API endpoints
│   │   │   ├── models.py         # API data models
│   │   │   ├── views.py          # Core API views and health checks
│   │   │   └── urls.py           # API URL configuration
│   │   ├── company/              # Company portal app
│   │   │   ├── models.py         # Company user models
│   │   │   ├── views.py          # Company dashboard and authentication
│   │   │   ├── urls.py           # Company portal routing
│   │   │   └── forms.py          # Company registration forms
│   │   ├── client/               # Client portal app
│   │   │   ├── models.py         # Customer models
│   │   │   ├── views.py          # Client authentication and dashboard
│   │   │   ├── urls.py           # Client portal routing
│   │   │   └── forms.py          # Client registration forms
│   │   ├── pages/                # Content management app
│   │   │   ├── models.py         # Page content models
│   │   │   └── views.py          # Static page views
│   │   ├── templates/            # HTML templates
│   │   │   ├── company/          # Company portal templates
│   │   │   │   ├── dashboard.html    # Company dashboard with modal system
│   │   │   │   ├── login.html        # Company login form
│   │   │   │   └── register.html     # Company registration
│   │   │   ├── client/           # Client portal templates
│   │   │   │   ├── login.html        # Client login form
│   │   │   │   └── register.html     # Client registration
│   │   │   ├── page.html         # Base template with modern styling
│   │   │   ├── home.html         # Landing page with dual portal access
│   │   │   ├── track_parcel.html # Package tracking interface
│   │   │   ├── create_parcel.html # Shipment creation form
│   │   │   ├── about.html        # About page
│   │   │   ├── support.html      # Support and FAQ
│   │   │   ├── privacy_policy.html # Privacy policy
│   │   │   └── terms_of_service.html # Terms of service
│   │   ├── static/               # Static files
│   │   │   ├── css/              # Stylesheets
│   │   │   │   └── styles.css    # Main CSS with modal styling
│   │   │   ├── js/               # JavaScript files
│   │   │   └── images/           # Image assets
│   │   ├── ziply_delivery/       # Django project settings
│   │   │   ├── settings.py       # Main configuration
│   │   │   ├── urls.py           # Root URL configuration
│   │   │   ├── views.py          # Main project views
│   │   │   └── wsgi.py           # WSGI configuration
│   │   ├── manage.py             # Django management script
│   │   ├── .env.example          # Environment template
│   │   └── .env                  # Local environment (not in git)
│   └── requirements.txt          # Python dependencies
├── README.md                     # Project documentation
├── LICENSE                       # GPL-3.0 license
└── .gitignore                    # Git ignore rules
```

### Key Application Components

#### Company Dashboard Features
- **Modern Modal System**: Glassmorphism-styled modals for status updates
- **Real-time Updates**: AJAX-powered status modification without page refresh
- **Professional UI**: Modern card-based layout with hover effects
- **Status Management**: Complete parcel lifecycle management
- **Form Validation**: Client-side and server-side validation
- **CSRF Security**: Secure form submissions with token validation

#### Authentication System
- **Dual Portal Design**: Separate interfaces for customers and companies
- **Session Management**: Secure login/logout with proper redirects
- **Role-based Access**: Different permissions for users vs companies
- **Registration System**: Complete signup flow for both user types

#### API Architecture
- **RESTful Design**: Clean API endpoints following REST principles
- **Status Updates**: Real-time parcel status modification endpoints
- **Health Monitoring**: System health and database connectivity checks
- **Error Handling**: Comprehensive error responses with proper HTTP codes

#### Database Design
- **MongoDB Integration**: NoSQL database with optimized indexes
- **Status History**: Embedded document structure for tracking history
- **Geographic Data**: Location-based queries for delivery optimization
- **Unique Constraints**: Tracking number uniqueness with proper indexing

### Modern UI Components

#### Styling Architecture
- **CSS Custom Properties**: Consistent color scheme and spacing
- **Glassmorphism Effects**: Modern backdrop-blur and transparency
- **Responsive Design**: Mobile-first approach with CSS Grid/Flexbox
- **Animation System**: Smooth transitions and hover effects
- **Professional Typography**: Clean, readable font hierarchy

#### Interactive Elements
- **Modal System**: Professional overlay modals with backdrop blur
- **Form Controls**: Styled inputs with focus states and validation
- **Button Components**: Consistent button styling with hover effects
- **Status Badges**: Color-coded status indicators
- **Card Components**: Modern card layout with shadows and borders

#### JavaScript Features
- **AJAX Integration**: Asynchronous form submissions
- **DOM Manipulation**: Dynamic content updates
- **Event Handling**: Proper event delegation and cleanup
- **Error Handling**: User-friendly error messages and validation
- **CSRF Token Management**: Automatic token handling for security

### Running Tests
```bash
python manage.py test
```

### Database Management
```bash
# Initialize database with indexes
python manage.py init_database

# Create superuser for admin
python manage.py createsuperuser
```

## Deployment

### Production Checklist
- [ ] Set `DEBUG=False` in production
- [ ] Configure secure `SECRET_KEY`
- [ ] Set up MongoDB with authentication
- [ ] Configure allowed hosts
- [ ] Set up SSL/HTTPS
- [ ] Configure static file serving


## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Support

For support and questions:
- Create an issue in the GitHub repository
- Check the `/database/README.md` for database-specific documentation
- Review API documentation at the root endpoint (`/`)

---

**Created**: November 29, 2025  
**Author**: Ziply Dilevery Service  
**Version**: 1.2.0
