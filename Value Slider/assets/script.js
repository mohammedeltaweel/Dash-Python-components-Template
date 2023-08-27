function sliderValShow() {
  
  const rangeInput = document.querySelector('.range-input input');


  // Get the labels

  const labels = document.querySelectorAll('.range-labels-item'); 
  // Add a click event listener to the labels

  labels.forEach(label => {
      label.addEventListener('click', function () {
        console.log(label);

          // Get the year value from the clicked label
          const selectedYear = parseInt(label.textContent);
          // Set the value of the input to the selected year
          rangeInput.value = selectedYear;

          // Remove the "active" class from all labels
          labels.forEach(label => {
              label.classList.remove('active');
          });
          // Add the "active" class to the clicked label
          label.classList.add('active');
      });
  });

  // Add an input event listener to update the labels when the input value changes
  rangeInput.addEventListener('input', function () {
      // Get the selected year value
      const selectedYear = parseInt(rangeInput.value);

      // Remove the "active" class from all labels
      labels.forEach(label => {
          label.classList.remove('active');
      });

      // Add the "active" class to the corresponding label
      const correspondingLabel = document.querySelector(`.item-${selectedYear}`);

      if (correspondingLabel) {
          correspondingLabel.classList.add('active');
      }
  });
}