# Paramarsh Construction 🏗️

A modern construction services platform that connects contractors, workers, and clients through a comprehensive web application. Built with Flask backend and responsive frontend design.

![Paramarsh Construction](https://img.shields.io/badge/Flask-3.0+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🏠 **Core Functionality**
- **Contractor Management**: Browse and connect with verified contractors
- **Worker Directory**: Find skilled workers for specific projects
- **Project Showcase**: View completed and ongoing construction projects
- **Service Catalog**: Explore available construction services
- **Contact System**: Direct communication between clients and professionals
- **Quote Requests**: Submit and manage project quotes

### 🎨 **User Experience**
- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Modern UI/UX**: Clean, professional interface with smooth animations
- **Interactive Forms**: Real-time validation and user feedback
- **Search & Filter**: Find contractors and workers by location, specialty, and rating
- **Admin Panel**: Comprehensive backend management system

### 🔧 **Technical Features**
- **RESTful API**: Complete backend API for all operations
- **JSON Database**: Lightweight, file-based data storage
- **CORS Support**: Cross-origin resource sharing enabled
- **Form Processing**: Secure contact and quote submission handling
- **Data Validation**: Server-side validation and sanitization

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd connect2construct
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the website**
   Open your browser and navigate to: `http://localhost:5001`

## 📁 Project Structure

```
connect2construct/
├── app.py                          # Main Flask application
├── wsgi.py                         # WSGI entry point for production
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version specification
├── Procfile                        # Process file for deployment
├── render.yaml                     # Render deployment configuration
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── DEPLOYMENT.md                   # Deployment guide
├── PROJECT_STRUCTURE.md            # Project structure documentation
│
├── static/                         # Static files
│   ├── css/
│   │   └── styles.css             # Main stylesheet
│   ├── js/
│   │   └── script.js              # Main JavaScript file
│   └── images/                    # Image assets
│
├── templates/                      # HTML templates
│   ├── base.html                  # Base template
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
    └── run.py                     # Legacy run script
```

## 🗄️ Database Schema

### Contractors
- `id`: Unique identifier
- `name`: Company name
- `email`: Contact email
- `phone`: Contact phone
- `specialties`: Array of specialties
- `rating`: Average rating (0-5)
- `experience_years`: Years of experience
- `completed_projects`: Number of completed projects
- `location`: Service location
- `description`: Company description
- `image_url`: Profile image
- `status`: Active/inactive status

### Workers
- `id`: Unique identifier
- `name`: Worker name
- `email`: Contact email
- `phone`: Contact phone
- `specialties`: Array of skills
- `experience_years`: Years of experience
- `rating`: Average rating (0-5)
- `location`: Work location
- `hourly_rate`: Hourly rate
- `availability`: Availability status
- `contractor_id`: Associated contractor
- `image_url`: Profile image
- `status`: Available/unavailable status

### Projects
- `id`: Unique identifier
- `title`: Project title
- `description`: Project description
- `category`: Project category
- `image_url`: Project image
- `size`: Project size
- `location`: Project location
- `budget`: Project budget
- `start_date`: Project start date
- `expected_completion`: Expected completion date
- `status`: Project status
- `progress`: Completion percentage
- `contractor_id`: Assigned contractor
- `assigned_workers`: Array of worker IDs
- `client_name`: Client name
- `client_email`: Client email
- `client_phone`: Client phone

### Services
- `id`: Unique identifier
- `name`: Service name
- `description`: Service description
- `icon`: Font Awesome icon class
- `category`: Service category

## 🔌 API Endpoints

### Public Endpoints
- `GET /` - Homepage
- `GET /admin` - Admin panel
- `GET /services` - Services page
- `GET /projects` - Projects page
- `GET /workers` - Workers page
- `GET /contractors` - Contractors page

### API Endpoints
- `POST /api/contact` - Submit contact form
- `POST /api/quote` - Submit quote request
- `GET /api/projects` - Get all projects
- `GET /api/services` - Get all services
- `GET /api/stats` - Get website statistics
- `GET /api/contractors` - Get all contractors
- `GET /api/contractors/<id>` - Get specific contractor
- `GET /api/contractors/<id>/projects` - Get contractor's projects
- `GET /api/contractors/<id>/workers` - Get contractor's workers
- `GET /api/workers` - Get all workers
- `GET /api/workers/<id>` - Get specific worker
- `GET /api/workers/<id>/projects` - Get worker's projects
- `GET /api/projects/<id>` - Get specific project details
- `GET /api/search/contractors` - Search contractors
- `GET /api/search/workers` - Search workers

### Admin Endpoints
- `GET /api/admin/contacts` - Get all contact submissions
- `GET /api/admin/quotes` - Get all quote requests
- `PUT /api/admin/quote/<id>` - Update quote status
- `POST /api/admin/projects` - Add new project
- `POST /api/admin/services` - Add new service

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 3.0+**: Web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: WSGI server for production

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox and Grid
- **JavaScript**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### Data Storage
- **JSON**: File-based database
- **SQLAlchemy**: Database ORM (for future PostgreSQL integration)

## 🚀 Deployment

### Local Development
```bash
python app.py
```
Access at: `http://localhost:5001`

### Production Deployment
This project is configured for deployment on Render. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

**Quick Deploy to Render:**
1. Push code to GitHub
2. Connect repository to Render
3. Deploy using the provided `render.yaml` blueprint

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Flask secret key for sessions
- `PORT`: Application port (default: 5001)
- `DATABASE_URL`: Database connection string (for future use)

### Customization
- **Styling**: Modify `static/css/styles.css`
- **Functionality**: Edit `static/js/script.js`
- **Backend Logic**: Update `app.py`
- **Templates**: Modify files in `templates/`

## 🧪 Testing

### Manual Testing
1. **Contact Form**: Submit test contact via homepage
2. **Quote Request**: Submit test quote request
3. **Admin Panel**: Access `/admin` to view submissions
4. **API Endpoints**: Test all API endpoints
5. **Responsive Design**: Test on different screen sizes

### Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Troubleshooting

**Common Issues:**
1. **Port already in use**: Change port in `app.py`
2. **Database errors**: Delete `data/database.json` and restart
3. **Missing dependencies**: Run `pip install -r requirements.txt`
4. **CORS errors**: Ensure Flask-CORS is installed

**Getting Help:**
- Check the [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for detailed architecture
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for deployment issues
- Open an issue on GitHub for bugs or feature requests

## 📊 Roadmap

### Planned Features
- [ ] PostgreSQL database integration
- [ ] User authentication and profiles
- [ ] Real-time messaging system
- [ ] Project bidding system
- [ ] Payment integration
- [ ] Mobile app development
- [ ] Advanced search and filtering
- [ ] Email notifications
- [ ] File upload for project images
- [ ] Analytics dashboard

### Performance Improvements
- [ ] Database indexing optimization
- [ ] CDN integration for static assets
- [ ] Caching implementation
- [ ] API rate limiting
- [ ] Image optimization

---

**Paramarsh Construction** - Connecting construction professionals with clients, one project at a time. 🏗️✨

*Built with ❤️ using Flask and modern web technologies* 