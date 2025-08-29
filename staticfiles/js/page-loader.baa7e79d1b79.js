// Page Loader Fix
document.addEventListener('DOMContentLoaded', function() {
    // Ensure all pages load properly
    const main = document.getElementById('main-content');
    if (main) {
        main.classList.remove('page-loading');
        main.classList.add('page-content');
    }
    
    // Fix navigation issues
    const navLinks = document.querySelectorAll('a[href^="/"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!link.target || link.target === '_self') {
                const href = link.getAttribute('href');
                if (href && href !== '#') {
                    // Add loading state
                    if (main) {
                        main.classList.add('page-loading');
                    }
                    
                    // Navigate after short delay
                    setTimeout(() => {
                        window.location.href = href;
                    }, 100);
                }
            }
        });
    });
    
    // Remove loading screen if it exists
    const loadingScreen = document.querySelector('.loading-screen');
    if (loadingScreen) {
        setTimeout(() => {
            loadingScreen.style.opacity = '0';
            setTimeout(() => {
                loadingScreen.remove();
            }, 500);
        }, 1000);
    }
});