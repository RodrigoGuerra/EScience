$(function() {
   
   $("#addTag").click(addTag);
   
});


function addTag(){
    tag = $("#tagText").val();
    $('#tagList').append('<p>'+tag+'<span onclick="deleteTag(\''+tag+'\')" class="glyphicon glyphicon-remove" aria-hidden="true"></span>'+'</p>');
    $("#tagText").val('');
}

function deleteTag(tag){
    $('#tagList > p').each(function(){
        if($(this).text()==tag){
            $(this).remove();
        }
    })
}