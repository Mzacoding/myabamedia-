// Modern Features JavaScript

class ModernUI {
    constructor() {
        this.init();
    }

    init() {
        this.setupLoadingScreen();
        this.setupScrollProgress();
        this.setupDarkMode();
        this.setupParticles();
        this.setupCounters();
        this.setupTypingAnimation();
        this.setupSmoothScroll();
        this.setupLazyLoading();
        this.setupNotifications();
    }

    // Loading screen
    setupLoadingScreen() {
        window.addEventListener('load', () => {
            const loader = document.querySelector('.loading-screen');
            if (loader) {
                setTimeout(() => {
                    loader.classList.add('hidden');
                }, 1000);
            }
        });
    }

    // Scroll progress bar
    setupScrollProgress() {
        const progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', () => {
            const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
            progressBar.style.width = scrolled + '%';
        });
    }

    // Dark mode toggle
    setupDarkMode() {
        const toggle = document.createElement('div');
        toggle.className = 'theme-toggle';
        toggle.title = 'Toggle Dark Mode';
        document.body.appendChild(toggle);

        // Check saved theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.body.classList.add('dark-theme');
            toggle.classList.add('active');
        }

        toggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-theme');
            toggle.classList.toggle('active');
            
            const isDark = document.body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }

    // Particle background
    setupParticles() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        document.body.appendChild(particlesContainer);

        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 6 + 's';
            particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
            particlesContainer.appendChild(particle);
        }
    }

    // Animated counters
    setupCounters() {
        const counters = document.querySelectorAll('.stats-counter');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.animateCounter(entry.target);
                }
            });
        });

        counters.forEach(counter => observer.observe(counter));
    }

    animateCounter(element) {
        const target = parseInt(element.dataset.target);
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const timer = setInterval(() => {
            current += step;
            element.textContent = Math.floor(current);
            
            if (current >= target) {
                element.textContent = target;
                clearInterval(timer);
            }
        }, 16);
    }

    // Typing animation
    setupTypingAnimation() {
        const typingElements = document.querySelectorAll('.typing-text');
        
        typingElements.forEach(element => {
            const text = element.textContent;
            element.textContent = '';
            element.style.width = '0';
            
            let i = 0;
            const timer = setInterval(() => {
                element.textContent += text.charAt(i);
                i++;
                
                if (i > text.length) {
                    clearInterval(timer);
                    element.style.borderRight = 'none';
                }
            }, 100);
        });
    }

    // Smooth scroll
    setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Lazy loading images
    setupLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    // Notification system
    setupNotifications() {
        window.showNotification = (message, type = 'success') => {
            const notification = document.createElement('div');
            notification.className = `notification ${type}`;
            notification.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span>${message}</span>
                    <button onclick="this.parentElement.parentElement.remove()" style="background: none; border: none; font-size: 18px; cursor: pointer;">&times;</button>
                </div>
            `;
            
            document.body.appendChild(notification);
            
            setTimeout(() => notification.classList.add('show'), 100);
            setTimeout(() => {
                notification.classList.remove('show');
                setTimeout(() => notification.remove(), 300);
            }, 5000);
        };
    }
}

// Chat widget
class ChatWidget {
    constructor() {
        this.createWidget();
    }

    createWidget() {
        const widget = document.createElement('div');
        widget.innerHTML = `
            <div id="chat-widget" style="position: fixed; bottom: 100px; right: 30px; z-index: 1000;">
                <div id="chat-button" class="fab" style="background: #25d366;">
                    <i class="fab fa-whatsapp"></i>
                </div>
                <div id="chat-popup" style="display: none; position: absolute; bottom: 70px; right: 0; width: 300px; background: white; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); padding: 20px;">
                    <h4 style="margin: 0 0 15px 0; color: #333;">Chat with us!</h4>
                    <p style="margin: 0 0 15px 0; color: #666; font-size: 14px;">Hi there! How can we help you today?</p>
                    <div style="display: flex; gap: 10px;">
                        <a href="https://wa.me/27814109337" target="_blank" class="btn btn-success" style="flex: 1; text-align: center; padding: 10px; font-size: 12px;">
                            <i class="fab fa-whatsapp"></i> WhatsApp
                        </a>
                        <a href="tel:+27814109337" class="btn btn-primary" style="flex: 1; text-align: center; padding: 10px; font-size: 12px;">
                            <i class="fas fa-phone"></i> Call
                        </a>
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(widget);
        
        const button = document.getElementById('chat-button');
        const popup = document.getElementById('chat-popup');
        
        button.addEventListener('click', () => {
            popup.style.display = popup.style.display === 'none' ? 'block' : 'none';
        });
        
        document.addEventListener('click', (e) => {
            if (!widget.contains(e.target)) {
                popup.style.display = 'none';
            }
        });
    }
}

