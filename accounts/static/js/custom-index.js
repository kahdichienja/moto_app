(function($) {
	"use strict";

    //Preloader
    $(window).load(function() {
        $('.images-preloader').fadeOut();
    });

	//Header Scroll
	
	function init() {
        window.addEventListener('scroll', function(e){
			
			var mq = window.matchMedia( "(min-width: 992px)" );
			
			if (mq.matches) {
				var distanceY = window.pageYOffset || document.documentElement.scrollTop,
                shrinkOn = 10,
                header = document.querySelector(".main-bar");
            if (distanceY > shrinkOn) {
                classie.add(header,"smaller");
            } else {
                if (classie.has(header,"smaller")) {
                    classie.remove(header,"smaller");
                }

            }
			}

            
        });
    }
    window.onload = init();

    // Elements Animation Important
    if($('.wow').length){
        var wow = new WOW(
          {
            boxClass:     'wow',      // animated element css class (default is wow)
            animateClass: 'animated', // animation css class (default is animated)
            offset:       0,          // distance to the element when triggering the animation (default is 0)
            mobile:       true,       // trigger animations on mobile devices (default is true)
            live:         true       // act on asynchronously loaded content (default is true)
          }
        );
        wow.init();
    }
    
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

    //Position Navigation

    $(window).on('resize', function () {
        var hbar = $('.site-header').outerHeight(),
            sbar = $('header .sub-bar').height();
        $('.main-bar .nav').css('top', hbar);
        $("header .main-bar").css('top', sbar);
    }).trigger('resize');
    
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

	//All Sliders

	var $portfolio = $( "#recent-slider" );
	$portfolio.owlCarousel({
        navigation: false, 
        navigationText: ["<i class='fa fa-caret-left'></i>","<i class='fa fa-caret-right'></i>"],
        slideSpeed : 600,
        autoPlay : 8000,
        items : 3,
		itemsDesktop      : [1199,3],
		itemsDesktopSmall     : [979,3],
		itemsTablet       : [768,2],
		itemsMobile       : [479,1],
        pagination: false
    });

    $('.next-slide').on('click',function(e){
    	e.preventDefault();
      	$portfolio.trigger( 'owl.next' );
    });
    $('.back-slide').on('click',function(e){
    	e.preventDefault();
      	$portfolio.trigger( 'owl.prev' );
    });

    $("#testimonials").owlCarousel({
        navigation: false, 
        slideSpeed : 600,
        autoPlay : 6000,
        singleItem:true,
        pagination: true,
        navigationText: [
	      "<i class='fa fa-caret-left'></i>",
	      "<i class='fa fa-caret-right'></i>"
	    ],
    });
    $("#hotel").owlCarousel({
        navigation: false, 
        slideSpeed : 600,
        autoPlay : 6000,
        singleItem:true,
        pagination: true,
        navigationText: [
          "<i class='fa fa-caret-left'></i>",
          "<i class='fa fa-caret-right'></i>"
        ],
    });
    //Fun Fact

    jQuery(document).ready(function($){
        $('.counter-skills').counterUp({
            delay: 100,
            time: 2000
        });
    });

     // Owl Client
        $("#clients").owlCarousel({
        navigation: false, 
        navigationText: ["<i class='fa fa-caret-left'></i>","<i class='fa fa-caret-right'></i>"],
        slideSpeed : 600,
        autoPlay : 2000,
        items : 5,
        itemsDesktop      : [1199,5],
        itemsDesktopSmall     : [979,4],
        itemsTablet       : [768,3],
        itemsMobile       : [479,2],
        pagination: false
    });

    //Isotop Projects

    $(window).load(function() {
        // --------------------------------------------------
        // filtering gallery
        // --------------------------------------------------
        var $container = $('#gallery');
        $container.isotope({
            itemSelector: '.item',
            filter: '*'
        });

        $('#filter a').on('click',function() {
            var $this = $(this);
            if ( $this.hasClass('current') ) {
                return false;
                }
            var $optionSet = $this.parents();
            $optionSet.find('.current').removeClass('current');
            $this.addClass('current');
                    
            var selector = $(this).attr('data-filter');
            $container.isotope({ 
                filter: selector,
            });
            return false;
        });

    });
    
    //Revo Slider

    $('#revolution-slider').revolution({
        delay: 9000,
        startwidth: 1100,
        startheight: 600,
        hideThumbs: 10,
        fullWidth: "off",
        fullScreen: "off",
        fullScreenOffsetContainer: "",
        touchenabled: "on",
        navigationType: "none",
        onHoverStop: "off",
    });

	//Colorbox Project

	$(".zoomin").colorbox({rel:'item-image', maxWidth:'80%', maxHeight:'80%', transition: 'elastic'});

	//Back To Top
	$('#to-top').on('click',function() {
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
	

})(jQuery);