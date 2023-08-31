function activateNavigation() {
    const navLinks = document.querySelectorAll(".nav-dot");
    const sections = document.querySelectorAll(".section");
    let preventObserver = false; // Flag to prevent Intersection Observer from updating the navigation dots
  
    // Function to remove "nav-dot-selected" class from all navigation dots
    function clearSelectedNav() {
      navLinks.forEach((navLink) => {
        navLink.classList.remove("nav-dot-selected");
      });
    }
  
    // Function to update the selected navigation dot
    function updateSelectedNav(navLink) {
      clearSelectedNav();
      navLink.classList.add("nav-dot-selected");
    }
  
    // Function to handle the click on the navigation bar
    function handleNavClick(event) {
      event.preventDefault(); // Prevent the default jump-to behavior
      const clickedNavLink = event.target.closest(".nav-dot");
  
      if (clickedNavLink && !preventObserver) {
        // If a valid navigation link is clicked and the Observer is not prevented
        preventObserver = true; // Prevent the Observer from updating the dots temporarily
        updateSelectedNav(clickedNavLink); // Update the selected navigation dot immediately
  
        // After a short delay, reset the flag to allow the Observer to work again
        setTimeout(() => {
          preventObserver = false;
        }, 700); // You can adjust the delay (in milliseconds) as needed
  
        // Scroll to the corresponding section
        const targetSectionId = clickedNavLink.getAttribute("href").substring(1);
        const targetSection = document.getElementById(targetSectionId);
        if (targetSection) {
          targetSection.scrollIntoView({ behavior: "smooth" });
        }
      }
    }
  
    // Add a click event listener to the entire navigation bar
    document.querySelector(".nav").addEventListener("click", handleNavClick);
  
    // Intersection Observer callback function
    function handleIntersection(entries, observer) {
      if (preventObserver) return; // If Observer is prevented, skip the intersection handling
  
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const targetSectionId = entry.target.getAttribute("id");
          const correspondingNavLink = document.querySelector(`[href="#${targetSectionId}"]`);
          if (correspondingNavLink) {
            updateSelectedNav(correspondingNavLink);
          }
        }
      });
    }
  
    // Create Intersection Observer
    const observer = new IntersectionObserver(handleIntersection, {
      rootMargin: "0px",
      threshold: 0.5,
    });
  
    // Observe each section
    sections.forEach((section) => {
      observer.observe(section);
    });
  }
  

  const sections = document.querySelectorAll("section");
const originalHs = document.querySelectorAll(".section .class1");

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry =>{

        entry.target.classList.toggle("show", entry.isIntersecting);
        setTimeout(() => {
            const sectionid = document.querySelector(".section.show");
            const hs = document.querySelector(".section.show .class1");
            const divs = document.querySelector(".section.show .class2");
            originalHs.forEach(originalh => {
                originalh.classList.remove("class3");
            })
            hs.classList.add("class3");
        }, 50); // You can adjust the delay (in milliseconds) as needed
  

    })
}, {
    threshold: 0.5
})
sections.forEach(section => {
    observer.observe(section);
})
