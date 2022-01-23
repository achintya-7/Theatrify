// Header Scroll
let nav = document.querySelector(".navbar");

window.onscroll = () =>{
    if(document.documentElement.scrollTop > 20){
        nav.classList.add("header-scrolled");
    }else{
        nav.classList.remove("header-scrolled");
    }
}

// Nav hide
let navbar = document.querySelectorAll(".nav-link");
let navCollapse = document.querySelector(".navbar-collapse.collapse");
let mainBtn = document.querySelector(".main-btn");

navbar.forEach((a)=>{
    a.addEventListener("click", ()=>{
        navCollapse.classList.remove("show");
    });
});

mainBtn.addEventListener("click", ()=>{
    navCollapse.classList.remove("show");
});


