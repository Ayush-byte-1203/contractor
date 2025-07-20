"""
BuildPro Connect - Configuration Module
=======================================

This module contains configuration classes for different environments
(development, production, testing) and provides a centralized way to
manage application settings.

The configuration system allows for environment-specific settings while
maintaining a consistent interface across all environments.

Author: BuildPro Connect Team
Version: 1.0.0
"""

import os

class Config:
    """
    Base configuration class with common settings.
    
    This class defines the default configuration that is shared across
    all environments. Environment-specific classes inherit from this
    and override settings as needed.
    """
    
    # Security Configuration
    # SECRET_KEY is used for session management, CSRF protection, and other security features
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database Configuration
    # Path to the JSON database file (relative to project root)
    DATABASE_FILE = os.environ.get('DATABASE_FILE') or 'data/database.json'
    
    # Flask Application Settings
    DEBUG = False  # Disable debug mode by default for security
    TESTING = False  # Testing mode flag
    
    # Session Security Settings
    # These settings enhance the security of user sessions
    SESSION_COOKIE_SECURE = True  # Only send cookies over HTTPS
    SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access to cookies
    SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection for cookies
    
    # CORS (Cross-Origin Resource Sharing) Settings
    # Configure which origins can access the API
    # WARNING: Using '*' allows all origins - configure appropriately for production
    CORS_ORIGINS = ['*']  # Configure appropriately for production
    
    # Additional Security Headers (can be added here)
    # SECURITY_HEADERS = {
    #     'X-Content-Type-Options': 'nosniff',
    #     'X-Frame-Options': 'DENY',
    #     'X-XSS-Protection': '1; mode=block'
    # }

class DevelopmentConfig(Config):
    """
    Development environment configuration.
    
    This configuration is optimized for development with:
    - Debug mode enabled for detailed error messages
    - Less strict security settings for easier development
    - Development-specific database and logging
    """
    
    DEBUG = True  # Enable debug mode for development
    SESSION_COOKIE_SECURE = False  # Allow HTTP cookies in development
    
    # Development-specific settings
    # LOG_LEVEL = 'DEBUG'
    # DATABASE_FILE = 'data/dev_database.json'

class ProductionConfig(Config):
    """
    Production environment configuration.
    
    This configuration is optimized for production with:
    - Debug mode disabled for security
    - Strict security settings
    - Production-optimized settings
    """
    
    DEBUG = False  # Disable debug mode for security
    
    # Production-specific settings
    # These should be configured via environment variables in production
    
    # Database settings for production
    # DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Logging configuration
    # LOG_LEVEL = 'INFO'
    # LOG_FILE = '/var/log/buildpro/app.log'
    
    # Performance settings
    # MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Security enhancements for production
    # SESSION_COOKIE_SECURE = True  # Already set in base config
    # SESSION_COOKIE_HTTPONLY = True  # Already set in base config
    
    # Rate limiting (if implemented)
    # RATELIMIT_ENABLED = True
    # RATELIMIT_STORAGE_URL = 'redis://localhost:6379/0'

class TestingConfig(Config):
    """
    Testing environment configuration.
    
    This configuration is optimized for testing with:
    - Debug mode enabled for detailed error messages
    - Separate test database to avoid affecting development data
    - Testing-specific settings
    """
    
    TESTING = True  # Enable testing mode
    DEBUG = True  # Enable debug mode for testing
    DATABASE_FILE = 'data/test_database.json'  # Use separate test database
    
    # Testing-specific settings
    # WTF_CSRF_ENABLED = False  # Disable CSRF for testing
    # PRESERVE_CONTEXT_ON_EXCEPTION = False

# Configuration Dictionary
# This dictionary maps environment names to their respective configuration classes
# It allows the application to easily switch between configurations based on
# the FLASK_ENV environment variable or other configuration methods
config = {
    'development': DevelopmentConfig,  # Development environment
    'production': ProductionConfig,    # Production environment
    'testing': TestingConfig,          # Testing environment
    'default': DevelopmentConfig       # Default fallback configuration
}

# Usage Example:
# app.config.from_object(config[os.environ.get('FLASK_ENV', 'default')]) 