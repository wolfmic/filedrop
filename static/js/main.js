function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

// AJAX for posting
function create_post() {
    var data = new FormData($('form').get(0));
    console.log(`data: ${data}`)
    $.ajax({
        url : "upload/", // the endpoint
        type : "POST", // http method
        data: data,
        async: false,
        cache: false,
        contentType: false,
        processData: false,
        success : function(json) {
            //console.log(data);
            $('#id_file').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// Submit post on submit
$('#post-form').on('submit', function(event){
    event.preventDefault();
    create_post(event);
});
