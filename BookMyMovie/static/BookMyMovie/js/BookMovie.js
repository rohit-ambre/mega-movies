$( document ).ready(function() {

    $(".seat-btn").on('click',function(e){
        var target_id = e.target.id;

        if($(this).hasClass("active")){

            if($(this).hasClass("btn-success")){
                $(this).addClass('btn-light');
                $(this).removeClass('btn-success');
            }
        }else{
            $(this).removeClass('btn-light');
            $(this).addClass('btn-success');
        }
 
    });
});