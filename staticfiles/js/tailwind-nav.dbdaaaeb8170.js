// Tailwind Navigation JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menuToggle');
    const sideNav = document.getElementById('sideNav');
    const overlay = document.getElementById('overlay');
    const closeSideNav = document.getElementById('closeSideNav');
    
    function openMenu() {
        sideNav.classList.remove('translate-x-full');
        overlay.classList.remove('hidden');
        document.body.classList.add('overflow-hidden');
    }
    
    function closeMenu() {
        sideNav.classList.add('translate-x-full');
        overlay.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
    }
    
    if (menuToggle) {
        menuToggle.addEventListener('click', openMenu);
    }
    
    if (closeSideNav) {
        closeSideNav.addEventListener('click', closeMenu);
    }
    
    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }
    
    // Close menu when clicking nav links
    const navLinks = sideNav.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', closeMenu);
    });
});