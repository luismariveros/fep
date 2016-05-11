jQuery(document).ready(function() {
  

   $('#papaC').carousel();
  
	//this code is for the gmap
	 var map = new GMaps({
        el: '#map',
        lat: -12.043333,
        lng: -77.028333
      });


      

          function onScroll(event){
              var scrollPos = $(document).scrollTop();
              $('.navbar-default .navbar-nav>li>a').each(function () {
                  var currLink = $(this);
                  var refElement = $(currLink.attr("href"));
                  if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
                      $('.navbar-default .navbar-nav>li>a').removeClass("active");
                      currLink.addClass("active");
                  }
                  else{
                      currLink.removeClass("active");
                  }
              });
          }
     
     
     //this code is for animation nav
     jQuery(window).scroll(function() {
        var windowScrollPosTop = jQuery(window).scrollTop();

        if(windowScrollPosTop >= 150) {
          jQuery(".header").css({"background": "#B193DD",});
          jQuery(".top-header img.logo").css({"margin-top": "-40px", "margin-bottom": "0"});
          jQuery(".navbar-default").css({"margin-top": "12px",});
        }
        else{
          jQuery(".header").css({"background": "transparent",});
           jQuery(".top-header img.logo").css({"margin-top": "-12px", "margin-bottom": "25px"});
           jQuery(".navbar-default").css({"margin-top": "12px", "margin-bottom": "0"});
          
        }
     });

      
     

});