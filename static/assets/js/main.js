
const showMenu = (headerToggle, navbarId) => {
    const toggleBtn = document.getElementById(headerToggle),
        nav = document.getElementById(navbarId)

    // Validate that variables exist
    if (headerToggle && navbarId) {
        toggleBtn.addEventListener('click', () => {
            // We add the show-menu class to the div tag with the nav__menu class
            nav.classList.toggle('show-menu')
            // change icon
            toggleBtn.classList.toggle('bx-x')
        })
    }
}
showMenu('header-toggle', 'navbar')


const linkColor = document.querySelectorAll('.nav__link')

function colorLink() {
    linkColor.forEach(l => l.classList.remove('active'))
    this.classList.add('active')
}

linkColor.forEach(l => l.addEventListener('click', colorLink))



// Get references to elements
const helpButton = document.getElementById('helpButton');
const popupContainer = document.getElementById('popupContainer');
const closeButton = document.getElementById('closeButton');

// Open popup when Help button is clicked
helpButton.addEventListener('click', () => {
    popupContainer.style.display = 'flex';
});

// Close popup when Close button is clicked
closeButton.addEventListener('click', () => {
    popupContainer.style.display = 'none';
});
