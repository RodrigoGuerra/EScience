$(function () {
    $("#submit").click(submitForm)
});


function submitForm() {
    alert("Upload with sucess")
    var formData = {};

    var file = $("#fileinput")[0].files[0];

    var fd = new FormData();
    fd.append('file', file);

    formData['Title'] = $("#titleinput").text();

    formData['Description'] = $("#textDescription").text();

    var tags = [];
    $("#tagList").find('p').each(function (index, element) {
        tags.push({Name: element.text()});
    });
    formData['Tags'] = tags;

    var authors = [];
    $("#authors_list").find('p').each(function (index, element) {
        authors.push({Name: element.text()});
    });
    formData['Authors'] = authors;


    $("#attribute_list").find('p').each(function (index, element) {
        formData.append('attribute' + index, element.text());
    });

    formData['View&Download'] = $("#FileViewers input:radio:checked").val();

    formData['Update'] = $("#FileUpdaters input:radio:checked").val();
    formData['License'] = $("#sel1");

    var uploadFile = function (data) {
        var id = data._id;
        console.log(JSON.stringify(data, null, 2));

        $.ajax({
            url: window.location.pathname + '/UploadFile/' + id,
            type: 'POST',
            data: fd,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data2) {
                console.log("OK!!!");
                console.log(JSON.stringify(data2, null, 2));
            },
            xhr: function () {  // Custom XMLHttpRequest
                var myXhr = $.ajaxSettings.xhr();
                if (myXhr.upload) { // Avalia se tem suporte a propriedade upload
                    myXhr.upload.addEventListener('progress', function () {
                        /* faz alguma coisa durante o progresso do upload */
                    }, false);
                }
                return myXhr;
            }
        });
    };

    $.ajax({
        url: window.location.pathname + '/InsertFile',
        type: 'post',
        dataType: 'json',
        success: uploadFile,
        data: JSON.stringify(formData)
    }).then(function (test) {
        console.log(test)
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