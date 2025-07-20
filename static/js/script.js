/**
 * BuildPro Connect - Main JavaScript File
 * =======================================
 * 
 * This file contains all the interactive functionality for the BuildPro Connect
 * website. It handles navigation, form submissions, animations, and user interactions.
 * 
 * Features:
 * - Mobile navigation toggle
 * - Smooth scrolling navigation
 * - Modal windows for forms
 * - Form validation and submission
 * - Scroll animations and effects
 * - Counter animations for statistics
 * - Loading states and user feedback
 * 
 * Author: BuildPro Connect Team
 * Version: 1.0.0
 */

// ============================================================================
// NAVIGATION FUNCTIONALITY
// ============================================================================

/**
 * Mobile Navigation Toggle
 * Handles the hamburger menu for mobile devices
 */
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

// Toggle mobile menu when hamburger is clicked
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a navigation link
document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}));

/**
 * Smooth Scrolling Navigation
 * Enables smooth scrolling for anchor links within the page
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/**
 * Scroll to Section Function
 * Programmatically scroll to a specific section
 * 
 * @param {string} sectionId - The ID of the section to scroll to
 */
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// ============================================================================
// MODAL FUNCTIONALITY
// ============================================================================

/**
 * Open Modal Function
 * Displays a modal window and prevents background scrolling
 * 
 * @param {string} modalId - The ID of the modal to open
 */
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
}

/**
 * Close Modal Function
 * Hides a modal window and restores background scrolling
 * 
 * @param {string} modalId - The ID of the modal to close
 */
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto'; // Restore scrolling
    }
}

// Close modal when clicking outside the modal content
window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
        e.target.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
});

// ============================================================================
// NAVBAR EFFECTS
// ============================================================================

/**
 * Navbar Background Change on Scroll
 * Changes navbar appearance when user scrolls down
 */
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        // Scrolled down - make navbar more opaque and add shadow
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
        navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
        // At top - make navbar semi-transparent and remove shadow
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
        navbar.style.boxShadow = 'none';
    }
});

// ============================================================================
// FORM HANDLING
// ============================================================================

/**
 * Contact Form Submission Handler
 * Handles the submission of the contact form on the homepage
 */
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Extract form data
    const data = {
        name: this.querySelector('input[type="text"]').value,
        email: this.querySelector('input[type="email"]').value,
        phone: this.querySelector('input[type="tel"]').value,
        message: this.querySelector('textarea').value
    };

    try {
        // Show loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        showLoading(submitBtn);

        // Send POST request to API
        const response = await fetch('/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            // Success - show success message and reset form
            alert('Message sent successfully! We will get back to you soon.');
            this.reset();
        } else {
            // Error - show error message
            const errorData = await response.json();
            alert(`Error: ${errorData.error || 'Failed to send message. Please try again.'}`);
        }
    } catch (error) {
        // Network or other error
        console.error('Error:', error);
        alert('Error sending message. Please try again.');
    } finally {
        // Hide loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        hideLoading(submitBtn, originalText);
    }
});

/**
 * Quote Form Submission Handler
 * Handles the submission of the quote request form
 */
document.getElementById('quoteForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Extract form data
    const data = {
        name: this.querySelector('input[type="text"]').value,
        email: this.querySelector('input[type="email"]').value,
        phone: this.querySelector('input[type="tel"]').value,
        service_type: this.querySelector('select').value, // Note: API expects service_type
        description: this.querySelector('textarea').value,
        budget: this.querySelector('input[placeholder*="Budget"]').value
    };

    try {
        // Show loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        showLoading(submitBtn);

        // Send POST request to API
        const response = await fetch('/api/quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            // Success - show success message, reset form, and close modal
            alert('Quote request submitted successfully! We will contact you within 24 hours.');
            this.reset();
            closeModal('quoteModal');
        } else {
            // Error - show error message
            const errorData = await response.json();
            alert(`Error: ${errorData.error || 'Failed to submit quote request. Please try again.'}`);
        }
    } catch (error) {
        // Network or other error
        console.error('Error:', error);
        alert('Error submitting quote request. Please try again.');
    } finally {
        // Hide loading state
        const submitBtn = this.querySelector('button[type="submit"]');
        hideLoading(submitBtn, originalText);
    }
});

// ============================================================================
// ANIMATIONS AND EFFECTS
// ============================================================================

/**
 * Scroll Animation Observer Configuration
 * Defines how elements should animate when they come into view
 */
const observerOptions = {
    threshold: 0.1, // Trigger when 10% of element is visible
    rootMargin: '0px 0px -50px 0px' // Trigger 50px before element enters viewport
};

/**
 * Intersection Observer for Scroll Animations
 * Animates elements when they come into view
 */
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Element is visible - animate it in
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

