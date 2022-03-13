// search filter
function episodes_search_filter() {
  let input = document.querySelector("#epispdeNumber");
  let ep = document.querySelectorAll(".episodes .all a");
  let null_ep = document.querySelector(".all .null-ep");
  input.onkeyup = function () {
    let none_ = 0;
    for (let i = 0; i < ep.length; i++) {
      if (ep[i].textContent.startsWith(input.value)) {
        ep[i].classList.remove("hide");
      } else {
        ep[i].classList.add("hide");
      }
      if (ep[i].classList.contains("hide")) {
        none_ += 1;
      }
    }
    if (none_ == ep.length) {
      null_ep.classList.remove("hide");
    } else {
      null_ep.classList.add("hide");
    }
  };
}
episodes_search_filter();
