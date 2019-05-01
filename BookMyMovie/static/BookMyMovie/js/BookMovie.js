$( document ).ready(function() {

    $(".seat-btn").on('click',function(e){
        // console.log(e.target.id);
        var target_id = e.target.id;
        $("#"+target_id).removeClass('btn-light');
        $("#"+target_id).addClass('btn-success');
 
    });
});