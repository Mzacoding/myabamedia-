// Instant features that load immediately
(function() {
    'use strict';
    
    // Create loading screen immediately
    const loadingHTML = `
        <div class="loading-screen" id="loading-screen">
            <div class="loader"></div>
        </div>
    `;
    document.body.insertAdjacentHTML('afterbegin', loadingHTML);
    
    // Create scroll progress bar
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.id = 'scroll-progress';
    document.body.appendChild(progressBar);
    
    // Create theme toggle
    const themeToggle = document.createElement('div');
    themeToggle.className = 'theme-toggle';
    themeToggle.id = 'theme-toggle';
    themeToggle.title = 'Toggle Dark Mode';
    document.body.appendChild(themeToggle);
    
    // Create FAB
    const fab = document.createElement('a');
    fab.href = 'tel:+27814109337';
    fab.className = 'fab';
    fab.innerHTML = '<i class="fas fa-phone"></i>';
    fab.title = 'Call Us';
    document.body.appendChild(fab);
    
    // Create WhatsApp widget
    const whatsappWidget = document.createElement('div');
    whatsappWidget.innerHTML = `
        <div style="position: fixed; bottom: 100px; right: 30px; z-index: 1000;">
            <a href="https://wa.me/27814109337" target="_blank" class="fab" style="background: #25d366; bottom: 0;">
                <i class="fab fa-whatsapp"></i>
            </a>
        </div>
    `;
    document.body.appendChild(whatsappWidget);
    
    // Hide loading screen when page loads
    window.addEventListener('load', function() {
        setTimeout(function() {
            const loader = document.getElementById('loading-screen');
            if (loader) {
                loader.classList.add('hidden');
                setTimeout(() => loader.remove(), 500);
            }
        }, 1000);
    });
    
    // Scroll progress functionality
    window.addEventListener('scroll', function() {
        const progress = document.getElementById('scroll-progress');
        if (progress) {
            const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
            progress.style.width = scrolled + '%';
        }
    });
    
    // Theme toggle functionality
    document.addEventListener('click', function(e) {
        if (e.target.id === 'theme-toggle') {
            document.body.classList.toggle('dark-theme');
            e.target.classList.toggle('active');
            
            const isDark = document.body.classList.contains('dark-theme');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        }
    });
    
    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        const toggle = document.getElementById('theme-toggle');
        if (toggle) toggle.classList.add('active');
    }
    
    // Add particles
    function createParticles() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        document.body.appendChild(particlesContainer);

        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 6 + 's';
            particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
            particlesContainer.appendChild(particle);
        }
    }
    
    // Create particles after a short delay
    setTimeout(createParticles, 500);
    
    // Add CSS for theme toggle active state
    const style = document.createElement('style');
    style.textContent = `
        .theme-toggle::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            width: 21px;
            height: 21px;
            background: white;
            border-radius: 50%;
            transition: all 0.3s ease;
        }
        
        .theme-toggle.active {
            background: #667eea !important;
        }
        
        .theme-toggle.active::after {
            transform: translateX(25px);
        }
    `;
    document.head.appendChild(style);
    
})();