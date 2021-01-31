$(".q1").click(function(){
      $("#question-one").css("display", "none");
      $("#question-two").css("display", "block");
      $("#reset-btn").css("display", "block");
      $("#q2image").css("float", "right");
      var question1 = $(this).text().trim();
      localStorage.setItem('q1ans', question1);
});
$("#reset-btn").click(function(){

  $("#question-two").css("display", "none");
  $("#why-us").css("display", "none");
  $("#question2image").css("float", "right");
  $("#question-one").css("display", "block");
  $("#reset-btn").css("display", "none");

})
$(".q2").click(function(e) {
    e.preventDefault();
    var answerone = localStorage.getItem('q1ans')
    var questiontwo = $(this).text().trim();
    $.ajax({
        type: "POST",
        url: "/insights/question-answer",
        dataType: 'json',
        data:{
            'answerone':answerone,
            'answertwo':questiontwo,
        },
        headers:{
        "X-CSRFToken": '{{ csrf_token }}'
    }
    }).done(function(data) {
            $("#question-two").css("display", "none");
            $("#why-us").css("display", "block");
             $('#questionres').html(data.html_table);

    });
});

