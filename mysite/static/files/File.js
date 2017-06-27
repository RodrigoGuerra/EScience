$(function() {
    $("#submit").click(submitForm)  
});


function submitForm(){
    alert("Upload with sucess")
    var formData = new FormData(this);
    
    files = $("#fileinput")[0].files;
    
    $.each(files, function(key, value)
    {
        formData.append('fileinput', value);
    });
    
    
    formData.append('Title',$("#titleinput").text());
    
    formData.append('Description',$("#textDescription").text());
    
    $("#tagList").find('p').each(function (index, element){
        formData.append('tag'+index,element.text());                              
    });
    
    $("#authors_list").find('p').each(function (index, element){
        formData.append('author'+index,element.text());                              
    });
    
    $("#attribute_list").find('p').each(function (index, element){
        formData.append('attribute'+index,element.text());                            
    });
    
    formData.append('view&download',$("#FileViewers input:radio:checked").val());
    
    formData.append('Update',$("#FileUpdaters input:radio:checked").val());
    
    formData.append('license',$("#sel1"));
    
    $.ajax({
       url: window.location.pathname+'/InsertFile',
       type: 'POST',
        data: formData,
        success: function (data) {
            alert(data)
        },
        
        xcsrftoken: getCookie('xcsrftoken'),
        cache: false,
        contentType: false,
        processData: false,
        xhr: function() {  // Custom XMLHttpRequest
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) { // Avalia se tem suporte a propriedade upload
                myXhr.upload.addEventListener('progress', function () {
                    /* faz alguma coisa durante o progresso do upload */
                }, false);
            }
        return myXhr;
        }
    });
        
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}