$( document ).ready(function() {

    
    $(".listing").hover(function() {
        $( this ).addClass( "listing-hover" );
        $( this ).children().children(".listing-name").addClass("listing-name-hove-color")
    }, function(){
        $( this ).removeClass( "listing-hover" );
        $( this ).children().children(".listing-name").removeClass("listing-name-hove-color")
    } );
});

