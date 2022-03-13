// title
title = document.querySelectorAll(".tc-js");
categories = document.querySelectorAll(".categorys .all a");

for (let i = 0; i < title.length; i++) {
  if (title[i].innerText.length > 10) {
    title[i].innerText = `${title[i].innerText.substring(0, 8)}..`;
  }
}

for (let i = 0; i < categories.length; i++) {
  if (categories[i].innerText.length > 7) {
    categories[i].innerText = `${categories[i].innerText.substring(0, 6)}`;
  }
}

// type
let anime_type = document.querySelectorAll(".type");
for (let index = 0; index < anime_type.length; index++) {
  if (anime_type[index].innerText == "حلقة خاصة") {
    anime_type[index].innerText = "خاصة";
  }
}
