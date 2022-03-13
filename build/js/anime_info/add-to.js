function add_to() {
  let add_to = document.querySelectorAll(".add-to");
  let box = document.querySelectorAll(".menu-setting-ab");

  add_to[0].addEventListener("click", function () {
    if (box[0].classList.contains("hide")) {
      box[0].classList.remove("hide");
    } else {
      box[0].classList.add("hide");
    }
  });

  add_to[1].addEventListener("click", function () {
    if (box[1].classList.contains("hide")) {
      box[1].classList.remove("hide");
    } else {
      box[1].classList.add("hide");
    }
  });
}

add_to();
