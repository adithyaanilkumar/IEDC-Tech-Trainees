

$(document).ready(function(){
    $(".back-to-top").hide();

    $(window).scroll(function () {
           if ($(this).scrollTop() > 100) {
               $('.back-to-top').fadeIn();
           } else {
               $('.back-to-top').fadeOut();
           }
       });
       // scroll body to 0px on click
       $('.back-to-top').click(function () {
           $('.back-to-top').tooltip('hide');
           $('body,html').animate({
               scrollTop: 0
           }, 800);
           return false;
       });
       
       $('.back-to-top').tooltip('show');

});

// Counter 
$(document).ready(function() {

    $('.counter').each(function () {
    $(this).prop('Counter',0).animate({
    Counter: $(this).text()
    }, {
    duration: 4000,
    easing: 'swing',
    step: function (now) {
    $(this).text(Math.ceil(now));
    }
    });
    });
    
    });

    AOS.init();