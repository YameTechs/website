// toggle burgir menu //

const burgirBtn = document.getElementsByClassName("burgir")[0];
const menuShow = document.getElementsByClassName("menu")[0];
const userAccMenu_Show = document.getElementsByClassName("userAcc_menu2")[0];
const navChange = document.getElementsByClassName("navbar")[0];

burgirBtn.addEventListener("click", () => {
  navChange.classList.toggle("clicked");
  menuShow.classList.toggle("active");
  userAccMenu_Show.classList.toggle("active");
});

//end gurgir //
