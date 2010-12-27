$(document).ready(function() 
    { 
        form = $("div.comments-form");
        link = $("p.show-comments-form");
        form.hide();
        link.show();
        link.click(function(e) {
            e.preventDefault();
            link.hide();
            $("div.comments").hide();
            form.show();
        });
            
        // $("#movie-table th").click(function() {
        //         $(this).removeClass("over");
        //     });
    } 
); 