// Premium Navigation JavaScript
class PremiumNavigation {
    constructor() {
        this.header = document.getElementById('header');
        this.menuToggle = document.getElementById('menuToggle');
        this.sideNav = document.getElementById('sideNav');
        this.overlay = document.getElementById('overlay');
        
        this.init();
    }

    init() {
        this.setupScrollEffects();
        this.setupMobileMenu();
        this.setupActiveLinks();
        this.setupSmoothScroll();
    }

    setupScrollEffects() {
        let lastScrollY = window.scrollY;
        
        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;
            
            // Add scrolled class for styling
            if (currentScrollY > 50) {
                this.header.classList.add('scrolled');
            } else {
                this.header.classList.remove('scrolled');
            }
            
            // Hide/show header on scroll
            if (currentScrollY > lastScrollY && currentScrollY > 100) {
                this.header.style.transform = 'translateY(-100%)';
            } else {
                this.header.style.transform = 'translateY(0)';
            }
            
            lastScrollY = currentScrollY;
        });
    }

    setupMobileMenu() {
        if (this.menuToggle && this.sideNav && this.overlay) {
            this.menuToggle.addEventListener('click', () => {
                this.toggleMobileMenu();
            });
            
            this.overlay.addEventListener('click', () => {
                this.closeMobileMenu();
            });
            
            // Close menu when clicking nav links
            const navLinks = this.sideNav.querySelectorAll('a');
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    this.closeMobileMenu();
                });
            });
        }
    }

    toggleMobileMenu() {
        this.menuToggle.classList.toggle('open');
        this.sideNav.classList.toggle('open');
        this.overlay.classList.toggle('active');
        document.body.classList.toggle('no-scroll');
    }

    closeMobileMenu() {
        this.menuToggle.classList.remove('open');
        this.sideNav.classList.remove('open');
        this.overlay.classList.remove('active');
        document.body.classList.remove('no-scroll');
    }

    setupActiveLinks() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav a, .side-nav a');
        
        navLinks.forEach(link => {
            const linkPath = new URL(link.href).pathname;
            if (linkPath === currentPath) {
                link.classList.add('active');
            }
        });
    }

    setupSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    const headerHeight = this.header.offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
}

// Enhanced Search Functionality
class EnhancedSearch {
    constructor() {
        this.searchOverlay = document.getElementById('search-overlay');
        this.searchInput = document.getElementById('search-input');
        this.searchResults = document.getElementById('search-results');
        this.searchClose = document.getElementById('search-close');
        
        this.init();
    }

    init() {
        this.setupSearchTriggers();
        this.setupSearchFunctionality();
    }

    setupSearchTriggers() {
        // Keyboard shortcut
        document.addEventListener('keydown', (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                this.openSearch();
            }
            if (e.key === 'Escape') {
                this.closeSearch();
            }
        });

        // Search trigger button
        const searchTrigger = document.querySelector('.search-trigger');
        if (searchTrigger) {
            searchTrigger.addEventListener('click', () => this.openSearch());
        }

        // Close button
        if (this.searchClose) {
            this.searchClose.addEventListener('click', () => this.closeSearch());
        }

        // Click outside to close
        if (this.searchOverlay) {
            this.searchOverlay.addEventListener('click', (e) => {
                if (e.target === this.searchOverlay) {
                    this.closeSearch();
                }
            });
        }
    }

    setupSearchFunctionality() {
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => {
                this.performSearch(e.target.value);
            });
        }
    }

    openSearch() {
        if (this.searchOverlay) {
            this.searchOverlay.style.display = 'block';
            setTimeout(() => {
                if (this.searchInput) {
                    this.searchInput.focus();
                }
            }, 100);
        }
    }

    closeSearch() {
        if (this.searchOverlay) {
            this.searchOverlay.style.display = 'none';
            if (this.searchInput) {
                this.searchInput.value = '';
            }
            if (this.searchResults) {
                this.searchResults.innerHTML = '';
            }
        }
    }

    async performSearch(query) {
        if (query.length < 2) {
            if (this.searchResults) {
                this.searchResults.innerHTML = '';
            }
            return;
        }

        try {
            const response = await fetch(`/api/search/?q=${encodeURIComponent(query)}`);
            const data = await response.json();
            this.displayResults(data.results);
        } catch (error) {
            console.error('Search error:', error);
            this.displayResults([]);
        }
    }

    displayResults(results) {
        if (!this.searchResults) return;

        if (results.length === 0) {
            this.searchResults.innerHTML = `
                <div style="text-align: center; padding: 40px; color: #666;">
                    <i class="fas fa-search" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.3;"></i>
                    <p>No results found. Try different keywords.</p>
                </div>
            `;
            return;
        }

        const resultsHTML = results.map(result => `
            <div class="search-result-item" onclick="window.location.href='${result.url}'" style="
                padding: 20px;
                border-bottom: 1px solid #eee;
                cursor: pointer;
                transition: background-color 0.2s ease;
            " onmouseover="this.style.backgroundColor='#f8f9fa'" onmouseout="this.style.backgroundColor='white'">
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <span class="badge badge-${result.type === 'service' ? 'primary' : 'secondary'}" style="margin-right: 10px; font-size: 0.7rem;">
                        ${result.type.toUpperCase()}
                    </span>
                    <h5 style="margin: 0; color: #2c3e50; font-size: 1.1rem;">${result.title}</h5>
                </div>
                <p style="margin: 0; color: #666; font-size: 0.9rem; line-height: 1.4;">${result.description}</p>
            </div>
        `).join('');

        this.searchResults.innerHTML = resultsHTML;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new PremiumNavigation();
    new EnhancedSearch();
    
    // Add scroll indicator for better UX
    const scrollIndicator = document.createElement('div');
    scrollIndicator.style.cssText = `
        position: fixed;
        bottom: 30px;
        left: 30px;
        width: 50px;
        height: 50px;
        background: rgba(102, 126, 234, 0.9);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        cursor: pointer;
        opacity: 0;
        transition: all 0.3s ease;
        z-index: 999;
        font-size: 20px;
    `;
    scrollIndicator.innerHTML = '<i class="fas fa-arrow-up"></i>';
    scrollIndicator.title = 'Back to top';
    document.body.appendChild(scrollIndicator);
    
    // Show/hide scroll to top button
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            scrollIndicator.style.opacity = '1';
            scrollIndicator.style.transform = 'scale(1)';
        } else {
            scrollIndicator.style.opacity = '0';
            scrollIndicator.style.transform = 'scale(0.8)';
        }
    });
    
    // Scroll to top functionality
    scrollIndicator.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});