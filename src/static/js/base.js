// toggle burgir menu //

const burgirBtn = document.getElementsByClassName("burgir")[0];
const menuShow = document.getElementsByClassName("menu")[0];

burgirBtn.addEventListener("click", () => {
  menuShow.classList.toggle("active");
});

//end burgir //
