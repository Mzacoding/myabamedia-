# 🚀 Deployment Guide - Myaba Media Tech

This guide provides step-by-step instructions for deploying the Myaba Media Tech application to production.

## 📋 Pre-Deployment Checklist

### Environment Setup
- [ ] Python 3.8+ installed
- [ ] PostgreSQL database configured
- [ ] Domain name configured
- [ ] SSL certificate ready
- [ ] Email service configured (Gmail SMTP or similar)

### Security Configuration
- [ ] Strong SECRET_KEY generated
- [ ] DEBUG=False in production
- [ ] ALLOWED_HOSTS configured
- [ ] Database credentials secured
- [ ] Email credentials secured

## 🌐 Render.com Deployment

### 1. Repository Setup
```bash
# Ensure your code is in a Git repository
git add .
git commit -m "Prepare for production deployment"
git push origin main
```

### 2. Render.com Configuration

1. **Create New Web Service**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Select your repository and branch

2. **Build Settings**
   ```
   Build Command: pip install -r requirements.txt && python manage.py setup_production --skip-superuser
   Start Command: gunicorn myabamediatech.wsgi:application
   ```

3. **Environment Variables**
   ```
   DEBUG=False
   SECRET_KEY=your-super-secret-key-here
   DATABASE_URL=postgresql://user:password@host:port/database
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ADMIN_EMAIL=admin@yourdomain.com
   ADMIN_PASSWORD=secure-admin-password
   ```

### 3. Database Setup

1. **Create PostgreSQL Database**
   - In Render dashboard, create a new PostgreSQL database
   - Copy the connection string to DATABASE_URL

2. **Run Migrations**
   ```bash
   # This is handled automatically by setup_production command
   python manage.py migrate
   ```

### 4. Static Files Configuration

Static files are handled by WhiteNoise automatically. Ensure your settings include:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

## 🔧 Manual Server Deployment

### 1. Server Preparation (Ubuntu/Debian)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Install Node.js (for potential frontend assets)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### 2. Application Setup

```bash
# Create application directory
sudo mkdir -p /var/www/myabamediatech
cd /var/www/myabamediatech

# Clone repository
sudo git clone https://github.com/yourusername/myabamedia-.git .

# Create virtual environment
sudo python3 -m venv venv
sudo chown -R www-data:www-data /var/www/myabamediatech

# Activate virtual environment and install dependencies
sudo -u www-data bash
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Create .env file
sudo -u www-data nano .env
```

Add your production environment variables:
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:password@localhost/myabamediatech
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 4. Database Setup

```bash
# Create PostgreSQL database and user
sudo -u postgres psql
CREATE DATABASE myabamediatech;
CREATE USER myabauser WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE myabamediatech TO myabauser;
\q

# Run setup command
sudo -u www-data bash
source venv/bin/activate
python manage.py setup_production
```

### 5. Gunicorn Configuration

```bash
# Create Gunicorn socket file
sudo nano /etc/systemd/system/gunicorn.socket
```

```ini
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

```bash
# Create Gunicorn service file
sudo nano /etc/systemd/system/gunicorn.service
```

```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/myabamediatech
ExecStart=/var/www/myabamediatech/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          myabamediatech.wsgi:application

[Install]
WantedBy=multi-user.target
```

### 6. Nginx Configuration

```bash
# Create Nginx configuration
sudo nano /etc/nginx/sites-available/myabamediatech
```

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/myabamediatech;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        root /var/www/myabamediatech;
        expires 1y;
        add_header Cache-Control "public";
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

### 7. SSL Configuration with Certbot

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Test automatic renewal
sudo certbot renew --dry-run
```

### 8. Start Services

```bash
# Enable and start services
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl start gunicorn.service
sudo systemctl enable gunicorn.service

# Enable Nginx site
sudo ln -s /etc/nginx/sites-available/myabamediatech /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable nginx
```

## 📊 Monitoring and Maintenance

### Log Monitoring
```bash
# Check Gunicorn logs
sudo journalctl -u gunicorn.service -f

# Check Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Check application logs
sudo tail -f /var/www/myabamediatech/logs/django.log
```

### Regular Maintenance Tasks

1. **Database Backups**
   ```bash
   # Create backup script
   sudo nano /usr/local/bin/backup-db.sh
   ```
   
   ```bash
   #!/bin/bash
   DATE=$(date +%Y%m%d_%H%M%S)
   pg_dump myabamediatech > /backups/myabamediatech_$DATE.sql
   # Keep only last 7 days of backups
   find /backups -name "myabamediatech_*.sql" -mtime +7 -delete
   ```

2. **Update Application**
   ```bash
   cd /var/www/myabamediatech
   sudo -u www-data git pull origin main
   sudo -u www-data bash
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   exit
   sudo systemctl restart gunicorn.service
   ```

## 🔒 Security Best Practices

### Firewall Configuration
```bash
# Configure UFW firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### Regular Security Updates
```bash
# Set up automatic security updates
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure -plow unattended-upgrades
```

### Monitoring Setup
- Set up log monitoring (e.g., Logwatch)
- Configure fail2ban for intrusion prevention
- Monitor disk space and performance
- Set up uptime monitoring

## 🆘 Troubleshooting

### Common Issues

1. **Static Files Not Loading**
   ```bash
   python manage.py collectstatic --noinput
   sudo systemctl restart gunicorn.service
   ```

2. **Database Connection Issues**
   - Check DATABASE_URL in environment variables
   - Verify PostgreSQL service is running
   - Check database user permissions

3. **Email Not Working**
   - Verify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
   - Check Gmail app password configuration
   - Test SMTP connection

4. **Permission Issues**
   ```bash
   sudo chown -R www-data:www-data /var/www/myabamediatech
   sudo chmod -R 755 /var/www/myabamediatech
   ```

### Performance Optimization

1. **Enable Gzip Compression**
   ```nginx
   # Add to Nginx configuration
   gzip on;
   gzip_vary on;
   gzip_min_length 1024;
   gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
   ```

2. **Database Optimization**
   ```bash
   # Regular database maintenance
   python manage.py dbshell
   VACUUM ANALYZE;
   ```

3. **Caching Setup**
   - Configure Redis for session storage
   - Enable Django's cache framework
   - Set up CDN for static files

## 📞 Support

For deployment support, contact:
- **Email**: info@myabamediatech.com
- **Phone**: +27 81 410 9337

---

**Myaba Media Tech** - Professional deployment made simple.