// Professional Animation Controller
class ProfessionalAnimations {
    constructor() {
        this.init();
    }

    init() {
        this.setupScrollAnimations();
        this.setupHeroAnimations();
        this.setupColorMatching();
        this.setupStatsCounters();
        this.setupPageTransitions();
    }

    // Smooth scroll-triggered animations
    setupScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in', 'revealed');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        // Observe elements for animation
        document.querySelectorAll('.section-animate, .card-animate, .reveal-up, .reveal-left, .reveal-right, .scale-in, .stats-animate').forEach(el => {
            observer.observe(el);
        });
    }

    // Enhanced hero animations with color matching
    setupHeroAnimations() {
        const hero = document.getElementById('hero');
        if (!hero) return;

        const slides = this.getSlidesData();
        if (!slides || slides.length === 0) return;

        let currentIndex = 0;
        
        // Enhanced slide transition
        const changeSlide = () => {
            const slide = slides[currentIndex];
            
            // Smooth background transition with color overlay
            hero.style.backgroundImage = `linear-gradient(135deg, rgba(102, 126, 234, 0.8), rgba(118, 75, 162, 0.8)), url('${slide.image_url}')`;
            
            // Animate text changes
            this.animateTextChange(hero, slide);
            
            currentIndex = (currentIndex + 1) % slides.length;
        };

        // Initial slide
        changeSlide();
        
        // Auto-change slides
        setInterval(changeSlide, 8000);
    }

    // Smooth text animation for hero changes
    animateTextChange(hero, slide) {
        const h1 = hero.querySelector('.dynamic-h1');
        const h2 = hero.querySelector('.dynamic-h2');
        const p = hero.querySelector('.dynamic-p');

        // Fade out
        [h1, h2, p].forEach((el, index) => {
            if (el) {
                el.style.opacity = '0';
                el.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    el.textContent = index === 0 ? slide.h1_text : 
                                   index === 1 ? slide.h2_text : slide.p_text;
                    
                    // Fade in with stagger
                    setTimeout(() => {
                        el.style.opacity = '1';
                        el.style.transform = 'translateY(0)';
                    }, index * 200);
                }, 400);
            }
        });
    }

    // Color matching system
    setupColorMatching() {
        const colorPalette = {
            primary: '#667eea',
            secondary: '#764ba2',
            accent: '#3498db',
            success: '#27ae60',
            warning: '#f39c12',
            danger: '#e74c3c'
        };

        // Apply consistent colors
        document.documentElement.style.setProperty('--primary-color', colorPalette.primary);
        document.documentElement.style.setProperty('--secondary-color', colorPalette.secondary);
        document.documentElement.style.setProperty('--accent-color', colorPalette.accent);
    }

    // Enhanced stats counter with smooth animation
    setupStatsCounters() {
        const counters = document.querySelectorAll('.stats-counter');
        
        const animateCounter = (counter) => {
            const target = parseInt(counter.dataset.target);
            const duration = 2500;
            const increment = target / (duration / 16);
            let current = 0;

            const updateCounter = () => {
                current += increment;
                counter.textContent = Math.floor(current);
                
                if (current < target) {
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target;
                    // Add completion effect
                    counter.style.transform = 'scale(1.1)';
                    setTimeout(() => {
                        counter.style.transform = 'scale(1)';
                    }, 200);
                }
            };

            updateCounter();
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    animateCounter(entry.target);
                }
            });
        });

        counters.forEach(counter => observer.observe(counter));
    }

    // Page transition effects
    setupPageTransitions() {
        // Add page transition class to main content
        const main = document.querySelector('main');
        if (main) {
            main.classList.add('page-transition');
        }

        // Smooth link transitions
        document.querySelectorAll('a[href^="/"]').forEach(link => {
            link.addEventListener('click', (e) => {
                if (link.target !== '_blank') {
                    e.preventDefault();
                    
                    // Fade out effect
                    document.body.style.opacity = '0.8';
                    document.body.style.transform = 'scale(0.98)';
                    
                    setTimeout(() => {
                        window.location.href = link.href;
                    }, 300);
                }
            });
        });
    }

    // Get slides data from template
    getSlidesData() {
        const slidesElement = document.getElementById('slides-data');
        if (slidesElement) {
            try {
                return JSON.parse(slidesElement.textContent);
            } catch (e) {
                console.warn('Could not parse slides data');
                return null;
            }
        }
        return null;
    }
}

// Enhanced interaction effects
class InteractionEffects {
    constructor() {
        this.setupHoverEffects();
        this.setupClickEffects();
        this.setupFormAnimations();
    }

    setupHoverEffects() {
        // Add professional hover to cards
        document.querySelectorAll('.interactive-card, .key-service-item, .testimonial-item').forEach(card => {
            card.classList.add('professional-hover');
            
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-8px) scale(1.02)';
                card.style.boxShadow = '0 20px 40px rgba(0,0,0,0.15)';
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0) scale(1)';
                card.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
            });
        });

        // Enhanced button hovers
        document.querySelectorAll('.btn-modern, .btn-primary, .btn-secondary').forEach(btn => {
            btn.classList.add('btn-professional');
        });
    }

    setupClickEffects() {
        // Ripple effect on buttons
        document.querySelectorAll('button, .btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const ripple = document.createElement('span');
                const rect = btn.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.cssText = `
                    position: absolute;
                    width: ${size}px;
                    height: ${size}px;
                    left: ${x}px;
                    top: ${y}px;
                    background: rgba(255,255,255,0.3);
                    border-radius: 50%;
                    transform: scale(0);
                    animation: ripple 0.6s linear;
                    pointer-events: none;
                `;
                
                btn.style.position = 'relative';
                btn.style.overflow = 'hidden';
                btn.appendChild(ripple);
                
                setTimeout(() => ripple.remove(), 600);
            });
        });
    }

    setupFormAnimations() {
        // Enhanced form field animations
        document.querySelectorAll('input, textarea').forEach(field => {
            field.addEventListener('focus', () => {
                field.style.transform = 'scale(1.02)';
                field.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.2)';
            });
            
            field.addEventListener('blur', () => {
                field.style.transform = 'scale(1)';
                field.style.boxShadow = 'none';
            });
        });
    }
}

// Add ripple animation CSS
const rippleCSS = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;

const style = document.createElement('style');
style.textContent = rippleCSS;
document.head.appendChild(style);

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new ProfessionalAnimations();
    new InteractionEffects();
    
    // Add animation classes to elements
    document.querySelectorAll('.who-we-are-section, .key-services-section, .testimonials-section, .cta-section').forEach(section => {
        section.classList.add('section-animate');
    });
    
    document.querySelectorAll('.key-service-item, .testimonial-item').forEach(item => {
        item.classList.add('card-animate');
    });
    
    document.querySelectorAll('.stats-counter').forEach(counter => {
        counter.parentElement.classList.add('stats-animate');
    });
});