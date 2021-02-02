$(document).on("click", '.icofont-trash', function(event){
    event.preventDefault();
    var bookmark_id = $(this).find("span").text().trim();
    $.ajax({
        type: "POST",
        url: "/insights/bookmark-delete-ajax",
        dataType: 'json',
        data:{
            'bookmark_id':bookmark_id,
        },
        headers:{
        "X-CSRFToken": '{{ csrf_token }}'
    }
    }).done(function(data) {
            $("#red-ajax").html(data.html_table);
            $("#bookmark-article").html(data.bookmark);

    });
});
