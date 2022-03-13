let watch_url = document.querySelector("#watch_db");
let iframe = document.querySelector("#iframe_video_db");
let download_d = document.querySelector("#download_this_ep");

function iframe_url() {
  let data = document.querySelector(`#${watch_url.value}`);

  if (iframe.src != data.getAttribute("watch")) {
    iframe.src = data.getAttribute("watch");
  }
  if (download_d.href != data.getAttribute("download")) {
    download_d.href = data.getAttribute("download");
  }
}
setInterval(iframe_url, 500);
