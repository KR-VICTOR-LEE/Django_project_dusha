window.addEventListener("scroll", function() {
  var topButton = document.getElementById("topButton");
  if (document.documentElement.scrollTop > 200) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
});

document.getElementById("topButton").addEventListener("click", function() {
  document.documentElement.scrollTop = 0;
});