// Search functionality
class SearchFeature {
    constructor() {
        this.createSearchBar();
    }

    createSearchBar() {
        const searchHTML = `
            <div id="search-overlay" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 9999; backdrop-filter: blur(5px);">
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; max-width: 600px;">
                    <div style="background: white; border-radius: 15px; padding: 30px; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
                        <div style="display: flex; align-items: center; margin-bottom: 20px;">
                            <input type="text" id="search-input" placeholder="Search services, about us, contact..." style="flex: 1; padding: 15px; border: 2px solid #ddd; border-radius: 10px; font-size: 16px; outline: none;">
                            <button id="search-close" style="background: none; border: none; font-size: 24px; margin-left: 15px; cursor: pointer;">&times;</button>
                        </div>
                        <div id="search-results"></div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', searchHTML);
        
        // Add search trigger (Ctrl+K)
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'k') {
                e.preventDefault();
                this.openSearch();
            }
            if (e.key === 'Escape') {
                this.closeSearch();
            }
        });
        
        document.getElementById('search-close').addEventListener('click', () => this.closeSearch());
        document.getElementById('search-input').addEventListener('input', (e) => this.search(e.target.value));
    }

    openSearch() {
        document.getElementById('search-overlay').style.display = 'block';
        document.getElementById('search-input').focus();
    }

    closeSearch() {
        document.getElementById('search-overlay').style.display = 'none';
        document.getElementById('search-input').value = '';
        document.getElementById('search-results').innerHTML = '';
    }

    search(query) {
        if (query.length < 2) {
            document.getElementById('search-results').innerHTML = '';
            return;
        }

        const searchData = [
            { title: 'Web Development', url: '/services/', description: 'Professional web development services' },
            { title: 'Graphic Design', url: '/services/', description: 'Creative graphic design solutions' },
            { title: 'News Publishing', url: '/services/', description: 'The Highveld Chronicle news service' },
            { title: 'About Us', url: '/about/', description: 'Learn more about Myaba Media Tech' },
            { title: 'Contact', url: '/contact/', description: 'Get in touch with our team' },
            { title: 'Services', url: '/services/', description: 'All our professional services' }
        ];

        const results = searchData.filter(item => 
            item.title.toLowerCase().includes(query.toLowerCase()) ||
            item.description.toLowerCase().includes(query.toLowerCase())
        );

        const resultsHTML = results.map(item => `
            <div style="padding: 15px; border-bottom: 1px solid #eee; cursor: pointer;" onclick="window.location.href='${item.url}'">
                <h5 style="margin: 0 0 5px 0; color: #333;">${item.title}</h5>
                <p style="margin: 0; color: #666; font-size: 14px;">${item.description}</p>
            </div>
        `).join('');

        document.getElementById('search-results').innerHTML = results.length ? resultsHTML : '<p style="text-align: center; color: #666; padding: 20px;">No results found</p>';
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ModernUI();
    new ChatWidget();
    new SearchFeature();
    
    // Add keyboard shortcut hint
    const hint = document.createElement('div');
    hint.innerHTML = 'Press <kbd>Ctrl+K</kbd> to search';
    hint.style.cssText = 'position: fixed; bottom: 10px; left: 10px; background: rgba(0,0,0,0.7); color: white; padding: 5px 10px; border-radius: 5px; font-size: 12px; z-index: 999;';
    document.body.appendChild(hint);
    
    setTimeout(() => hint.style.opacity = '0.5', 3000);
});