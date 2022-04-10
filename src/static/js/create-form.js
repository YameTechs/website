// For the button "Add Project"
const addingButton = document.getElementById("adding");
// The overlay
const overlay = document.getElementById("overlay");
// the Modal
const modal = document.getElementById("modalForm");

// Close button
const closeButton = document.getElementById("close");
// When clicking it opens
addingButton.addEventListener("click", () => {
  overlay.classList.toggle("open");
  modal.classList.toggle("open");
});
