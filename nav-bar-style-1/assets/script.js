function setupNavbarFunctionality() {
    const menuBtn = document.querySelector(".menu-icon span");
    const searchBtn = document.querySelector(".search-icon");
    const cancelBtn = document.querySelector(".cancel-icon");
    const items = document.querySelector(".main-nav-items");
    const form = document.querySelector("form");
  
    menuBtn.onclick = () => {
        items.classList.add("active");
        menuBtn.classList.add("hide");
        searchBtn.classList.add("hide");
        cancelBtn.classList.add("show");
    };
  
    cancelBtn.onclick = () => {
        items.classList.remove("active");
        menuBtn.classList.remove("hide");
        searchBtn.classList.remove("hide");
        cancelBtn.classList.remove("show");
        form.classList.remove("active");
        cancelBtn.style.color = "#ff3d00";
    };
  
    searchBtn.onclick = () => {
        form.classList.add("active");
        searchBtn.classList.add("hide");
        cancelBtn.classList.add("show");
    };
  
    // Set up clientside callback to update active class based on URL pathname
    const updateActiveLink = () => {
        const pathname = window.location.pathname;
        const navLinks = document.querySelectorAll(".main-nav-items li");
  
        navLinks.forEach((link) => {
            if (link.querySelector("a").getAttribute("href") === pathname) {
                link.classList.add("active");
            } else {
                link.classList.remove("active");
            }
        });
    };
  
    // Call the updateActiveLink function initially and whenever the URL changes
    updateActiveLink();
    window.addEventListener("popstate", updateActiveLink);
  }
  

  function changeNavStyle (){
    const primaryHeader = document.querySelector(".main-navigation");
    const scrollWatcher = document.createElement("div");
    scrollWatcher.setAttribute("data-scroll-watcher", "");
    
    primaryHeader.before(scrollWatcher);
    
    const navObserver = new IntersectionObserver((entries) =>{
        primaryHeader.classList.toggle("sticking", !entries[0].isIntersecting);
    }, {rootMargin: "100px 0px 0px 0px"});
    navObserver.observe(scrollWatcher);
    }