$(function () {

    $(".skill-progress span").each(function () {

        $(this).animate({

            'width': $(this).data("width")

        }, 2000);

    });

})