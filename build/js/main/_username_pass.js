let passwords = document.querySelectorAll(".jspass");
let username = document.querySelectorAll(".jsname");
let submit = document.querySelectorAll(".jssubmit");
let email = document.querySelectorAll(".jsemail");

// pass and username
function CheckPassword(val) {
  // var str = /^[A-Za-z]\w{3,15}$/;
  if (String(val.value).length >= 8 && String(val.value).length <= 30) {
    val.classList.remove("input-error");
  } else {
    val.classList.add("input-error");
  }
}

function CheckUsername(val) {
  if (String(val.value).length >= 3 && String(val.value).length <= 20) {
    val.classList.remove("input-error");
  } else {
    val.classList.add("input-error");
  }
}

// email
function ValidateEmail(val) {
  var str = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (val.value.match(str)) {
    val.classList.remove("input-error");
  } else {
    val.classList.add("input-error");
  }
}

// call
setInterval(function () {
  // pass
  if (passwords[0].value != "") {
    passwords[0].onkeyup = CheckPassword(passwords[0]);
  }

  if (passwords[1].value != "") {
    passwords[1].onkeyup = CheckPassword(passwords[1]);
  }

  // username
  if (username[0].value != "") {
    username[0].onkeyup = CheckUsername(username[0]);
  }

  // email
  if (email[0].value != "") {
    email[0].onkeyup = ValidateEmail(email[0]);
  }

  if (email[1].value != "") {
    email[1].onkeyup = ValidateEmail(email[1]);
  }

  // submit
  if (
    passwords[1].classList.contains("input-error") ||
    email[1].classList.contains("input-error")
  ) {
    submit[1].classList.add("submit-disactive");
    submit[1].disabled = true;
  } else {
    submit[1].classList.remove("submit-disactive");
    submit[1].disabled = false;
  }

  if (
    passwords[0].classList.contains("input-error") ||
    username[0].classList.contains("input-error") ||
    email[0].classList.contains("input-error")
  ) {
    submit[0].classList.add("submit-disactive");
    submit[0].disabled = true;
  } else {
    submit[0].classList.remove("submit-disactive");
    submit[0].disabled = false;
  }
}, 500);
