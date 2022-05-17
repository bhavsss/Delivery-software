new WOW().init();

$('body').on('mouseenter mouseleave','.dropdown-hover',function(e){
    let dropdown=$(e.target).closest('.dropdown-hover');
    dropdown.addClass('show');

    setTimeout(function(){
        dropdown[dropdown.is(':hover')?'addClass':'removeClass']('show');
    },300);
});

/* inout plus js */
$("#input_plus").click(function() {
    increment();
});
$("#input_minus").click(function() {
    decrement();
});

function increment() {
    var inputNumber = parseInt($("#inputCalcBox").val());
    inputNumber++;
    $("#inputCalcBox").val(inputNumber);
}

function decrement() {
    var inputNumber = parseInt($("#inputCalcBox").val());
    inputNumber--;
    $("#inputCalcBox").val(inputNumber);
}
/**********input_plus************/
$("#input_plus").mousedown(function() {
    var inputNumber = parseInt($("#inputCalcBox").val());
    timeout = setInterval(function() {
        $("#inputCalcBox").val(inputNumber++);
    }, 150);
    return false;
});

$("#input_plus").mouseup(function() {
    clearInterval(timeout);
    return false;
});
/*********input_minus*************/
$("#input_minus").mousedown(function() {
    var inputNumber = parseInt($("#inputCalcBox").val());
    timeout = setInterval(function() {
        $("#inputCalcBox").val(inputNumber--);
    }, 150);
    return false;
});

$("#input_minus").mouseup(function() {
    clearInterval(timeout);
    return false;
});
/* inout plus js END */

$('.deliveryfrom-slider').owlCarousel({
    loop:true,
    margin:30,
    nav:false,
    dots: true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
});

$('.testimonial-slider').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
});


$('.testimonial-slider2').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
});


$('.category-slider').owlCarousel({
    loop: true,
    margin: 30,
    nav: false,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 4
        }
    }
});
$('.blog-slider').owlCarousel({
    loop: true,
    margin: 0,
    nav: false,
    dots: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});