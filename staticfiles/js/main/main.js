elements=document.querySelectorAll(".js-cut"),rows=document.querySelectorAll(".row");for(var i=0;i<rows.length;i++)if(rows[i].querySelectorAll(".js-cut").length%5!=0){len=rows[i].querySelectorAll(".js-cut").length;for(let e=1;e<=len%5;e++)rows[i].querySelectorAll(".js-cut")[len-e].classList.add("hide-plus-12")}function nav(){let e=document.getElementsByClassName("fa-bars")[0],s=document.getElementsByClassName("fa-window-close"),t=document.getElementsByClassName("right-nav")[0],i=document.getElementsByClassName("fa-search")[0],a=document.getElementsByClassName("shearch")[0],l=document.getElementsByClassName("menu")[0],n=document.getElementsByClassName("fa-user-circle")[0],c=document.getElementsByClassName("full")[0],o=document.querySelector(".container.full");e.addEventListener("click",(function(){0==a.classList.contains("hide")&&(a.classList.add("hide"),i.classList.remove("open")),this.classList.add("hide"),s[0].classList.remove("hide"),t.classList.remove("close-nav"),document.body.style.overflow="hidden"})),s[0].addEventListener("click",(function(){this.classList.add("hide"),e.classList.remove("hide"),t.classList.add("close-nav"),document.body.style.overflow=""})),o.addEventListener("click",(function(){s[0].classList.add("hide"),e.classList.remove("hide"),t.classList.add("close-nav"),document.body.style.overflow=""})),i.addEventListener("click",(function(){0==t.classList.contains("close-nav")&&(s[0].classList.add("hide"),e.classList.remove("hide"),t.classList.add("close-nav")),0==l.classList.contains("hide")&&(l.classList.add("hide"),n.classList.remove("user-icon-bg")),1==a.classList.contains("hide")?(this.classList.add("open"),a.classList.remove("hide")):(this.classList.remove("open"),a.classList.add("hide"))})),s[1].addEventListener("click",(function(){i.classList.remove("open"),a.classList.add("hide")})),n.addEventListener("click",(function(){0==a.classList.contains("hide")&&(a.classList.add("hide"),i.classList.remove("open")),1==l.classList.contains("hide")?(l.classList.remove("hide"),this.classList.add("user-icon-bg")):(l.classList.add("hide"),this.classList.remove("user-icon-bg"))})),c.addEventListener("click",(function(){l.classList.add("hide"),a.classList.add("hide"),i.classList.remove("open")}))}function user_not_her(){let e=document.querySelector(".normal-notifications .id-02");e.classList.remove("hide"),setTimeout((function(){e.classList.add("hide")}),4e3)}function photo_not_found_to_delete(){let e=document.querySelector(".normal-notifications .id-03");e.classList.remove("hide"),setTimeout((function(){e.classList.add("hide")}),4e3)}function soon(){let e=document.querySelector(".normal-notifications .id-01");e.classList.remove("hide"),setTimeout((function(){e.classList.add("hide")}),4e3)}function register(e){let s=document.getElementsByClassName("signupBt"),t=document.getElementsByClassName("loginBt"),i=document.querySelector(".signup"),a=document.querySelector(".login"),l=document.querySelector(".container.full");s[e].addEventListener("click",(function(){0==i.classList.contains("hide")?(this.classList.remove("this"),i.classList.add("hide"),l.classList.remove("opacity"),document.querySelector("body").style.overflowX="hidden"):(this.classList.add("this"),t[e].classList.remove("this"),i.classList.remove("hide"),l.classList.add("opacity"),a.classList.add("hide"))})),t[e].addEventListener("click",(function(){0==a.classList.contains("hide")?(this.classList.remove("this"),a.classList.add("hide"),l.classList.remove("opacity"),document.querySelector("body").style.overflowX="hidden"):(this.classList.add("this"),s[e].classList.remove("this"),a.classList.remove("hide"),l.classList.add("opacity"),i.classList.add("hide"))}))}nav(),setTimeout((function(){document.querySelector(".notifications").style.opacity=0}),6e3),register(0),register(1),title=document.querySelectorAll(".tc-js"),categories=document.querySelectorAll(".categorys .all a");for(let e=0;e<title.length;e++)title[e].innerText.length>10&&(title[e].innerText=`${title[e].innerText.substring(0,8)}..`);for(let e=0;e<categories.length;e++)categories[e].innerText.length>7&&(categories[e].innerText=`${categories[e].innerText.substring(0,6)}`);let anime_type=document.querySelectorAll(".type");for(let e=0;e<anime_type.length;e++)"حلقة خاصة"==anime_type[e].innerText&&(anime_type[e].innerText="خاصة");let passwords=document.querySelectorAll(".jspass"),username=document.querySelectorAll(".jsname"),submit=document.querySelectorAll(".jssubmit"),email=document.querySelectorAll(".jsemail");function CheckPassword(e){String(e.value).length>=8&&String(e.value).length<=30?e.classList.remove("input-error"):e.classList.add("input-error")}function CheckUsername(e){String(e.value).length>=3&&String(e.value).length<=20?e.classList.remove("input-error"):e.classList.add("input-error")}function ValidateEmail(e){e.value.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)?e.classList.remove("input-error"):e.classList.add("input-error")}setInterval((function(){""!=passwords[0].value&&(passwords[0].onkeyup=CheckPassword(passwords[0])),""!=passwords[1].value&&(passwords[1].onkeyup=CheckPassword(passwords[1])),""!=username[0].value&&(username[0].onkeyup=CheckUsername(username[0])),""!=email[0].value&&(email[0].onkeyup=ValidateEmail(email[0])),""!=email[1].value&&(email[1].onkeyup=ValidateEmail(email[1])),passwords[1].classList.contains("input-error")||email[1].classList.contains("input-error")?(submit[1].classList.add("submit-disactive"),submit[1].disabled=!0):(submit[1].classList.remove("submit-disactive"),submit[1].disabled=!1),passwords[0].classList.contains("input-error")||username[0].classList.contains("input-error")||email[0].classList.contains("input-error")?(submit[0].classList.add("submit-disactive"),submit[0].disabled=!0):(submit[0].classList.remove("submit-disactive"),submit[0].disabled=!1)}),500);
//# sourceMappingURL=../../maps/js/main.js.map
