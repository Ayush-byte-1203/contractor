# Deploy BuildPro Connect to Render

This guide will help you deploy your BuildPro Connect website to Render with full backend and database support.

## Prerequisites

1. A Render account (free at [render.com](https://render.com))
2. Your code pushed to a Git repository (GitHub, GitLab, etc.)

## Step 1: Prepare Your Repository

Ensure your repository contains all the necessary files:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `render.yaml` - Render configuration
- `Procfile` - Process file for deployment
- `runtime.txt` - Python version specification
- All HTML, CSS, and JS files

## Step 2: Deploy to Render

### Option A: Using render.yaml (Recommended)

1. **Connect Repository**: 
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" and select "Blueprint"
   - Connect your Git repository

2. **Deploy Services**:
   - Render will automatically detect the `render.yaml` file
   - It will create both the web service and PostgreSQL database
   - Click "Apply" to start the deployment

### Option B: Manual Deployment

1. **Create Web Service**:
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" and select "Web Service"
   - Connect your Git repository
   - Configure the service:
     - **Name**: `buildpro-connect`
     - **Environment**: `Python`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
     - **Health Check Path**: `/api/stats`

2. **Create PostgreSQL Database**:
   - Click "New +" and select "PostgreSQL"
   - **Name**: `buildpro-db`
   - **Plan**: Free
   - Copy the connection string for later use

3. **Link Database to Web Service**:
   - Go back to your web service
   - Add environment variable:
     - **Key**: `DATABASE_URL`
     - **Value**: Your PostgreSQL connection string

## Step 3: Environment Variables

Add these environment variables to your web service:

- `SECRET_KEY`: A secure random string (Render can generate this)
- `PORT`: Usually set automatically by Render
- `DATABASE_URL`: Your PostgreSQL connection string (if using database)

## Step 4: Verify Deployment

1. **Check Health**: Visit your app's health check endpoint: `https://your-app.onrender.com/api/stats`

2. **Test Features**:
   - Homepage: `https://your-app.onrender.com/`
   - Admin Panel: `https://your-app.onrender.com/admin`
   - Contact Form: Submit a test contact
   - Quote Form: Submit a test quote request

## Step 5: Custom Domain (Optional)

1. Go to your web service settings
2. Click "Custom Domains"
3. Add your domain and configure DNS

## Troubleshooting

### Common Issues

1. **Build Failures**:
   - Check the build logs in Render dashboard
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version in `runtime.txt`

2. **Database Connection Issues**:
   - Verify `DATABASE_URL` environment variable
   - Check if database service is running
   - Ensure database is accessible from web service

3. **Static Files Not Loading**:
   - Check file paths in HTML files
   - Verify static file serving routes in `app.py`

4. **Health Check Failures**:
   - Ensure `/api/stats` endpoint returns 200 status
   - Check application logs for errors

### Logs and Monitoring

- **Application Logs**: Available in Render dashboard under your web service
- **Build Logs**: Check build process and dependency installation
- **Health Checks**: Monitor service health and uptime

## Performance Optimization

1. **Enable Caching**: Add caching headers for static assets
2. **Database Indexing**: Optimize database queries
3. **CDN**: Use a CDN for static assets
4. **Compression**: Enable gzip compression

## Security Considerations

1. **Environment Variables**: Never commit sensitive data to Git
2. **HTTPS**: Render provides SSL certificates automatically
3. **Input Validation**: Ensure all form inputs are validated
4. **Rate Limiting**: Consider adding rate limiting for API endpoints

## Support

If you encounter issues:
1. Check Render's documentation: [docs.render.com](https://docs.render.com)
2. Review application logs in Render dashboard
3. Test locally before deploying changes

---

Your BuildPro Connect website should now be live at `https://your-app-name.onrender.com`! 