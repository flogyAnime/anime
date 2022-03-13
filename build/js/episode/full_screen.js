let enter_full = document.querySelector(".fas.fa-expand");
let close_full = document.querySelector(".fas.fa-compress");
let iframe_ = document.querySelector("#iframe_video_db");
let dad = document.querySelector(".full-screen");

// mega
let mega_fullscreen = document.querySelector("#icon-fullscreen-enter");

// enter full screen fun
function openFullscreen(ele) {
  if (ele.requestFullscreen) {
    ele.requestFullscreen();
  } else if (ele.webkitRequestFullscreen) {
    /* Safari */
    ele.webkitRequestFullscreen();
  } else if (ele.msRequestFullscreen) {
    /* IE11 */
    ele.msRequestFullscreen();
  }
}

// clse full screen fun
function closeFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.webkitExitFullscreen) {
    /* Safari */
    document.webkitExitFullscreen();
  } else if (document.msExitFullscreen) {
    /* IE11 */
    document.msExitFullscreen();
  }
}

enter_full.addEventListener("click", function () {
  this.classList.add("hide");
  close_full.classList.remove("hide");
  iframe_.classList.add("height_full");
  openFullscreen(dad);
});

close_full.addEventListener("click", function () {
  this.classList.add("hide");
  enter_full.classList.remove("hide");
  iframe_.classList.remove("height_full");
  closeFullscreen();
});

// mega_fullscreen.addEventListener("click", function () {
//   this.classList.add("hide");
//   enter_full.classList.remove("hide");
//   openFullscreen();
// });
