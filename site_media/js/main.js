$().ready(function() {
    $('div.movie-buttons input[type="submit"]').click(function(e){
        return confirm("Are you sure you want to do this?");
    });
});
