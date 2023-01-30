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

  

// Character creation subrace change
  function subracechange() {
      while (character_subrace.lastChild) {
        character_subrace.removeChild(character_subrace.lastChild)
      }
      a = document.querySelector(".race").value
      data[a].forEach(item => {
        var selection = document.createElement("OPTION")
        var text = document.createTextNode(item)
        selection.appendChild(text)
        selection.setAttribute("value", item)
        character_subrace.appendChild(selection)
      });
      }
    
  character_race.addEventListener('change', subracechange)

});