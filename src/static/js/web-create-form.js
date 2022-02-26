//the classes or id from services html

//the Overlay background layer
const overlay = document.getElementsByClassName("outside-layer")[0];

// the pop up/modal
const modalOpen = document.getElementsByClassName("theModal")[0];

//website button option
const websiteButton = document.getElementById("web-button");

//discord button
//const

//The close button
const closeModal = document.getElementById("close");

// Function for when clicking the button it will show the form
websiteButton.addEventListener("click", () => {
  overlay.classList.toggle("overlay");
  modalOpen.classList.toggle("active");
});

//x button when pressed
closeModal.addEventListener("click", () => {
  overlay.classList.toggle("overlay");
  modalOpen.classList.remove("active");
});

//when clicked outside it also closes
overlay.addEventListener("click", () => {
  overlay.classList.toggle("overlay");
  modalOpen.classList.remove("active");
});
