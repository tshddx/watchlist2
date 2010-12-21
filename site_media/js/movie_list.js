$(document).ready(function() 
    { 
        $("#movie-table").tablesorter();
        $("#movie-table th").append(' <span class="sort-arrows">&#x21C5;</span>');
        $("#movie-table th").css('cursor', 'pointer');
        $("#movie-table th").mouseover(function() {
                $(this).addClass("over");
            });
        $("#movie-table th").mouseout(function() {
                $(this).removeClass("over");
            });
        $("#movie-table th").click(function() {
                $(this).removeClass("over");
            });
    } 
); 