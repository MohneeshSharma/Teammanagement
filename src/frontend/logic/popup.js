const buttonsContainer = document.querySelector('.content-sections');
const popups = document.querySelectorAll('.popup');


buttonsContainer.addEventListener('click', (event) => {
  const target = event.target;

  // Handle button clicks to open corresponding popups
  if (target.matches('#add-user-btn')) {
    document.getElementById('add-user-popup').style.display = 'block';
  } else if (target.matches('#remove-user-btn')) {
    document.getElementById('remove-user-popup').style.display = 'block';
  } else if (target.matches('.section-buttons:nth-child(2) button')) {
    document.getElementById('assign-task-popup').style.display = 'block';
  } else if (target.matches('.section-buttons:nth-child(3) button')) {
    document.getElementById('view-tasks-popup').style.display = 'block';
  }

  // Add a class to the body to indicate the popup is active
  body.classList.add('popup-active');
});

// Handle close icon clicks to hide popups
popups.forEach((popup) => {
  const closeButton = popup.querySelector('.close-btn');

  closeButton.addEventListener('click', () => {
    popup.style.display = 'none';
    // Remove the class from the body when the popup is closed
    body.classList.remove('popup-active');
  });
});

// Hide all popups when the page loads
window.addEventListener('DOMContentLoaded', () => {
  popups.forEach((popup) => {
    popup.style.display = 'none';
  });
});
