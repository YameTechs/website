// toggle burgir menu //

const burgirBtn = document.getElementsByClassName('burgir')[0]
const menuShow = document.getElementsByClassName('menu')[0]

burgirBtn.addEventListener('click', () => {
  menuShow.classList.toggle('active')
})

//end gurgir //


// dropdown //

const UserAcc = document.getElementsByClassName('user_acc')[0]
const UserAccContent = document.getElementsByClassName('dropdown')[0]

UserAcc.addEventListener('click', () => {
  UserAccContent.classList.toggle('active')
})
// end dropdown // 