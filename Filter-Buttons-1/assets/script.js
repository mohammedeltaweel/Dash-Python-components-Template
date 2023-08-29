function setupFilterElements() {
  // Get all filter-dot and filter-text elements
  const filterDotElements = document.querySelectorAll(".filter-dot");
  const filterTextElements = document.querySelectorAll(".filter-text");

  // Function to update class names when a filter-dot or filter-text element is clicked
  function updateClassNames(event) {
    // Toggle the active class on the clicked element
    event.target.classList.toggle("active");

    // Check if the clicked element is a filter-dot or filter-text
    const isDotElement = event.target.classList.contains("filter-dot");
    const isTextElement = event.target.classList.contains("filter-text");

    // If the clicked element is a filter-dot, update the corresponding filter-text element
    if (isDotElement) {
      const index = Array.from(filterDotElements).indexOf(event.target);
      if (index !== -1) {
        filterTextElements[index].classList.toggle("active");
      }
    }

    // If the clicked element is a filter-text, update the corresponding filter-dot element
    if (isTextElement) {
      const index = Array.from(filterTextElements).indexOf(event.target);
      if (index !== -1) {
        filterDotElements[index].classList.toggle("active");
      }
    }
  }

  // Add click event listeners to all filter-dot elements
  filterDotElements.forEach((dot) => {
    dot.addEventListener("click", updateClassNames);
  });

  // Add click event listeners to all filter-text elements
  filterTextElements.forEach((text) => {
    text.addEventListener("click", updateClassNames);
  });
}

