let favorite_bt = document.querySelectorAll(".favorite");
let watchNow_bt = document.querySelectorAll(".watchNow");
let wantWatch_bt = document.querySelectorAll(".wantWatch");
let watched_bt = document.querySelectorAll(".watched");
let input_anime_list_val = document.querySelector(
  "#user-profile-data-anime-sh input[type='text']"
);
let submit_anime_list_send = document.querySelector(
  "#user-profile-data-anime-sh input[type='submit']"
);
let anime_title = input_anime_list_val.getAttribute("anime_title");

// favorite
favorite_bt[0].addEventListener("click", function () {
  input_anime_list_val.value = `favorite$=>#${anime_title}`;
  submit_anime_list_send.click();
});
favorite_bt[1].addEventListener("click", function () {
  input_anime_list_val.value = `favorite$=>#${anime_title}`;
  submit_anime_list_send.click();
});
// watchNow
watchNow_bt[0].addEventListener("click", function () {
  input_anime_list_val.value = `watchNow$=>#${anime_title}`;
  submit_anime_list_send.click();
});
watchNow_bt[1].addEventListener("click", function () {
  input_anime_list_val.value = `watchNow$=>#${anime_title}`;
  submit_anime_list_send.click();
});
// wantWatch
wantWatch_bt[0].addEventListener("click", function () {
  input_anime_list_val.value = `wantWatch$=>#${anime_title}`;
  submit_anime_list_send.click();
});
wantWatch_bt[1].addEventListener("click", function () {
  input_anime_list_val.value = `wantWatch$=>#${anime_title}`;
  submit_anime_list_send.click();
});
// watched
watched_bt[0].addEventListener("click", function () {
  input_anime_list_val.value = `watched$=>#${anime_title}`;
  submit_anime_list_send.click();
});
watched_bt[1].addEventListener("click", function () {
  input_anime_list_val.value = `watched$=>#${anime_title}`;
  submit_anime_list_send.click();
});