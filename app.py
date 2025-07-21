"""
Paramarsh Construction - Main Flask Application
========================================

This is the main Flask application for the Paramarsh Construction platform.
It provides a comprehensive construction services marketplace that connects
contractors, workers, and clients through a web-based interface.

Features:
- Contractor and worker management
- Project showcase and tracking
- Service catalog
- Contact and quote request handling
- Admin panel for data management
- RESTful API endpoints

Author: Paramarsh Construction Team
Version: 1.0.0
"""

# Standard library imports
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os
import json

# Initialize Flask application
app = Flask(__name__)

# Configure application settings
# SECRET_KEY is used for session management and CSRF protection
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Enable Cross-Origin Resource Sharing (CORS) for API access
CORS(app)

# Database configuration
# Using JSON file as a simple database for development
DB_FILE = 'data/database.json'

def init_db():
    """
    Initialize the database with default data if it doesn't exist.
    
    This function creates the data directory and populates it with sample data
    including contractors, workers, projects, and services. This ensures the
    application has data to work with on first run.
    
    Returns:
        None
    """
    if not os.path.exists(DB_FILE):
        # Create data directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        # Default data structure with sample records
        default_data = {
            'contacts': [],  # Store contact form submissions
            'quotes': [],    # Store quote requests
            'contractors': [
                {
                    'id': 1,
                    'name': 'ABC Construction Co.',
                    'email': 'info@abcconstruction.com',
                    'phone': '(555) 123-4567',
                    'specialties': ['residential', 'commercial'],
                    'rating': 4.8,
                    'experience_years': 15,
                    'completed_projects': 45,
                    'location': 'New York, NY',
                    'description': 'Leading construction company with 15+ years of experience in residential and commercial projects.',
                    'image_url': '/static/images/contractor1.jpg',
                    'status': 'active',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 2,
                    'name': 'Elite Builders LLC',
                    'email': 'contact@elitebuilders.com',
                    'phone': '(555) 234-5678',
                    'specialties': ['residential', 'renovation'],
                    'rating': 4.6,
                    'experience_years': 12,
                    'completed_projects': 38,
                    'location': 'Los Angeles, CA',
                    'description': 'Specialized in luxury residential construction and high-end renovations.',
                    'image_url': '/static/images/contractor2.jpg',
                    'status': 'active',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 3,
                    'name': 'Commercial Pro Builders',
                    'email': 'info@commercialpro.com',
                    'phone': '(555) 345-6789',
                    'specialties': ['commercial', 'industrial'],
                    'rating': 4.9,
                    'experience_years': 20,
                    'completed_projects': 67,
                    'location': 'Chicago, IL',
                    'description': 'Expert commercial and industrial construction with focus on large-scale projects.',
                    'image_url': '/static/images/contractor3.jpg',
                    'status': 'active',
                    'created_at': datetime.utcnow().isoformat()
                }
            ],
            'workers': [
                {
                    'id': 1,
                    'name': 'John Smith',
                    'email': 'john.smith@email.com',
                    'phone': '(555) 111-2222',
                    'specialties': ['carpentry', 'electrical'],
                    'experience_years': 8,
                    'rating': 4.7,
                    'location': 'New York, NY',
                    'hourly_rate': 45,
                    'availability': 'full-time',
                    'contractor_id': 1,  # Associated with ABC Construction Co.
                    'image_url': '/static/images/worker1.jpg',
                    'status': 'available',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 2,
                    'name': 'Maria Garcia',
                    'email': 'maria.garcia@email.com',
                    'phone': '(555) 222-3333',
                    'specialties': ['plumbing', 'hvac'],
                    'experience_years': 12,
                    'rating': 4.8,
                    'location': 'Los Angeles, CA',
                    'hourly_rate': 55,
                    'availability': 'full-time',
                    'contractor_id': 2,  # Associated with Elite Builders LLC
                    'image_url': '/static/images/worker2.jpg',
                    'status': 'available',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 3,
                    'name': 'Mike Johnson',
                    'email': 'mike.johnson@email.com',
                    'phone': '(555) 333-4444',
                    'specialties': ['masonry', 'concrete'],
                    'experience_years': 15,
                    'rating': 4.9,
                    'location': 'Chicago, IL',
                    'hourly_rate': 50,
                    'availability': 'full-time',
                    'contractor_id': 3,  # Associated with Commercial Pro Builders
                    'image_url': '/static/images/worker3.jpg',
                    'status': 'available',
                    'created_at': datetime.utcnow().isoformat()
                }
            ],
            'projects': [
                {
                    'id': 1,
                    'title': 'Modern Family Home',
                    'description': '3,200 sq ft custom home with smart home features',
                    'category': 'residential',
                    'image_url': '/static/images/project1.jpg',
                    'size': '3,200 sq ft',
                    'location': 'Suburban Area',
                    'budget': '$750,000',
                    'start_date': '2024-01-15',
                    'expected_completion': '2024-08-15',
                    'status': 'in-progress',
                    'progress': 65,  # Percentage complete
                    'contractor_id': 1,  # ABC Construction Co.
                    'assigned_workers': [1, 2],  # John Smith and Maria Garcia
                    'client_name': 'Sarah and Tom Wilson',
                    'client_email': 'wilson.family@email.com',
                    'client_phone': '(555) 444-5555',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 2,
                    'title': 'Office Complex',
                    'description': '15,000 sq ft modern office building',
                    'category': 'commercial',
                    'image_url': '/static/images/project2.jpg',
                    'size': '15,000 sq ft',
                    'location': 'Downtown',
                    'budget': '$2,500,000',
                    'start_date': '2024-03-01',
                    'expected_completion': '2024-12-01',
                    'status': 'in-progress',
                    'progress': 40,
                    'contractor_id': 3,  # Commercial Pro Builders
                    'assigned_workers': [3],  # Mike Johnson
                    'client_name': 'TechCorp Inc.',
                    'client_email': 'projects@techcorp.com',
                    'client_phone': '(555) 555-6666',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 3,
                    'title': 'Retail Center',
                    'description': 'Multi-tenant retail development',
                    'category': 'commercial',
                    'image_url': '/static/images/project3.jpg',
                    'size': '25,000 sq ft',
                    'location': 'Shopping District',
                    'budget': '$3,200,000',
                    'start_date': '2024-02-01',
                    'expected_completion': '2024-10-01',
                    'status': 'completed',
                    'progress': 100,
                    'contractor_id': 3,  # Commercial Pro Builders
                    'assigned_workers': [1, 2, 3],  # All workers
                    'client_name': 'Mall Development Group',
                    'client_email': 'info@malldev.com',
                    'client_phone': '(555) 666-7777',
                    'created_at': datetime.utcnow().isoformat()
                }
            ],
            'services': [
                {
                    'id': 1,
                    'name': 'Residential Construction',
                    'description': 'Custom homes, renovations, and additions tailored to your lifestyle.',
                    'icon': 'fas fa-home',
                    'category': 'residential',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 2,
                    'name': 'Commercial Projects',
                    'description': 'Office buildings, retail spaces, and industrial facilities.',
                    'icon': 'fas fa-building',
                    'category': 'commercial',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 3,
                    'name': 'Renovation & Remodeling',
                    'description': 'Transform existing spaces with modern upgrades and improvements.',
                    'icon': 'fas fa-tools',
                    'category': 'renovation',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 4,
                    'name': 'Project Management',
                    'description': 'Comprehensive project oversight from planning to completion.',
                    'icon': 'fas fa-clipboard-list',
                    'category': 'management',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 5,
                    'name': 'Electrical Services',
                    'description': 'Professional electrical installation and maintenance services.',
                    'icon': 'fas fa-bolt',
                    'category': 'electrical',
                    'created_at': datetime.utcnow().isoformat()
                },
                {
                    'id': 6,
                    'name': 'Plumbing Services',
                    'description': 'Expert plumbing installation, repair, and maintenance.',
                    'icon': 'fas fa-faucet',
                    'category': 'plumbing',
                    'created_at': datetime.utcnow().isoformat()
                }
            ]
        }
        
        # Save the default data to the database file
        save_db(default_data)

