// register
function register(index) {
  let signupBt = document.getElementsByClassName("signupBt");
  let loginBt = document.getElementsByClassName("loginBt");
  let signupbox = document.querySelector(".signup");
  let loginbox = document.querySelector(".login");
  let content_ = document.querySelector(".container.full");

  // sign up
  signupBt[index].addEventListener("click", function () {
    if (signupbox.classList.contains("hide") == false) {
      this.classList.remove("this");
      signupbox.classList.add("hide");
      content_.classList.remove("opacity");
      document.querySelector("body").style.overflowX = "hidden";
    } else {
      this.classList.add("this");
      loginBt[index].classList.remove("this");
      signupbox.classList.remove("hide");
      content_.classList.add("opacity");
      loginbox.classList.add("hide");
    }
  });

  // login
  loginBt[index].addEventListener("click", function () {
    if (loginbox.classList.contains("hide") == false) {
      this.classList.remove("this");
      loginbox.classList.add("hide");
      content_.classList.remove("opacity");
      document.querySelector("body").style.overflowX = "hidden";
    } else {
      this.classList.add("this");
      signupBt[index].classList.remove("this");
      loginbox.classList.remove("hide");
      content_.classList.add("opacity");
      signupbox.classList.add("hide");
    }
  });
}

register(0);
register(1);
