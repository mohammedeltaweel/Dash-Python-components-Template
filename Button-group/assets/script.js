function changeActiveBtn() {
    const toggleSelectBtns = document.querySelectorAll('.toggle-select-button'); 
    toggleSelectBtns.forEach(toggleSelectBtn => {
          toggleSelectBtn.addEventListener('click', function () {
  
              // Remove the "active" class from all buttons
              toggleSelectBtns.forEach(label => {
                  label.classList.remove('active');
              });
              // Add the "active" class to the clicked button
              toggleSelectBtn.classList.add('active');
          });
      });
  }