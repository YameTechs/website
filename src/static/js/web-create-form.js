//the classes or id from services html

//the Overlay background layer
const overlay = document.getElementsByClassName("outside-layer")[0];

// Website Modal
const webModal = document.getElementById("web-form");

// Discord Modal
const dcModal = document.getElementById("web-form2");

//website button option
const websiteButton = document.getElementById("web-button");

//discord button
const discordButton = document.getElementById("dc-btn");

//The close button
const closeModal = document.getElementById("close");
const closeModal2 = document.getElementById("close2");

// Function for when clicking the Website button it will show the form
websiteButton.addEventListener("click", () => {
  overlay.classList.toggle("overlay");
  webModal.classList.toggle("active");
  closeModal.classList.add("active");
});

// Function for when clicking the Discord Button
discordButton.addEventListener("click", () => {
  overlay.classList.toggle("overlay");
  dcModal.classList.toggle("active");
});

// x button (Web) when pressed it should close
closeModal.addEventListener("click", () => {
  overlay.classList.remove("overlay");
  webModal.classList.remove("active");
});

// x button (DcBot) when pressed it should close
closeModal2.addEventListener("click", () => {
  overlay.classList.remove("overlay");
  dcModal.classList.remove("active");
});

// when clicked outside it also closes
overlay.addEventListener("click", () => {
  overlay.classList.remove("overlay");
  webModal.classList.remove("active");
  dcModal.classList.remove("active");
});
