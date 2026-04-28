$(document).ready(function() 
    { 
        form = $("div.comments-form");
        link = $("p.show-comments-form>a");
        form.hide();
        link.show();
        link.click(function(e) {
            e.preventDefault();
            link.hide();
            $("div.comments").hide();
            form.show();
        });
    } 
); 