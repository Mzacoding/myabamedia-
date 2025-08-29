from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseServerError, JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods
import logging
from .forms import ContactForm
from .models import Service, Testimonial, NewsArticle

# Configure logging
logger = logging.getLogger(__name__)
def get_base_context():
    """
    Returns common context data used across multiple templates.
    """
    return {
        
        'newspaper_name': 'The Highveld Chronicle Newspaper',
        'company_name': 'Myaba Media Tech',
        'email': 'info@myabamediatech.com',
        'phone': '+27 81 410 9337',
        'address': '29 GELDENHUYS DELMAS',
    }

@cache_page(60 * 15)  # Cache for 15 minutes
def home_view(request):
    """
    Renders the main home page with dynamic hero content.
    """
    slides = [
        {
            'image_url': static('images/screenImg.jpg'), 
            'h1_text': 'The Pulse of the Highveld',
            'h2_text': 'Your Complete ICT, Media & Publishing Partner.',
            'p_text': 'Connecting communities and empowering businesses in the Nkangala District Municipality and beyond.'
        },
        {
            'image_url': static('images/background.png'),
            'h1_text': 'Innovating Solutions',
            'h2_text': 'Cutting-Edge ICT for Your Business Growth.',
            'p_text': 'Transforming challenges into opportunities with bespoke web development and system design.'
        },
        {
            'image_url': static('images/news.jpg'),
            'h1_text': 'Informing Communities',
            'h2_text': 'Reliable News from The Highveld Chronicle',
            'p_text': 'Delivering timely, accurate, and unbiased news to over 1.5 million people.'
        },
        {
            'image_url': static('images/office.jpg'),
            'h1_text': 'Building Digital Futures',
            'h2_text': 'Expert Web & System Development Services.',
            'p_text': 'Creating intuitive websites and robust systems that drive your success.'
        },
    ]

    context = {
        **get_base_context(),
        'district': 'Nkangala District Municipality',
        'population_coverage': 'over 1.5 million people',
        'slides_data': slides,
        'key_services': [
            {
                'title': 'Web Development',
                'description': 'Crafting responsive and high-performance websites tailored to your business goals.',
                'icon_class': 'fas fa-laptop-code',
                'image_url': 'images/SoftWareCodingImg.jpg'
            },
            {
                'title': 'Graphic Design',
                'description': 'Creating stunning visuals and brand identities that resonate with your audience.',
                'icon_class': 'fas fa-palette',
                'image_url': 'images/GraphicDesign.jpg'
            },
            {
                'title': 'News Publishing',
                'description': 'Delivering timely, accurate, and unbiased news through The Highveld Chronicle.',
                'icon_class': 'fas fa-newspaper',
                'image_url': 'images/news.jpg'
            },
            {
            'title': 'Digital Marketing Strategies',
            'description': 'Crafting tailored online campaigns to boost your brand\'s visibility and engagement across all platforms.',
            'icon_class': 'fas fa-chart-line',
            'image_url': 'images/ecommence.jpg'
           },
        ],
        'testimonials': [
            {
                'quote': 'Myaba Media Tech transformed our online presence. Their web development is top-notch!',
                'author': 'Nyiko Mkansi, Local Business Owner'
            },
            {
                'quote': 'The Highveld Chronicle provides essential community news. Highly reliable and informative.',
                'author': 'Community Member, Nkangala District'
            },
            {
                'quote': 'Exceptional graphic design service. They truly understood our vision and brought it to life.',
                'author': 'Meisie M, Startup Founder'
            },
            {
            'quote': 'Our website traffic and lead generation have seen a remarkable increase since their team revamped our online presence. The development process was seamless, and their technical expertise is truly unmatched.',
            'author': 'Alex M., E-commerce Manager'
            }
        ]
    }
    return render(request, 'home.html', context)  



@cache_page(60 * 30)  # Cache for 30 minutes
def about_view(request):
    """
    Renders the About Us page.
    """
    context = {
        **get_base_context(),
        'founded_year': 2012,
        'newspaper_established_year': 2016,
        'district': 'Nkangala District Municipality',
        'population_coverage': 'over 1.5 million people',
    }
    return render(request, 'about.html', context)