/**
 * Initialize Scroll Animations
 * Sets up animations for service cards, project cards, and statistics
 */
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = document.querySelectorAll('.service-card, .project-card, .stat');
    
    animateElements.forEach(el => {
        // Set initial state (hidden and moved down)
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        
        // Start observing the element
        observer.observe(el);
    });
});

/**
 * Counter Animation Function
 * Animates a number from 0 to target value
 * 
 * @param {HTMLElement} element - The element containing the number
 * @param {number} target - The target number to count to
 * @param {number} duration - Animation duration in milliseconds
 */
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16); // 60fps animation
    
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            // Animation complete
            element.textContent = target + '+';
            clearInterval(timer);
        } else {
            // Update counter
            element.textContent = Math.floor(start) + '+';
        }
    }, 16); // ~60fps
}

/**
 * Statistics Counter Observer
 * Triggers counter animations when stats section comes into view
 */
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Stats section is visible - animate counters
            const stats = entry.target.querySelectorAll('.stat h3');
            stats.forEach(stat => {
                const target = parseInt(stat.textContent);
                animateCounter(stat, target);
            });
            // Stop observing after animation is triggered
            statsObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Start observing the stats section
document.addEventListener('DOMContentLoaded', () => {
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
});

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

/**
 * Form Validation Function
 * Validates form inputs and shows error messages
 * 
 * @param {HTMLFormElement} form - The form element to validate
 * @returns {boolean} - True if form is valid, false otherwise
 */
function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        // Remove existing error styling
        input.classList.remove('error');
        
        // Check if field is required and empty
        if (input.hasAttribute('required') && !input.value.trim()) {
            input.classList.add('error');
            isValid = false;
        }
        
        // Email validation
        if (input.type === 'email' && input.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value)) {
                input.classList.add('error');
                isValid = false;
            }
        }
        
        // Phone validation (basic)
        if (input.type === 'tel' && input.value) {
            const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
            if (!phoneRegex.test(input.value.replace(/[\s\-\(\)]/g, ''))) {
                input.classList.add('error');
                isValid = false;
            }
        }
    });
    
    return isValid;
}

/**
 * Show Loading State
 * Shows a loading spinner on a button
 * 
 * @param {HTMLElement} element - The button element
 */
function showLoading(element) {
    element.disabled = true;
    element.innerHTML = '<span class="spinner"></span> Sending...';
}

/**
 * Hide Loading State
 * Restores the original button text
 * 
 * @param {HTMLElement} element - The button element
 * @param {string} originalText - The original button text
 */
function hideLoading(element, originalText) {
    element.disabled = false;
    element.innerHTML = originalText;
}

// ============================================================================
// ENHANCED USER EXPERIENCE
// ============================================================================

/**
 * Back to Top Button
 * Creates and manages a "back to top" button that appears when scrolling
 */
function createBackToTopButton() {
    // Create button element
    const backToTopBtn = document.createElement('button');
    backToTopBtn.innerHTML = '↑';
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.title = 'Back to top';
    
    // Add to page
    document.body.appendChild(backToTopBtn);
    
    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.style.display = 'block';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    
    // Scroll to top when clicked
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

/**
 * Preloader Function
 * Shows a loading screen while the page is loading
 */
function createPreloader() {
    // Create preloader element
    const preloader = document.createElement('div');
    preloader.className = 'preloader';
    preloader.innerHTML = `
        <div class="preloader-content">
            <div class="spinner"></div>
            <p>Loading BuildPro Connect...</p>
        </div>
    `;
    
    // Add to page
    document.body.appendChild(preloader);
    
    // Hide preloader when page is loaded
    window.addEventListener('load', () => {
        setTimeout(() => {
            preloader.style.opacity = '0';
            setTimeout(() => {
                preloader.remove();
            }, 300);
        }, 500);
    });
}

// ============================================================================
// INITIALIZATION
// ============================================================================

/**
 * Initialize All Features
 * Sets up all interactive features when the DOM is loaded
 */
document.addEventListener('DOMContentLoaded', () => {
    // Create enhanced user experience features
    createBackToTopButton();
    createPreloader();
    
    // Initialize any additional features here
    console.log('BuildPro Connect - JavaScript initialized successfully');
});

/**
 * Error Handling
 * Global error handler for unhandled JavaScript errors
 */
window.addEventListener('error', (e) => {
    console.error('JavaScript Error:', e.error);
    // You could send this to an error tracking service
});

/**
 * Performance Monitoring
 * Logs page load performance metrics
 */
window.addEventListener('load', () => {
    // Log performance metrics
    if ('performance' in window) {
        const perfData = performance.getEntriesByType('navigation')[0];
        console.log('Page Load Time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
    }
}); 