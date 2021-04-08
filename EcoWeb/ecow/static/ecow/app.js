/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.body.style.backgroundColor = "white";
}

// Modal Image Gallery
function onClick(element) {
  document.getElementById("img01").src = element.src;
  document.getElementById("modal01").style.display = "block";
  var captionText = document.getElementById("caption");
  captionText.innerHTML = element.alt;
}

// PRODUCTS
$(document).ready(function(){
  
  // Lift card and show stats on Mouseover
  $('.product-card').hover(function(){
      $(this).addClass('animate');
      $('div.carouselNext, div.carouselPrev').addClass('visible');      
     }, function(){
      $(this).removeClass('animate');     
      $('div.carouselNext, div.carouselPrev').removeClass('visible');
  }); 
  
  // Flip card to the back side
  $('.view_details').click(function(){    
    $('div.carouselNext, div.carouselPrev').removeClass('visible');
    $('.product-card').addClass('flip-10');
    setTimeout(function(){
      $('.product-card').removeClass('flip-10').addClass('flip90').find('div.shadow').show().fadeTo( 80 , 1, function(){
        $('.product-front, .product-front div.shadow').hide();      
      });
    }, 50);
    
    setTimeout(function(){
      $('.product-card').removeClass('flip90').addClass('flip190');
      $('.product-back').show().find('div.shadow').show().fadeTo( 90 , 0);
      setTimeout(function(){        
        $('.product-card').removeClass('flip190').addClass('flip180').find('div.shadow').hide();            
        setTimeout(function(){
          $('.product-card').css('transition', '100ms ease-out');     
          $('.cx, .cy').addClass('s1');
          setTimeout(function(){$('.cx, .cy').addClass('s2');}, 100);
          setTimeout(function(){$('.cx, .cy').addClass('s3');}, 200);       
          $('div.carouselNext, div.carouselPrev').addClass('visible');        
        }, 100);
      }, 100);      
    }, 150);      
  });     
  
  // Flip card back to the front side
  $('.flip-back').click(function(){   
    
    $('.product-card').removeClass('flip180').addClass('flip190');
    setTimeout(function(){
      $('.product-card').removeClass('flip190').addClass('flip90');
  
      $('.product-back div.shadow').css('opacity', 0).fadeTo( 100 , 1, function(){
        $('.product-back, .product-back div.shadow').hide();
        $('.product-front, .product-front div.shadow').show();
      });
    }, 50);
    
    setTimeout(function(){
      $('.product-card').removeClass('flip90').addClass('flip-10');
      $('.product-front div.shadow').show().fadeTo( 100 , 0);
      setTimeout(function(){            
        $('.product-front div.shadow').hide();
        $('.product-card').removeClass('flip-10').css('transition', '100ms ease-out');    
        $('.cx, .cy').removeClass('s1 s2 s3');      
      }, 100);      
    }, 150);      
    
  }); 

  
  /* ----  Image Gallery Carousel ONE  ---- */
  
  var carousel_one = $('#carousel_one ul');
  var carouselSlideWidth_one = 335;
  var carouselWidth_one = 0;  
  var isAnimating_one = false;
  
  // building the width of the casousel
  $('#carousel_one li').each(function(){
    carouselWidth_one += carouselSlideWidth_one;
  });
  $(carousel_one).css('width', carouselWidth_one);
  
  // Load Next Image
  $('div#carouselNext_one').on('click', function(){
    var currentLeft_one = Math.abs(parseInt($(carousel_one).css("left")));
    var newLeft_one = currentLeft_one + carouselSlideWidth_one;
    if(newLeft_one == carouselWidth_one || isAnimating_one === true){return;}
    $('#carousel_one ul').css({'left': "-" + newLeft_one + "px",
                 "transition": "300ms ease-out"
               });
    isAnimating_one = true;
    setTimeout(function(){isAnimating_one = false;}, 300);      
  });
  
  // Load Previous Image
  $('div#carouselPrev_one').on('click', function(){
    var currentLeft_one = Math.abs(parseInt($(carousel_one).css("left")));
    var newLeft_one = currentLeft_one - carouselSlideWidth_one;
    if(newLeft_one < 0  || isAnimating_one === true){return;}
    $('.carousel ul').css({'left': "-" + newLeft_one + "px",
                 "transition": "300ms ease-out"
               });
      isAnimating_one = true;
    setTimeout(function(){isAnimating_one = false;}, 300);      
  });
});

/* ----  Image Gallery Carousel TWO  ---- */
  
var carousel_two = $('#carousel_two ul');
var carouselSlideWidth_two = 335;
var carouselWidth_two = 0;  
var isAnimating_two = false;

// building the width of the casousel
$('#carousel_two li').each(function(){
  carouselWidth_two += carouselSlideWidth_two;
});
$(carousel_two).css('width', carouselWidth_two);

// Load Next Image
$('div#carouselNext_two').on('click', function(){
  var currentLeft_two = Math.abs(parseInt($(carousel_two).css("left")));
  var newLeft_two = currentLeft_two + carouselSlideWidth_two;
  if(newLeft_two == carouselWidth_two || isAnimating_two === true){return;}
  $('#carousel_two ul').css({'left': "-" + newLeft_two + "px",
               "transition": "300ms ease-out"
             });
  isAnimating_two = true;
  setTimeout(function(){isAnimating_two = false;}, 300);      
});

// Load Previous Image
$('div#carouselPrev_two').on('click', function(){
  var currentLeft_two = Math.abs(parseInt($(carousel_two).css("left")));
  var newLeft_two = currentLeft_two - carouselSlideWidth_two;
  if(newLeft_two < 0  || isAnimating_two === true){return;}
  $('#carousel_two ul').css({'left': "-" + newLeft_two + "px",
               "transition": "300ms ease-out"
             });
    isAnimating_two = true;
  setTimeout(function(){isAnimating_two = false;}, 300);      
});

/* ----  Image Gallery Carousel THREE  ---- */
  
var carousel_three = $('#carousel_three ul');
var carouselSlideWidth_three = 335;
var carouselWidth_three = 0;  
var isAnimating_three = false;

// building the width of the casousel
$('#carousel_three li').each(function(){
  carouselWidth_three += carouselSlideWidth_three;
});
$(carousel_three).css('width', carouselWidth_three);