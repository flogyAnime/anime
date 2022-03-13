function send_comment_width() {
  let content = document.querySelector(".content");
  let chat = document.querySelector(".chat");
  setInterval(function () {
    chat.style.width = `${content.offsetWidth}px`;
  }, 0);
}

send_comment_width();
