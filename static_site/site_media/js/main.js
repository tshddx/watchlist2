$().ready(function() {
    $("div.just-watched-form, div.add-to-wish-list-form, div.recommend-form").each(function() {
        var tr = $(this).siblings('a')[0];
        var close = $(this).find("a.close-window")[0];
        var myOpen = function(hash) {
            hash.o.hover(
                function() {
                    $("a.close-window").css("text-decoration", "underline");
                },
                function() {
                    $("a.close-window").css("text-decoration", "none");
                }
            );
            hash.w.show();
        }; 
        $(this).jqm({ trigger: tr, overlay: 65, onShow: myOpen });
        $(this).jqmAddClose(close);
        left = Math.floor($(tr).position()['left'] - 4);
        // There is always a variable out there in js called 'top', and js won't
        // complain or comply if you assign it to something else.
        topp = Math.floor($(tr).position()['top'] - 4);
        $(this).css('left', '' + left + "px");
        $(this).css('top', '' + topp + "px");
        $(this).css('position', "absolute");
    });
    $("div.datepicker").datepicker({
        showOtherMonths: true,
        selectOtherMonths: true,
        dateFormat: 'yy-mm-dd',
        altField: '.datepicker-alt'
    });
});