const onLoad = () => {
  console.log("I'm working!!");

  const h1 = document.querySelector('h1');
  h1.style.cursor = 'pointer';
  h1.addEventListener(
      'click',
      (event) => {
          console.log(event);
          h1.style.color = 'blue';
      });

  const img = document.querySelector('img');
  img.style.cursor = 'pointer';
  img.addEventListener(
      "click",
      (event) => {
          console.log(event);
          img.style.height = '300px';
          img.style.width = '300px';
      });
}

// Run javascript after the DOM loads.
window.addEventListener("load", onLoad);
