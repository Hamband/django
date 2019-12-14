$('#home-slideshow div').lightSlider({
    rtl: true,
    pager: false,
    item: 1,
    slideMargin: 0,
    loop: true,
    adaptiveHeight: true,
    controls: false,
    enableDrag: false,
    enableTouch: false,
    auto: true,
    pause: 6000,
    speed: 2000,
    mode: 'fade'
});

function initilazeMenu() {
    var lastActiveClass = 'events';
    $('.posts-blog-select .nav-link').on('click', function () {
        var currentClass = '.' + $(this).attr('data-hamband-to-show');
        if (!$(this).hasClass('active')) {
            $(lastActiveClass).removeClass('active');
            $(currentClass).addClass('active');
            lastActiveClass = currentClass;
        }
    });
}

initilazeMenu();