// BACK TO THE TOP BUTTON
var btn = $('#button');

$(window).scroll(function () {
    if ($(window).scrollTop() > 300) {
        btn.addClass('show');
    } else {
        btn.removeClass('show');
    }
});

btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({ scrollTop: 0 }, '300');
});






// let logoBox = document.querySelector(".logo");
// {/* <i class='bx bx-x'></i> */ }


// logoBox.addEventListener("mouseover", () => {
//     navbar.classList.toggle("showInput");
//     if (navbar.classList.contains("showInput")) {
//         logoBox.classList.replace("logo", "logo2")
//     } else {

//         logoBox.classList.replace("logo2", "logo")

//     }
// })