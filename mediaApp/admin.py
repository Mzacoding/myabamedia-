from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils import timezone
from .models import ContactSubmission, ServiceCategory, Service, Testimonial, NewsArticle


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    """Professional admin interface for contact submissions."""
    
    list_display = [
        'name', 'email', 'subject', 'submitted_at', 
        'is_processed', 'processed_status'
    ]
    list_filter = [
        'is_processed', 'submitted_at', 'processed_at'
    ]
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = [
        'submitted_at', 'ip_address', 'user_agent'
    ]
    list_per_page = 25
    date_hierarchy = 'submitted_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Submission Details', {
            'fields': ('submitted_at', 'ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Processing', {
            'fields': ('is_processed', 'processed_at', 'notes')
        })
    )
    
    def processed_status(self, obj):
        if obj.is_processed:
            return format_html(
                '<span style="color: green;">✓ Processed</span>'
            )
        return format_html(
            '<span style="color: orange;">⏳ Pending</span>'
        )
    processed_status.short_description = 'Status'
    
    actions = ['mark_as_processed']
    
    def mark_as_processed(self, request, queryset):
        updated = queryset.update(
            is_processed=True, 
            processed_at=timezone.now()
        )
        self.message_user(
            request, 
            f'{updated} submissions marked as processed.'
        )
    mark_as_processed.short_description = 'Mark selected as processed'


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """Admin interface for service categories."""
    
    list_display = ['name', 'order', 'is_active', 'service_count']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['order', 'is_active']
    
    def service_count(self, obj):
        count = obj.services.count()
        if count > 0:
            url = reverse('admin:mediaApp_service_changelist')
            return format_html(
                '<a href="{}?category__id__exact={}">{} services</a>',
                url, obj.id, count
            )
        return '0 services'
    service_count.short_description = 'Services'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for services."""
    
    list_display = [
        'title', 'category', 'price_range', 'is_featured', 
        'is_active', 'order'
    ]
    list_filter = [
        'category', 'is_featured', 'is_active', 'created_at'
    ]
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['is_featured', 'is_active', 'order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'short_description')
        }),
        ('Content', {
            'fields': ('description', 'image')
        }),
        ('Pricing & Display', {
            'fields': ('price_range', 'is_featured', 'is_active', 'order')
        })
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Admin interface for testimonials."""
    
    list_display = [
        'client_name', 'company', 'rating_display', 
        'is_featured', 'is_active', 'created_at'
    ]
    list_filter = [
        'rating', 'is_featured', 'is_active', 'created_at'
    ]
    search_fields = [
        'client_name', 'company', 'client_title', 'testimonial_text'
    ]
    list_editable = ['is_featured', 'is_active']
    
    def rating_display(self, obj):
        return obj.get_stars_display()
    rating_display.short_description = 'Rating'


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    """Admin interface for news articles."""
    
    list_display = [
        'title', 'author', 'is_published', 'is_featured', 
        'published_at', 'created_at'
    ]
    list_filter = [
        'is_published', 'is_featured', 'author', 
        'published_at', 'created_at'
    ]
    search_fields = ['title', 'excerpt', 'content', 'author']
    list_editable = ['is_published', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured', 'published_at')
        })
    )
    
    def save_model(self, request, obj, form, change):
        if obj.is_published and not obj.published_at:
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)


# Customize admin site headers
admin.site.site_header = 'Myaba Media Tech Administration'
admin.site.site_title = 'Myaba Media Tech Admin'
admin.site.index_title = 'Welcome to Myaba Media Tech Administration'