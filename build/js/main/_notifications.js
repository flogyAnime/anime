// hide notifications element after 5s
setTimeout(function () {
  document.querySelector(".notifications").style.opacity = 0;
}, 6000);

// user not logened
function user_not_her() {
  let not_2 = document.querySelector(".normal-notifications .id-02");
  not_2.classList.remove("hide");
  setTimeout(function () {
    not_2.classList.add("hide");
  }, 4000);
}
// photo not found to delete
function photo_not_found_to_delete() {
  let not_3 = document.querySelector(".normal-notifications .id-03");
  not_3.classList.remove("hide");
  setTimeout(function () {
    not_3.classList.add("hide");
  }, 4000);
}
// soon 
function soon() {
  let not_1 = document.querySelector(".normal-notifications .id-01");
  not_1.classList.remove("hide");
  setTimeout(function () {
    not_1.classList.add("hide");
  }, 4000);
}