def load_db():
    """
    Load data from the JSON database file.
    
    Returns:
        dict: The loaded database data or empty dict if file doesn't exist
    """
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_db(data):
    """
    Save data to the JSON database file.
    
    Args:
        data (dict): The data to save to the database
        
    Returns:
        None
    """
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# ============================================================================
# ROUTE DEFINITIONS
# ============================================================================

@app.route('/')
def index():
    """
    Homepage route - displays the main landing page.
    
    Returns:
        str: Rendered HTML template for the homepage
    """
    return render_template('index.html')

@app.route('/admin')
def admin():
    """
    Admin panel route - displays the admin interface for managing data.
    
    Returns:
        str: Rendered HTML template for the admin panel
    """
    return render_template('admin.html')

@app.route('/services')
def services():
    """
    Services page route - displays available construction services.
    
    Returns:
        str: Rendered HTML template for the services page
    """
    return render_template('services.html')

@app.route('/projects')
def projects():
    """
    Projects page route - displays construction projects portfolio.
    
    Returns:
        str: Rendered HTML template for the projects page
    """
    return render_template('projects.html')

@app.route('/workers')
def workers():
    """
    Workers page route - displays available construction workers.
    
    Returns:
        str: Rendered HTML template for the workers page
    """
    return render_template('workers.html')

