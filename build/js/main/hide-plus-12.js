// hede anime if length of all % 5 > 0

elements = document.querySelectorAll(".js-cut");
rows = document.querySelectorAll(".row");
for (var i = 0; i < rows.length; i++) {
  if (rows[i].querySelectorAll(".js-cut").length % 5 != 0) {
    len = rows[i].querySelectorAll(".js-cut").length;
    for (let ii = 1; ii <= len % 5; ii++) {
      rows[i]
        .querySelectorAll(".js-cut")
        [len - ii].classList.add("hide-plus-12");
    }
  }
}
