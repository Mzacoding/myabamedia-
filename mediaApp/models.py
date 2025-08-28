from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils import timezone


class ContactSubmission(models.Model):
    """Model to store contact form submissions for record keeping."""
    
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s\-\']+$',
                message='Name can only contain letters, spaces, hyphens, and apostrophes.'
            )
        ]
    )
    email = models.EmailField(
        validators=[EmailValidator()]
    )
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    submitted_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True, help_text="Internal notes about this submission")
    
    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Submission'
        verbose_name_plural = 'Contact Submissions'
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.submitted_at.strftime('%Y-%m-%d %H:%M')})"
    
    def mark_as_processed(self, notes=None):
        """Mark this submission as processed."""
        self.is_processed = True
        self.processed_at = timezone.now()
        if notes:
            self.notes = notes
        self.save()


class ServiceCategory(models.Model):
    """Model for service categories."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon_class = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Font Awesome icon class (e.g., 'fas fa-code')"
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service Category'
        verbose_name_plural = 'Service Categories'
    
    def __str__(self):
        return self.name


class Service(models.Model):
    """Model for individual services offered."""
    
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        ServiceCategory, 
        on_delete=models.CASCADE, 
        related_name='services'
    )
    description = models.TextField()
    short_description = models.CharField(
        max_length=300, 
        blank=True,
        help_text="Brief description for cards/previews"
    )
    image = models.ImageField(
        upload_to='services/', 
        blank=True, 
        null=True,
        help_text="Service image (recommended: 800x600px)"
    )
    price_range = models.CharField(
        max_length=100, 
        blank=True,
        help_text="e.g., 'From R5,000' or 'R2,000 - R10,000'"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this service prominently on the homepage"
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category__order', 'order', 'title']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return f"{self.category.name} - {self.title}"


class Testimonial(models.Model):
    """Model for client testimonials."""
    
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(
        max_length=150, 
        blank=True,
        help_text="e.g., 'CEO at Company Name' or 'Local Business Owner'"
    )
    company = models.CharField(max_length=100, blank=True)
    testimonial_text = models.TextField(max_length=500)
    rating = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5,
        help_text="Rating out of 5 stars"
    )
    client_photo = models.ImageField(
        upload_to='testimonials/', 
        blank=True, 
        null=True,
        help_text="Client photo (recommended: 200x200px)"
    )
    is_featured = models.BooleanField(
        default=False,
        help_text="Show this testimonial prominently"
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.client_name} - {self.rating} stars"
    
    def get_stars_display(self):
        """Return star rating as string for templates."""
        return '★' * self.rating + '☆' * (5 - self.rating)


class NewsArticle(models.Model):
    """Model for news articles from The Highveld Chronicle."""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    excerpt = models.TextField(
        max_length=300,
        help_text="Brief summary of the article"
    )
    content = models.TextField()
    featured_image = models.ImageField(
        upload_to='news/', 
        blank=True, 
        null=True,
        help_text="Main article image (recommended: 1200x600px)"
    )
    author = models.CharField(max_length=100, default="The Highveld Chronicle")
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(
        default=False,
        help_text="Feature this article prominently"
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = 'News Article'
        verbose_name_plural = 'News Articles'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)