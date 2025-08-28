from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.conf import settings
import os


class Command(BaseCommand):
    """
    Professional setup command for production deployment.
    Usage: python manage.py setup_production
    """
    
    help = 'Sets up the application for production deployment'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-superuser',
            action='store_true',
            help='Skip superuser creation',
        )
        parser.add_argument(
            '--skip-static',
            action='store_true',
            help='Skip static files collection',
        )
    
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚀 Setting up Myaba Media Tech for production...')
        )
        
        # Run migrations
        self.stdout.write('📊 Running database migrations...')
        try:
            call_command('migrate', verbosity=0)
            self.stdout.write(
                self.style.SUCCESS('✅ Database migrations completed')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Migration failed: {e}')
            )
            return
        
        # Collect static files
        if not options['skip_static']:
            self.stdout.write('📁 Collecting static files...')
            try:
                call_command('collectstatic', '--noinput', verbosity=0)
                self.stdout.write(
                    self.style.SUCCESS('✅ Static files collected')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'⚠️ Static files collection failed: {e}')
                )
        
        # Create superuser if needed
        if not options['skip_superuser']:
            if not User.objects.filter(is_superuser=True).exists():
                self.stdout.write('👤 Creating superuser...')
                try:
                    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@myabamediatech.com')
                    admin_password = os.environ.get('ADMIN_PASSWORD')
                    
                    if admin_password:
                        User.objects.create_superuser(
                            username='admin',
                            email=admin_email,
                            password=admin_password
                        )
                        self.stdout.write(
                            self.style.SUCCESS(f'✅ Superuser created: {admin_email}')
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(
                                '⚠️ ADMIN_PASSWORD not set. Skipping superuser creation.'
                            )
                        )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'❌ Superuser creation failed: {e}')
                    )
            else:
                self.stdout.write(
                    self.style.SUCCESS('✅ Superuser already exists')
                )
        
        # Check configuration
        self.stdout.write('🔧 Checking configuration...')
        
        config_checks = [
            ('DEBUG', settings.DEBUG, False, 'Should be False in production'),
            ('SECRET_KEY', len(settings.SECRET_KEY) > 20, True, 'Should be a strong secret key'),
            ('ALLOWED_HOSTS', len(settings.ALLOWED_HOSTS) > 0, True, 'Should contain your domain'),
        ]
        
        for name, current, expected, message in config_checks:
            if current == expected:
                self.stdout.write(f'✅ {name}: OK')
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠️ {name}: {message}')
                )
        
        # Security recommendations
        self.stdout.write('\n🔒 Security Recommendations:')
        security_tips = [
            'Ensure DEBUG=False in production',
            'Use a strong SECRET_KEY',
            'Configure HTTPS/SSL certificates',
            'Set up regular database backups',
            'Monitor application logs',
            'Keep dependencies updated',
        ]
        
        for tip in security_tips:
            self.stdout.write(f'  • {tip}')
        
        self.stdout.write(
            self.style.SUCCESS('\n🎉 Production setup completed successfully!')
        )
        self.stdout.write(
            'Visit your admin panel at /admin/ to manage content.'
        )