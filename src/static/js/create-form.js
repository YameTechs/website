// For the button "Add Project"
const addingButton = document.getElementById("adding");

// The overlay
const overlay = document.getElementById("overlay");

// the Modal
const modal = document.getElementById("modalForm");

// Close button
const closeButton = document.getElementById("close");

//Close button function
closeButton.addEventListener("click", () => {
  overlay.classList.toggle("active");
  modal.classList.toggle("open");
});

// When clicking it opens Function
addingButton.addEventListener("click", () => {
  overlay.classList.toggle("active");
  modal.classList.toggle("open");
});
