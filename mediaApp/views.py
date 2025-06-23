from django.shortcuts import render
from django.templatetags.static import static

from django.shortcuts import render, redirect # Import redirect
from django.templatetags.static import static
from django.core.mail import send_mail # Import send_mail
from django.conf import settings # Import settings to get DEFAULT_FROM_EMAIL
from django.contrib import messages # Import messages framework
from .forms import ContactForm # Import your new ContactForm
def get_base_context():
    """
    Returns common context data used across multiple templates.
    """
    return {
        
        'newspaper_name': 'The Highveld Chronicle Newspaper',
        'company_name': 'Myaba Media Tech',
        'email': 'info@myabamediatech.com',
        'phone': '+27 81 410 9337',
        'address': 'University Rd, Hatfield, Pretoria, 0083',
    }

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
            'image_url': static('images/officePc.jpg'),
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
                'icon_class': 'fas fa-code'
            },
            {
                'title': 'Graphic Design',
                'description': 'Creating stunning visuals and brand identities that resonate with your audience.',
                'icon_class': 'fas fa-paint-brush'
            },
            {
                'title': 'News Publishing',
                'description': 'Delivering timely, accurate, and unbiased news through The Highveld Chronicle.',
                'icon_class': 'fas fa-newspaper'
            },
        ],
        'testimonials': [
            {
                'quote': 'Myaba Media Tech transformed our online presence. Their web development is top-notch!',
                'author': 'Client A, Local Business Owner'
            },
            {
                'quote': 'The Highveld Chronicle provides essential community news. Highly reliable and informative.',
                'author': 'Community Member, Nkangala District'
            },
            {
                'quote': 'Exceptional graphic design service. They truly understood our vision and brought it to life.',
                'author': 'Client C, Startup Founder'
            },
        ]
    }
    return render(request, 'home.html', context)  



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
            'image_url': 'images/webDesign.jpg'
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

def contact_view(request):
    """
    Renders the Contact page and handles form submissions.
    """
    # Get base context data for the page
    context = get_base_context()

    if request.method == 'POST':
        # If the request is POST, it means the form was submitted
        form = ContactForm(request.POST) # Create a form instance with submitted data
        if form.is_valid():
            # If the form data is valid, process it
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email message
            email_subject = f"Website Contact Form: {subject} from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = [settings.DEFAULT_FROM_EMAIL] # Send to your configured email

            try:
                # Send the email
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL, # From email (should be your configured website email)
                    recipient_list,
                    fail_silently=False, # Set to False to raise exceptions on email sending errors
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact') # Redirect to clear the form and show success message
            except Exception as e:
                # If there's an error sending email, add an error message
                messages.error(request, f'There was an error sending your message. Please try again later. ({e})')
                print(f"Email sending error: {e}") # Log the error for debugging
        else:
            # If the form is not valid, add an error message
            messages.error(request, 'Please correct the errors in the form.')
    else:
        # If the request is GET, display an empty form
        form = ContactForm()

    # Add the form instance to the context for rendering
    context['form'] = form
    return render(request, 'contact.html', context)