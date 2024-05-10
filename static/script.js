const wrapper = document.querySelector('.wrapper');
const loginlink = document.querySelector('.login-link');
const registerlink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnlogin-popup');
const iconClose = document.querySelector('.icon-close');
var contactLink = document.getElementById("contactlink");
var aboutLink = document.getElementById("aboutlink");

registerlink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});

loginlink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click',()=>{
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
});

function handleContactClick(){
    window.location.href="contact.html";
}
contactLink.addEventListener("click",handleContactClick);

function handleaboutClick(){
    window.location.href="about.html";
}
aboutLink.addEventListener("click",handleaboutClick);



function Auth() {
    var username = document.getElementById("mail");
    var Password = document.getElementById("password");
    if (username === "admin@gmail" && Password === "admin") {
        // Redirect the user to the dashboard page.
        window.location.href = "/dashboard.html";
      } else {
        // Display an error message.
        alert("Invalid username or password.");
      }
    }

