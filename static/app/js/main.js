(function ($) {
 "use strict";

/*----------------------------
 jQuery MeanMenu
------------------------------ */
	jQuery('nav#dropdown').meanmenu();	
	
/*----------------------------
 wow js active
------------------------------ */
	
 
/* ----------------------------
 Tooltip
------------------------------ */
    $('[data-toggle="tooltip"]').tooltip({
        animated: 'fade',
        container: 'body'
    });
/*----------------------------
 Active-Product
------------------------------ */  
	$('#active-product').owlCarousel({
		loop:true,
		margin:3,
		nav:true,
		navText:["<i class='sp-arrow-bold-left'></i>","<i class='sp-arrow-bold-right'></i>"],
		responsive:{
			320: {items: 1 },
			480: {items: 2 },
			768: {items: 3 },
			992: {items: 4 },
			1200:{items: 5 }
		}
	})

/*----------------------------
 Active-Testimonial
------------------------------ */  
	$('.active-testimonial').owlCarousel({
		loop:true,
		margin:3,
		//transitionStyle : "backSlide", /* [This code for animation ] */	
		nav:true,
		navText:["<i class='sp-angle-left'></i>","<i class='sp-angle-right'></i>"],
		responsive:{
			320: {items: 1 },
			480: {items: 1 },
			768: {items: 1 },
			992: {items: 1 },
			1200:{items: 1 }
		}
	})
	
/*----------------------------
 Active-Best-Sell
------------------------------ */  
	$('.active-best-sell').owlCarousel({
		loop:true,
		margin:3,
		nav:true,
		navText:["<i class='sp-arrow-bold-left'></i>","<i class='sp-arrow-bold-right'></i>"],
		responsive:{
			320: {items: 1 },
			480: {items: 2 },
			768: {items: 3 },
			992: {items: 3 },
			1200:{items: 4 }
		}
	})	
/*----------------------------
 Active-Best-Sell-2
------------------------------ */  
	$('.active-best-sell-2').owlCarousel({
		loop:true,
		//margin:3,
		nav:true,
		navText:["<i class='sp-arrow-bold-left'></i>","<i class='sp-arrow-bold-right'></i>"],
		responsive:{
			320: {items: 1 },
			480: {items: 2 },
			768: {items: 2 },
			992: {items: 3 },
			1200:{items: 4 }
		}
	})
	
/*----------------------------
 Active-Related-Product
------------------------------ */  
	$('.active-related-product').owlCarousel({
		loop:true,
		margin:10,
		nav:true,
		navText:false,
		responsive:{
			320: {items: 1 },
			480: {items: 2 },
			768: {items: 3 },
			992: {items: 4 },
			1200:{items: 5 }
		}
	})
	
	
/*----------------------------
 Active-new-collection-2
------------------------------ */  
	$('.active-new-collection-2').owlCarousel({
		loop:true,
		margin:10,
		nav:true,
		navText:false,
		responsive:{
			320 : { items: 1 },
			480 : { items: 2 },
			768 : { items: 3 },
			992 : { items: 4 },
			1200: { items: 5 }
		}
	})
	
/*--------------------------
 Shop Grid view and List view
---------------------------- */
$('.view-mode a').click(function(){
	var v_mode = $(this).attr('class');
	$( ".view-mode a" ).removeClass( "active" );
	$(".view-mode a."+v_mode).addClass( "active" );
});

/*----------------------------
 price-slider active
------------------------------ */  
	 $( "#slider-range" ).slider({
	 range: true,
	 min: 15,
	 max: 721,
	 values: [ 15, 550 ],
	 slide: function( event, ui ) {
	  $( "#amount" ).val( "$" + ui.values[ 0 ] + " - "+ "$" + ui.values[ 1 ] );
	  $('input[name="first_price"]').val('$' + ui.values[0]);
	  $('input[name="last_price"]').val('$' + ui.values[1]);
	 },
	});
	$( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
	 " - "+"$" + $( "#slider-range" ).slider( "values", 1 ) );
	$('input[name="first_price"]').val('$' + $( "#slider-range" ).slider( "values", 0 ));
	$('input[name="last_price"]').val('$' + $( "#slider-range" ).slider( "values", 1 )); 
	
/*---------------------
 Lightbox
--------------------- */	   
$(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

/*----- cart-plus-minus-button -----*/	
	 $(".cart-plus-minus").append('<div class="inc qtybutton">+</div><div class="dec qtybutton">-</div>');
	  $(".qtybutton").on("click", function() {
		var $button = $(this);
		var oldValue = $button.parent().find("input").val();
		if ($button.text() == "+") {
		  var newVal = parseFloat(oldValue) + 1;
		} else {
		   // Don't allow decrementing below zero
		  if (oldValue > 0) {
			var newVal = parseFloat(oldValue) - 1;
			} else {
			newVal = 0;
		  }
		  }
		$button.parent().find("input").val(newVal);
	  }); 	
	  
	  
	
/*-------------------------
  showlogin toggle function
--------------------------*/
	 $( '#showlogin' ).on('click', function() {
        $( '#checkout-login' ).slideToggle(900);
     }); 
		
/*-------------------------
  showcoupon toggle function
--------------------------*/
	 $( '#showcoupon' ).on('click', function() {
        $( '#checkout_coupon' ).slideToggle(900);
     });


                /*-------------------------
                  accordion toggle function
                --------------------------*/
                $('.payment-accordion').find('.payment-accordion-toggle').on('click', function(){
                  //Expand or collapse this panel
                  $(this).next().slideToggle(500);
                  //Hide the other panels
                  $(".payment-content").not($(this).next()).slideUp(500);

                });
                /* -------------------------------------------------------
                 accordion active class for style
                ----------------------------------------------------------*/
                $('.payment-accordion-toggle').on('click', function(event) {
                    $(this).siblings('.active').removeClass('active');
                    $(this).addClass('active');
                    event.preventDefault();
                }); 
/*---------------------
 countdown
--------------------- */
	$('[data-countdown]').each(function() {
		var $this = $(this), finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function(event) {
			$this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hour</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>Min</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>Sec</p></span>'));
		});
	});	

/*----------------------------
 price-slider active
------------------------------ */  
	// $( "#slider-range" ).slider({
		// range: true,
		// min: 40,
		// max: 600,
		// values: [ 60, 570 ],
		// slide: function( event, ui ) {
			// $( "#amount" ).val( "£" + ui.values[ 0 ] + " - £" + ui.values[ 1 ] );
		// }
	// });
	// $( "#amount" ).val( "£" + $( "#slider-range" ).slider( "values", 0 ) +
	// " - £" + $( "#slider-range" ).slider( "values", 1 ) );  
	   
/*--------------------------
 scrollUp
---------------------------- */	
	$.scrollUp({
        scrollText: '<i class="pe-7s-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });

	
	$(".active-best-sell-2 .owl-controls").addClass("container");
	
 
})(jQuery); 