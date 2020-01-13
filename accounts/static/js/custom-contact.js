//Global var
var INSPIRO = {};
(function($) {
	"use strict";

	//Preloader
    $(window).load(function() {
        $('.images-preloader').fadeOut();
    });
    
	

    //Position Navigation

    $(window).on('resize', function () {
        var hbar = $('.site-header').outerHeight(),
            sbar = $('header .sub-bar').height();
        $('.main-bar .nav').css('top', hbar);
        $("header .main-bar").css('top', sbar);
    }).trigger('resize');
    
    (function($) {
        $(document).ready(function() {
            $(window).load(function() {
            $('.nav_slide_button').on('click',function() {
              $('.top-search').slideToggle();

            });
            $('#search-delete').on('click',function() {
              $(".top-search").slideUp("slow");
            });
          });
            
        document.querySelector("#search-toggle").addEventListener("click", function() {
            this.classList.toggle("active");
          });
        });
    }(window.jQuery || window.$));
    // Menu Mobile
	
	$('.btn-toggle').on('click',function(){

		var parent = $(this).parents('header');
		if(parent.find('nav').hasClass('menu-mobile')){
            parent.find('nav').removeClass('menu-mobile');
        }else{
            parent.find('nav').addClass('menu-mobile');
        }

        if(parent.find('.top-info').hasClass('menu-mobile')){
            parent.find('.top-info').removeClass('menu-mobile');
        }else{
            parent.find('.top-info').addClass('menu-mobile');
        }

	});
	
	//Submenu Dropdown Toggle
    if($('.site-header li.menu-item-has-children ul').length){
        $('.site-header li.menu-item-has-children').append('<div class="dropdown-btn"><Span class="fa fa-angle-down"></span></div>');

        //Dropdown Button
        $('.site-header li.menu-item-has-children .dropdown-btn').on('click', function() {
            $(this).prev('ul').slideToggle(500);
        });

        //Disable dropdown parent link
        $('.navigation li.menu-item-has-children > a').on('click', function(e) {
            e.preventDefault();
        });
    }

	//Validate Contact Form

	$('.contact-form #submit').on('click',function(){ // when the button is clicked the code executes
		$('.error').fadeOut('slow'); // reset the error messages (hides them)

		var error = false; // we will set this true if the form isn't valid

		var name = $('input#name').val(); // get the value of the input field
		if(name == "" || name == " ") {
			$('#err-name').fadeIn('slow'); // show the error message
			error = true; // change the error state to true
		}

		var email_compare = /^([a-z0-9_.-]+)@([da-z.-]+).([a-z.]{2,6})$/; // Syntax to compare against input
		var email = $('input#email').val(); // get the value of the input field
		if (email == "" || email == " ") { // check if the field is empty
			$('#err-email').fadeIn('slow'); // error - empty
			error = true;
		}else if (!email_compare.test(email)) { // if it's not empty check the format against our email_compare variable
			$('#err-emailvld').fadeIn('slow'); // error - not right format
			error = true;
		}

		if(error == true) {
			$('#err-form').slideDown('slow');
			return false;
		}

		var data_string = $('#ajax-form').serialize(); // Collect data from form

		$.ajax({
			type: "POST",
			url: $('#ajax-form').attr('action'),
			data: data_string,
			timeout: 6000,
			error: function(request,error) {
				if (error == "timeout") {
					$('#err-timedout').slideDown('slow');
				}
				else {
					$('#err-state').slideDown('slow');
					$("#err-state").html('An error occurred: ' + error + '');
				}
			},
			success: function() {
				$('#ajaxsuccess').slideDown('slow');
			}
		});

		return false; // stops user browser being directed to the php file
	}); // end click function
	

	jQuery(document).ready(function($){
        $('[data-toggle="tooltip"]').tooltip();   
    });
    jQuery(document).ready(function($){
        $('[data-toggle="popover"]').popover()
    });
	//Back To Top
	$('#to-top').on('click',function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
	

})(jQuery);