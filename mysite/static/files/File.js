$(function () {
    $("#submit").click(submitForm)
});


function submitForm() {
    alert("Upload with sucess")
    var formData = {};
    /*
     files = $("#fileinput")[0].files;

     $.each(files, function (key, value) {
     formData.append('fileinput', value);
     });
     */
    formData['Title'] = $("#titleinput").text();

    formData['Description'] = $("#textDescription").text();

    var tags = []
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

    $.ajax({
        url: window.location.pathname + '/InsertFile',
        type: 'post',
        dataType: 'json',
        success: function (data) {
            console.log(JSON.stringify(data, null, 2));
        },
        data: JSON.stringify(formData)
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