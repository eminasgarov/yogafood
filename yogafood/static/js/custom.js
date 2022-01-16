/**************************************
    File Name: custom.js
    Template Name: RecipeList
    Created By: HTML.Design
    http://themeforest.net/user/wpdestek
**************************************/

(function ($) {
    "use strict";
    $(document).ready(function () {
        $('#nav-expander').on('click', function (e) {
            e.preventDefault();
            $('body').toggleClass('nav-expanded');
        });
        $('#nav-close').on('click', function (e) {
            e.preventDefault();
            $('body').removeClass('nav-expanded');
        });
    });

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    $('.carousel').carousel({
        interval: false
    })

    $(window).load(function () {
        $("#preloader").on(500).fadeOut();
        $(".preloader").on(600).fadeOut("slow");
    });

    jQuery(window).scroll(function () {
        if (jQuery(this).scrollTop() > 1) {
            jQuery('.dmtop').css({ bottom: "25px" });
        } else {
            jQuery('.dmtop').css({ bottom: "-100px" });
        }
    });
    jQuery('.dmtop').click(function () {
        jQuery('html, body').animate({ scrollTop: '0px' }, 800);
        return false;
    });

})(jQuery);

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 4000)


