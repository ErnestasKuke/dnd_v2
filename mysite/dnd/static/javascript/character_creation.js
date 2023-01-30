document.addEventListener("DOMContentLoaded", () => {
  const character_race = document.getElementById("race")
  const character_subrace = document.getElementById("subrace")


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