@app.route('/contractors')
def contractors():
    """
    Contractors page route - displays construction contractors.
    
    Returns:
        str: Rendered HTML template for the contractors page
    """
    return render_template('contractors.html')

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """
    API endpoint to handle contact form submissions.
    
    Expected JSON payload:
    {
        "name": "string",
        "email": "string", 
        "phone": "string" (optional),
        "message": "string"
    }
    
    Returns:
        JSON response with success/error status and message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Load existing database
        db_data = load_db()
        
        # Create new contact entry
        new_contact = {
            'id': len(db_data.get('contacts', [])) + 1,
            'name': data['name'],
            'email': data['email'],
            'phone': data.get('phone', ''),
            'message': data['message'],
            'created_at': datetime.utcnow().isoformat()
        }
        
        # Add to contacts list
        if 'contacts' not in db_data:
            db_data['contacts'] = []
        db_data['contacts'].append(new_contact)
        
        # Save updated database
        save_db(db_data)
        
        return jsonify({'success': True, 'message': 'Contact submitted successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Error submitting contact: {str(e)}'}), 500

@app.route('/api/quote', methods=['POST'])
def submit_quote():
    """
    API endpoint to handle quote request submissions.
    
    Expected JSON payload:
    {
        "name": "string",
        "email": "string",
        "phone": "string",
        "service_type": "string",
        "description": "string",
        "budget": "string" (optional)
    }
    
    Returns:
        JSON response with success/error status and message
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'service_type', 'description']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Load existing database
        db_data = load_db()
        
        # Create new quote entry
        new_quote = {
            'id': len(db_data.get('quotes', [])) + 1,
            'name': data['name'],
            'email': data['email'],
            'phone': data['phone'],
            'service_type': data['service_type'],
            'description': data['description'],
            'budget': data.get('budget', ''),
            'status': 'pending',  # Default status
            'created_at': datetime.utcnow().isoformat()
        }
        
        # Add to quotes list
        if 'quotes' not in db_data:
            db_data['quotes'] = []
        db_data['quotes'].append(new_quote)
        
        # Save updated database
        save_db(db_data)
        
        return jsonify({'success': True, 'message': 'Quote request submitted successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Error submitting quote: {str(e)}'}), 500

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """
    API endpoint to retrieve all projects.
    
    Returns:
        JSON response containing all projects data
    """
    db_data = load_db()
    return jsonify(db_data.get('projects', []))

