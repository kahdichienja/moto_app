(function($) {
	"use strict";

	//-- Making the header fixed --
    var jQueryheader = $('.main-bar#main-bar');
    var jQueryheaderTop = jQueryheader.offset().top;

    $('.offset').height( jQueryheader.outerHeight() )
     
    //-- Window Scroll Functions --
       
    $(window).scroll(function(){
      ($(window).scrollTop() > jQueryheaderTop) ? $('.main-bar').addClass('fixedHeader') : jQuery('.main-bar').removeClass('fixedHeader');
    });
	
})(jQuery);