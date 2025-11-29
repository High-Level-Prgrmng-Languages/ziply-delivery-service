
# NoSQL Library API - Parcel Tracking System

A Django-based REST API for parcel tracking using MongoDB as the database backend. Built for efficient package management and real-time tracking capabilities.

## Features

- **Parcel Management**: Create, track, and manage parcels through REST API
- **MongoDB Integration**: NoSQL database with optimized indexes for performance
- **Real-time Tracking**: Complete status history for each parcel
- **Health Monitoring**: Built-in health check endpoints
- **Geographic Optimization**: Location-based queries for delivery routing

## Technology Stack

- **Backend**: Django 4.x with Django REST Framework
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
cd delivery-service-website
```

2. **Create virtual environment**
```bash
python3.14 -m venv myproject-env
# Alternative: python -m venv myproject-env
source myproject-env/bin/activate  # On Windows: myproject-env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r src/requirements.txt
```

4. **Environment setup**
```bash
cp src/.env.example src/.env
# Edit src/.env with your MongoDB connection details
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
myproject/
├── parcels/              # Parcel tracking app
├── pages/                # Pages management app
├── database/             # Database documentation and setup
├── myproject/            # Django project settings
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

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
**Author**: Jyot Harshadkumar Bhavsar 
**Version**: 1.0.0
