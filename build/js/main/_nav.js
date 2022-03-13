// nav
function nav() {
  let icon_bars = document.getElementsByClassName("fa-bars")[0],
    icon_window_close = document.getElementsByClassName("fa-window-close"),
    right_nav = document.getElementsByClassName("right-nav")[0],
    icon_search = document.getElementsByClassName("fa-search")[0],
    shearch_box = document.getElementsByClassName("shearch")[0],
    menu_box = document.getElementsByClassName("menu")[0],
    icon_user = document.getElementsByClassName("fa-user-circle")[0],
    full = document.getElementsByClassName("full")[0],
    centent = document.querySelector(".container.full");

  // nav-right
  icon_bars.addEventListener("click", function () {
    // close shearch_box
    if (shearch_box.classList.contains("hide") == false) {
      shearch_box.classList.add("hide");
      icon_search.classList.remove("open");
    }
    // show right nav
    this.classList.add("hide");
    icon_window_close[0].classList.remove("hide");
    right_nav.classList.remove("close-nav");
    document.body.style.overflow = "hidden";
  });

  // close right nav
  icon_window_close[0].addEventListener("click", function () {
    this.classList.add("hide");
    icon_bars.classList.remove("hide");
    right_nav.classList.add("close-nav");
    document.body.style.overflow = "";
  });

  // close right nav
  centent.addEventListener("click", function () {
    icon_window_close[0].classList.add("hide");
    icon_bars.classList.remove("hide");
    right_nav.classList.add("close-nav");
    document.body.style.overflow = "";
  });

  // close right nav
  icon_search.addEventListener("click", function () {
    // close right nav
    if (right_nav.classList.contains("close-nav") == false) {
      icon_window_close[0].classList.add("hide");
      icon_bars.classList.remove("hide");
      right_nav.classList.add("close-nav");
    }
    // close menu box
    if (menu_box.classList.contains("hide") == false) {
      menu_box.classList.add("hide");
      icon_user.classList.remove("user-icon-bg");
    }

    // open or close shearch box at same shearch icon
    if (shearch_box.classList.contains("hide") == true) {
      this.classList.add("open");
      shearch_box.classList.remove("hide");
    } else {
      this.classList.remove("open");
      shearch_box.classList.add("hide");
    }
  });

  // close shearch box
  icon_window_close[1].addEventListener("click", function () {
    icon_search.classList.remove("open");
    shearch_box.classList.add("hide");
  });

  // menu
  icon_user.addEventListener("click", function () {
    // close shearch box
    if (shearch_box.classList.contains("hide") == false) {
      shearch_box.classList.add("hide");
      icon_search.classList.remove("open");
    }
    // show and close menu box
    if (menu_box.classList.contains("hide") == true) {
      menu_box.classList.remove("hide");
      this.classList.add("user-icon-bg");
    } else {
      menu_box.classList.add("hide");
      this.classList.remove("user-icon-bg");
    }
  });
  full.addEventListener("click", function () {
    menu_box.classList.add("hide");
    shearch_box.classList.add("hide");
    icon_search.classList.remove("open");
  });
}
nav();