@app.route('/api/services', methods=['GET'])
def get_services():
    """
    API endpoint to retrieve all services.
    
    Returns:
        JSON response containing all services data
    """
    db_data = load_db()
    return jsonify(db_data.get('services', []))

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    API endpoint to retrieve website statistics.
    
    Returns:
        JSON response containing various statistics about the platform
    """
    db_data = load_db()
    
    # Calculate statistics
    stats = {
        'total_contractors': len(db_data.get('contractors', [])),
        'total_workers': len(db_data.get('workers', [])),
        'total_projects': len(db_data.get('projects', [])),
        'completed_projects': len([p for p in db_data.get('projects', []) if p.get('status') == 'completed']),
        'active_projects': len([p for p in db_data.get('projects', []) if p.get('status') == 'in-progress']),
        'total_services': len(db_data.get('services', [])),
        'total_contacts': len(db_data.get('contacts', [])),
        'total_quotes': len(db_data.get('quotes', []))
    }
    
    return jsonify(stats)

# ============================================================================
# ADMIN API ENDPOINTS
# ============================================================================

@app.route('/api/admin/contacts', methods=['GET'])
def get_contacts():
    """
    Admin API endpoint to retrieve all contact submissions.
    
    Returns:
        JSON response containing all contact submissions
    """
    db_data = load_db()
    return jsonify(db_data.get('contacts', []))

@app.route('/api/admin/quotes', methods=['GET'])
def get_quotes():
    """
    Admin API endpoint to retrieve all quote requests.
    
    Returns:
        JSON response containing all quote requests
    """
    db_data = load_db()
    return jsonify(db_data.get('quotes', []))

@app.route('/api/admin/quote/<int:quote_id>', methods=['PUT'])
def update_quote_status(quote_id):
    """
    Admin API endpoint to update quote status.
    
    Args:
        quote_id (int): The ID of the quote to update
        
    Expected JSON payload:
    {
        "status": "string" (pending, approved, rejected)
    }
    
    Returns:
        JSON response with success/error status and message
    """
    try:
        data = request.get_json()
        new_status = data.get('status')
        
        if not new_status:
            return jsonify({'error': 'Status is required'}), 400
        
        # Load database
        db_data = load_db()
        quotes = db_data.get('quotes', [])
        
        # Find and update the quote
        for quote in quotes:
            if quote['id'] == quote_id:
                quote['status'] = new_status
                save_db(db_data)
                return jsonify({'success': True, 'message': 'Quote status updated successfully'})
        
        return jsonify({'error': 'Quote not found'}), 404
        
    except Exception as e:
        return jsonify({'error': f'Error updating quote: {str(e)}'}), 500

@app.route('/api/admin/projects', methods=['POST'])
def add_project():
    """
    Admin API endpoint to add a new project.
    
    Expected JSON payload:
    {
        "title": "string",
        "description": "string",
        "category": "string",
        "size": "string",
        "location": "string",
        "budget": "string",
        "contractor_id": int
    }
    
    Returns:
        JSON response with success/error status and message
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['title', 'description', 'category', 'size', 'location', 'budget', 'contractor_id']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Load database
        db_data = load_db()
        
        # Create new project
        new_project = {
            'id': len(db_data.get('projects', [])) + 1,
            'title': data['title'],
            'description': data['description'],
            'category': data['category'],
            'image_url': data.get('image_url', '/static/images/default-project.jpg'),
            'size': data['size'],
            'location': data['location'],
            'budget': data['budget'],
            'start_date': data.get('start_date', datetime.utcnow().strftime('%Y-%m-%d')),
            'expected_completion': data.get('expected_completion', ''),
            'status': data.get('status', 'in-progress'),
            'progress': data.get('progress', 0),
            'contractor_id': data['contractor_id'],
            'assigned_workers': data.get('assigned_workers', []),
            'client_name': data.get('client_name', ''),
            'client_email': data.get('client_email', ''),
            'client_phone': data.get('client_phone', ''),
            'created_at': datetime.utcnow().isoformat()
        }
        
        # Add to projects list
        if 'projects' not in db_data:
            db_data['projects'] = []
        db_data['projects'].append(new_project)
        
        # Save updated database
        save_db(db_data)
        
        return jsonify({'success': True, 'message': 'Project added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Error adding project: {str(e)}'}), 500

