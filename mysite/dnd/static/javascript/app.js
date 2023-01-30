document.addEventListener("DOMContentLoaded", () => {
  const burger = document.querySelector(".nav")
  const nav_menu = document.querySelector('.nav-menu')
  const nav_close = document.querySelector('.menu-close')
  const character_race = document.getElementById("race")
  const character_subrace = document.getElementById("subrace")



  // Navigation
  function expand() {
    nav_menu.classList.add("expanded")
  }

  function collapse() {
    nav_menu.classList.remove("expanded")
  }


  burger.addEventListener('click', expand)
  nav_close.addEventListener('click', collapse)



});