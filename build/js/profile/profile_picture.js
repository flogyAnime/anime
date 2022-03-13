function profile_picture() {
  let box = document.querySelector(".main .logo .box");
  let main_photo = document.querySelector(".main .logo img");
  let change = document.querySelector(".main .logo .box .changeImg");
  let delet = document.querySelector(".main .logo .box .deletImg");
  let back = document.querySelector(".main .logo .box .back_");
  let profile_picture = document.querySelector(
    "input[name='change_profile_picture']"
  );
  let delet_profile_picture = document.querySelector(
    "input[name='delet_profile_picture']"
  );
  let submit = document.querySelector(".save_profile_picture");

  main_photo.addEventListener("click", function () {
    box.classList.remove("hide");
  });

  change.addEventListener("click", function () {
    profile_picture.click();
    let loop = setInterval(function () {
      if (profile_picture.files.length == 1) {
        submit.click();
        clearInterval(loop);
      }
    }, 1000);
  });

  delet.addEventListener("click", function () {
    if (delet.getAttribute("statu") != "turn-of") {
      delet_profile_picture.value = "True";
      submit.click();
    }
  });

  back.addEventListener("click", function () {
    box.classList.add("hide");
  });
}
profile_picture();