@cache_page(60 * 30)  # Cache for 30 minutes
def services_view(request):
    """
    Renders the Our Services page with new image-based services.
    """
    services = [
        {
            'title': 'Graphic Design',
            'description': 'Our expert graphic designers bring your brand to life with stunning visuals. From logo creation and brand identity kits to marketing collateral like brochures, flyers, and social media graphics, we ensure your message is communicated clearly and creatively. We specialize in designs that capture attention and resonate with your target audience, enhancing your overall market presence and appeal.',
            'image_url': 'images/GraphicDesign.jpg'
        },
        {
            'title': 'News Posting',
            'description': 'We provide timely and accurate dissemination of local news and community updates, ensuring residents are well-informed. Our news posting services cover everything from breaking local stories and community events to public announcements and investigative journalism. We are dedicated to delivering unbiased, factual news that keeps the pulse of the community at your fingertips, fostering informed citizens.',
            'image_url': 'images/news.jpg'
        },
        {
            'title': 'Web Development',
            'description': 'Our team builds responsive, high-performance websites tailored precisely to your business needs. Whether you require a dynamic e-commerce platform, a robust corporate site, or an interactive web application, we utilize the latest technologies and best practices to deliver secure, scalable, and user-friendly web solutions that drive engagement and achieve your online objectives.',
            'image_url': 'images/SoftWareCodingImg.jpg'
        },
        {
            'title': 'System Design',
            'description': 'We architect robust and scalable IT systems that optimize your business operations. Our system design services encompass a holistic approach, from conceptualization and requirements gathering to detailed architectural planning and technology selection. We focus on creating efficient, secure, and future-proof systems that align with your strategic goals, ensuring seamless integration and peak performance for your enterprise infrastructure.',
            'image_url': 'images/PcCoding.jpg'
        },
        {
            'title': 'System Modeling',
            'description': 'Developing detailed models for complex systems is our forte, ensuring efficiency, reliability, and predictability. Through advanced modeling techniques, we simulate system behavior, analyze performance metrics, and identify potential bottlenecks before implementation. This rigorous approach minimizes risks, reduces development costs, and ensures that the final system meets all functional and non-functional requirements with precision.',
            'image_url': 'images/system.jpg'
        },
        {
            'title': 'Business Websites',
            'description': 'We specialize in crafting professional and engaging online presences for businesses of all sizes. Our business website development services focus on creating sites that are not just visually appealing but also highly functional, optimized for search engines, and easy to navigate. From lead generation to showcasing your products and services, we build platforms that effectively convert visitors into customers and enhance your digital footprint.',
            'image_url': 'images/ecommence.jpg'
        },
        {
            'title': 'Portfolied Websites',
            'description': 'Showcase your work and achievements with elegantly designed portfolio websites. Our portfolio website development services are perfect for artists, photographers, freelancers, and professionals looking to present their work in a compelling and organized manner. We focus on clean layouts, high-quality image presentation, and intuitive navigation to highlight your best work and make a lasting impression on potential clients or employers.',
            'image_url': 'images/codingImga2.jpg'
        },
    ]
    context = {
        **get_base_context(),
        'services': services,
    }
    return render(request, 'services.html', context) 

@csrf_protect
def contact_view(request):
    """
    Professional contact page with enhanced error handling and security.
    """
    context = get_base_context()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            try:
                # Extract cleaned data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                
                # Construct professional email
                email_subject = f"[Myaba Media Tech] New Contact: {subject}"
                email_message = f"""
New contact form submission from Myaba Media Tech website:

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from the Myaba Media Tech contact form.
Reply directly to this email to respond to the sender.
"""
                
                # Send email with enhanced error handling
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    reply_to=[email],  # Allow direct reply to sender
                    fail_silently=False,
                )
                
                # Log successful submission
                logger.info(f"Contact form submitted successfully by {name} ({email})")
                
                # Success message and redirect
                messages.success(
                    request, 
                    'Thank you for your message! We\'ll get back to you within 24 hours.'
                )
                return redirect('contact')
                
            except BadHeaderError:
                logger.warning(f"Bad header detected in contact form from {email}")
                messages.error(
                    request, 
                    'Invalid header detected. Please check your input and try again.'
                )
                
            except Exception as e:
                logger.error(f"Email sending failed: {str(e)} - From: {email}")
                messages.error(
                    request,
                    'We\'re experiencing technical difficulties. Please try again later or contact us directly.'
                )
        else:
            # Form validation failed
            logger.info(f"Contact form validation failed: {form.errors}")
            messages.error(
                request, 
                'Please correct the errors below and try again.'
            )
    else:
        form = ContactForm()
    
    context['form'] = form
    return render(request, 'contact.html', context)



@cache_page(60 * 30)
def portfolio_view(request):
    """Portfolio page with featured projects."""
    context = get_base_context()
    return render(request, 'portfolio.html', context)


@require_http_methods(["GET"])
def api_search(request):
    """API endpoint for search functionality."""
    query = request.GET.get('q', '').strip()
    
    if len(query) < 2:
        return JsonResponse({'results': []})
    
    results = []
    
    # Search services
    services = Service.objects.filter(
        title__icontains=query,
        is_active=True
    )[:3]
    
    for service in services:
        results.append({
            'title': service.title,
            'description': service.short_description or service.description[:100],
            'url': '/services/',
            'type': 'service'
        })
    
    # Search news articles
    articles = NewsArticle.objects.filter(
        title__icontains=query,
        is_published=True
    )[:3]
    
    for article in articles:
        results.append({
            'title': article.title,
            'description': article.excerpt,
            'url': f'/news/{article.slug}/',
            'type': 'news'
        })
    
    return JsonResponse({'results': results})


@cache_page(60 * 60)
def news_view(request):
    """News listing page."""
    articles = NewsArticle.objects.filter(is_published=True)[:10]
    context = {
        **get_base_context(),
        'articles': articles
    }
    return render(request, 'news.html', context)