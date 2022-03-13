function like_dislike_click() {
  let like_input = document.querySelector(".like_input");
  let deslike_input = document.querySelector(".deslike_input");
  let like = document.querySelectorAll(".like");
  let deslike = document.querySelectorAll(".deslike");
  let send = document.querySelector(".send-comment");
  let comment_id_data = document.querySelectorAll(".comment-id-data");
  let comment_id = document.querySelector(".comment-id");

  for (let i = 0; i < document.querySelectorAll(".comments .box").length; i++) {
    like[i].addEventListener("click", function () {
      like_input.value = "True";
      comment_id.value = comment_id_data[i].getAttribute("data");
      send.click();
    });
    deslike[i].addEventListener("click", function () {
      deslike_input.value = "True";
      comment_id.value = comment_id_data[i].getAttribute("data");
      send.click();
    });
  }
}
like_dislike_click();
