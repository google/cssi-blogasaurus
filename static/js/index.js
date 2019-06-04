// Run javascript after the DOM loads.
window.onload = function() {
  console.log("I'm working!!");

  let h1 = document.querySelector('h1');
  h1.style.cursor = 'pointer';
  h1.onclick = function(event) {
    console.log(event);
    h1.style.color = 'blue';
  }

  let img = document.querySelector('img');
  img.style.cursor = 'pointer';
  img.onclick = function(event) {
    console.log(event);
    img.style.height = '300px';
    img.style.width = '300px';
  }
}
