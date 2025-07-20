# BuildPro Connect - Project Structure

This document outlines the organized structure of the BuildPro Connect project for optimal deployment and maintenance.

## 📁 Project Structure

```
WebsiteMasterBuilder/
├── app.py                          # Main Flask application
├── wsgi.py                         # WSGI entry point for production
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version specification
├── Procfile                        # Process file for deployment
├── render.yaml                     # Render deployment configuration
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── DEPLOYMENT.md                   # Deployment guide
├── PROJECT_STRUCTURE.md            # This file
│
├── static/                         # Static files (CSS, JS, Images)
│   ├── css/
│   │   └── styles.css             # Main stylesheet
│   ├── js/
│   │   └── script.js              # Main JavaScript file
│   └── images/                    # Image assets
│       ├── contractor1.jpg
│       ├── contractor2.jpg
│       ├── contractor3.jpg
│       ├── worker1.jpg
│       ├── worker2.jpg
│       ├── worker3.jpg
│       ├── project1.jpg
│       ├── project2.jpg
│       └── project3.jpg
│
├── templates/                      # HTML templates
│   ├── base.html                  # Base template with navigation/footer
│   ├── index.html                 # Homepage
│   ├── admin.html                 # Admin panel
│   ├── services.html              # Services page
│   ├── projects.html              # Projects page
│   ├── workers.html               # Workers page
│   └── contractors.html           # Contractors page
│
├── data/                          # Data storage
│   └── database.json              # JSON database file
│
└── config/                        # Configuration files
    ├── config.py                  # Application configuration
    ├── simple_app.py              # Legacy simple app
    ├── run.py                     # Legacy run script
    └── __pycache__/               # Python cache
```

## 🏗️ Architecture Overview

### **Flask Application Structure**
- **app.py**: Main application with all routes and business logic
- **wsgi.py**: Production WSGI entry point
- **config/config.py**: Environment-specific configurations

### **Static Files Organization**
- **CSS**: All stylesheets in `static/css/`
- **JavaScript**: All scripts in `static/js/`
- **Images**: All images in `static/images/`

### **Template System**
- **base.html**: Base template with common elements
- **Individual pages**: Extend base template for consistency
- **Flask Jinja2**: Proper template inheritance and URL generation

### **Data Management**
- **JSON Database**: Simple file-based storage in `data/`
- **API Endpoints**: RESTful API for data operations
- **Admin Interface**: Web-based data management

## 🚀 Deployment Features

### **Render Deployment Ready**
- **render.yaml**: Blueprint configuration for automatic deployment
- **Procfile**: Process specification for web servers
- **runtime.txt**: Python version specification
- **requirements.txt**: Production dependencies

### **Production Optimizations**
- **Environment Variables**: Secure configuration management
- **Static File Serving**: Optimized for production
- **Error Handling**: Comprehensive error management
- **Security**: Production-ready security settings

## 📋 Key Features

### **Frontend**
- Responsive design for all devices
- Modern UI with smooth animations
- Interactive forms with validation
- Real-time data updates

### **Backend**
- RESTful API endpoints
- JSON-based data storage
- Admin panel for data management
- Contact and quote form processing

### **Database**
- JSON file-based storage
- Automatic data initialization
- Backup and restore capabilities
- Data validation and sanitization

## 🔧 Development Workflow

### **Local Development**
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run application: `python app.py`
4. Access at: `http://localhost:5001`

### **Production Deployment**
1. Push to GitHub
2. Deploy to Render using blueprint
3. Automatic deployment with database setup
4. Live at Render URL

## 📊 API Endpoints

### **Public Endpoints**
- `GET /` - Homepage
- `GET /admin` - Admin panel
- `GET /services` - Services page
- `GET /projects` - Projects page
- `GET /workers` - Workers page
- `GET /contractors` - Contractors page

### **API Endpoints**
- `POST /api/contact` - Submit contact form
- `POST /api/quote` - Submit quote request
- `GET /api/projects` - Get all projects
- `GET /api/services` - Get all services
- `GET /api/stats` - Get website statistics
- `GET /api/contractors` - Get all contractors
- `GET /api/workers` - Get all workers

### **Admin Endpoints**
- `GET /api/admin/contacts` - Get all contacts
- `GET /api/admin/quotes` - Get all quotes
- `PUT /api/admin/quote/<id>` - Update quote status

## 🛠️ Maintenance

### **Regular Tasks**
- Database backups
- Log monitoring
- Performance optimization
- Security updates

### **Updates**
- Template modifications
- API enhancements
- Database schema changes
- Static file updates

## 📈 Scalability

### **Current Architecture**
- File-based JSON storage
- Single-server deployment
- Static file serving

### **Future Enhancements**
- PostgreSQL database integration
- CDN for static files
- Load balancing
- Microservices architecture

---

This structure provides a solid foundation for a professional construction services website with room for growth and enhancement. 