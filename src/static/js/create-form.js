// For the button "Add Project"
const addingButton = document.getElementById("adding");

// The overlay and container
const overlay = document.getElementById("overlay");
const modalContainer = document.getElementById("modalContainer");

// the Modal
const modal1 = document.getElementById("modal1");

// Modal 2
const modal2 = document.getElementById("modal2");

// The Next button
const next = document.getElementById("next-btn");

// Close button
const closeButton = document.getElementById("close");

// When clicking it opens Function
addingButton.addEventListener("click", () => {
  overlay.classList.toggle("active");
  modalContainer.classList.toggle("active");
  modal1.classList.toggle("open");
});

// for Next page
next.addEventListener("click", () => {
  modal2.classList.toggle("open");
  modal1.classList.toggle("open");
});

// Close button function
closeButton.addEventListener("click", () => {
  overlay.classList.toggle("active");
  modalContainer.classList.toggle("active");
  modal1.classList.toggle("open");
});

// when clicking outside it closes too
overlay.addEventListener("click", () => {
  modal1.classList.toggle("open");
  overlay.classList.toggle("active");
});
