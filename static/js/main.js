//ISOTOPE
$(document).ready(function(){
    var $container = $('.portfolioContainer');//THIS IS THE NAME OF THE CLASS FOR THE CONTAINER THAT WILL HOLD THE PORTFOLIO IMAGES
    $container.isotope({
        filter: '*',
        animationOptions: {
            duration: 750,      //TIMING IN MS
            easing: 'linear',   //EASING
            queue: false
        }
    });
 
    $('.portfolio_filter li').click(function(){
        $('.portfolio_filter .current').removeClass('current');
        $(this).addClass('current');
 
        var selector = $(this).attr('data-filter');
        $container.isotope({
            filter: selector,
            animationOptions: {
                duration: 750,     //TIMING IN MS
                easing: 'linear',  //EASING
                queue: false
            }
         });
         return false;
    }); 
});


  

/**
 * Initiate PureCounter 
 */
new PureCounter();