@app.route('/api/admin/services', methods=['POST'])
def add_service():
    """
    Admin API endpoint to add a new service.
    
    Expected JSON payload:
    {
        "name": "string",
        "description": "string",
        "icon": "string",
        "category": "string"
    }
    
    Returns:
        JSON response with success/error status and message
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'description', 'icon', 'category']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Load database
        db_data = load_db()
        
        # Create new service
        new_service = {
            'id': len(db_data.get('services', [])) + 1,
            'name': data['name'],
            'description': data['description'],
            'icon': data['icon'],
            'category': data['category'],
            'created_at': datetime.utcnow().isoformat()
        }
        
        # Add to services list
        if 'services' not in db_data:
            db_data['services'] = []
        db_data['services'].append(new_service)
        
        # Save updated database
        save_db(db_data)
        
        return jsonify({'success': True, 'message': 'Service added successfully'}), 201
        
    except Exception as e:
        return jsonify({'error': f'Error adding service: {str(e)}'}), 500

# ============================================================================
# CONTRACTOR API ENDPOINTS
# ============================================================================

@app.route('/api/contractors', methods=['GET'])
def get_contractors():
    """
    API endpoint to retrieve all contractors.
    
    Returns:
        JSON response containing all contractors data
    """
    db_data = load_db()
    return jsonify(db_data.get('contractors', []))

@app.route('/api/contractors/<int:contractor_id>', methods=['GET'])
def get_contractor(contractor_id):
    """
    API endpoint to retrieve a specific contractor by ID.
    
    Args:
        contractor_id (int): The ID of the contractor to retrieve
        
    Returns:
        JSON response containing contractor data or 404 if not found
    """
    db_data = load_db()
    contractors = db_data.get('contractors', [])
    
    for contractor in contractors:
        if contractor['id'] == contractor_id:
            return jsonify(contractor)
    
    return jsonify({'error': 'Contractor not found'}), 404

@app.route('/api/contractors/<int:contractor_id>/projects', methods=['GET'])
def get_contractor_projects(contractor_id):
    """
    API endpoint to retrieve all projects for a specific contractor.
    
    Args:
        contractor_id (int): The ID of the contractor
        
    Returns:
        JSON response containing projects for the contractor
    """
    db_data = load_db()
    projects = db_data.get('projects', [])
    
    contractor_projects = [p for p in projects if p.get('contractor_id') == contractor_id]
    return jsonify(contractor_projects)

@app.route('/api/contractors/<int:contractor_id>/workers', methods=['GET'])
def get_contractor_workers(contractor_id):
    """
    API endpoint to retrieve all workers for a specific contractor.
    
    Args:
        contractor_id (int): The ID of the contractor
        
    Returns:
        JSON response containing workers for the contractor
    """
    db_data = load_db()
    workers = db_data.get('workers', [])
    
    contractor_workers = [w for w in workers if w.get('contractor_id') == contractor_id]
    return jsonify(contractor_workers)

# ============================================================================
# WORKER API ENDPOINTS
# ============================================================================

@app.route('/api/workers', methods=['GET'])
def get_workers():
    """
    API endpoint to retrieve all workers.
    
    Returns:
        JSON response containing all workers data
    """
    db_data = load_db()
    return jsonify(db_data.get('workers', []))

@app.route('/api/workers/<int:worker_id>', methods=['GET'])
def get_worker(worker_id):
    """
    API endpoint to retrieve a specific worker by ID.
    
    Args:
        worker_id (int): The ID of the worker to retrieve
        
    Returns:
        JSON response containing worker data or 404 if not found
    """
    db_data = load_db()
    workers = db_data.get('workers', [])
    
    for worker in workers:
        if worker['id'] == worker_id:
            return jsonify(worker)
    
    return jsonify({'error': 'Worker not found'}), 404

@app.route('/api/workers/<int:worker_id>/projects', methods=['GET'])
def get_worker_projects(worker_id):
    """
    API endpoint to retrieve all projects a worker is assigned to.
    
    Args:
        worker_id (int): The ID of the worker
        
    Returns:
        JSON response containing projects the worker is assigned to
    """
    db_data = load_db()
    projects = db_data.get('projects', [])
    
    worker_projects = [p for p in projects if worker_id in p.get('assigned_workers', [])]
    return jsonify(worker_projects)

# ============================================================================
# PROJECT API ENDPOINTS
# ============================================================================

@app.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project_detail(project_id):
    """
    API endpoint to retrieve detailed information about a specific project.
    
    Args:
        project_id (int): The ID of the project to retrieve
        
    Returns:
        JSON response containing detailed project information or 404 if not found
    """
    db_data = load_db()
    projects = db_data.get('projects', [])
    
    for project in projects:
        if project['id'] == project_id:
            # Get contractor information
            contractor = None
            contractors = db_data.get('contractors', [])
            for c in contractors:
                if c['id'] == project.get('contractor_id'):
                    contractor = c
                    break
            
            # Get assigned workers information
            assigned_workers = []
            workers = db_data.get('workers', [])
            for worker_id in project.get('assigned_workers', []):
                for w in workers:
                    if w['id'] == worker_id:
                        assigned_workers.append(w)
                        break
            
            # Add additional information to project
            project_detail = project.copy()
            project_detail['contractor'] = contractor
            project_detail['assigned_workers_detail'] = assigned_workers
            
            return jsonify(project_detail)
    
    return jsonify({'error': 'Project not found'}), 404

# ============================================================================
# SEARCH API ENDPOINTS
# ============================================================================

@app.route('/api/search/contractors', methods=['GET'])
def search_contractors():
    """
    API endpoint to search contractors by various criteria.
    
    Query Parameters:
        location (str): Filter by location
        specialty (str): Filter by specialty
        rating (float): Minimum rating
        experience (int): Minimum years of experience
        
    Returns:
        JSON response containing filtered contractors
    """
    db_data = load_db()
    contractors = db_data.get('contractors', [])
    
    # Get query parameters
    location = request.args.get('location', '').lower()
    specialty = request.args.get('specialty', '').lower()
    rating = request.args.get('rating', type=float)
    experience = request.args.get('experience', type=int)
    
    # Filter contractors based on criteria
    filtered_contractors = []
    
    for contractor in contractors:
        # Check if contractor matches all criteria
        matches = True
        
        if location and location not in contractor.get('location', '').lower():
            matches = False
        
        if specialty and specialty not in [s.lower() for s in contractor.get('specialties', [])]:
            matches = False
        
        if rating and contractor.get('rating', 0) < rating:
            matches = False
        
        if experience and contractor.get('experience_years', 0) < experience:
            matches = False
        
        if matches:
            filtered_contractors.append(contractor)
    
    return jsonify(filtered_contractors)

@app.route('/api/search/workers', methods=['GET'])
def search_workers():
    """
    API endpoint to search workers by various criteria.
    
    Query Parameters:
        location (str): Filter by location
        specialty (str): Filter by specialty
        rating (float): Minimum rating
        experience (int): Minimum years of experience
        max_rate (float): Maximum hourly rate
        
    Returns:
        JSON response containing filtered workers
    """
    db_data = load_db()
    workers = db_data.get('workers', [])
    
    # Get query parameters
    location = request.args.get('location', '').lower()
    specialty = request.args.get('specialty', '').lower()
    rating = request.args.get('rating', type=float)
    experience = request.args.get('experience', type=int)
    max_rate = request.args.get('max_rate', type=float)
    
    # Filter workers based on criteria
    filtered_workers = []
    
    for worker in workers:
        # Check if worker matches all criteria
        matches = True
        
        if location and location not in worker.get('location', '').lower():
            matches = False
        
        if specialty and specialty not in [s.lower() for s in worker.get('specialties', [])]:
            matches = False
        
        if rating and worker.get('rating', 0) < rating:
            matches = False
        
        if experience and worker.get('experience_years', 0) < experience:
            matches = False
        
        if max_rate and worker.get('hourly_rate', 0) > max_rate:
            matches = False
        
        if matches:
            filtered_workers.append(worker)
    
    return jsonify(filtered_workers)

# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    """
    Main entry point for the Flask application.
    
    This block runs when the script is executed directly (not imported).
    It initializes the database and starts the Flask development server.
    """
    # Initialize database with default data if needed
    init_db()
    
    # Start the Flask development server
    # In production, use a WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=5001) 