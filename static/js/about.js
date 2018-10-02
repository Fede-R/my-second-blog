//---------------------------------REVIEWSSSSS----------------------------------

// Show the new review form
$("#review-new-button").click(function() {
  $("#review-form").transition('slide down');
});


// Click a star
function clickStar(id) {
  for(i = 1; i <= id; i++) {
    $("#star-"+i).removeClass("empty star")
    $("#star-"+i).addClass("star")
  }
  for(i = id+1; i <= 5; i++) {
    $("#star-"+i).removeClass("star")
    $("#star-"+i).addClass("empty star")
  }
  $('#review-form').find('input[name="review-stars"]').val(id);
}


// REview Form Validation
$("#review-form").form({
    reviewName: {
      identifier: 'review-name',
      rules: [{
        type   : 'empty',
        prompt : 'Ingrese su nombre'
      }]
    },
    reviewComment: {
      identifier: 'review-comment',
      rules: [{
        type    : 'empty',
        prompt  : 'Deja un comentario'
      }]
    },
//    reviewStars: {
//      identifier: 'review-stars',
//      rules: [{
//        type    : 'empty',
//        prompt  : 'Please rate the dish'
//      }]
//    }
}, {
  onSuccess: function() {
    submitReview();
    // Reset Form
    $("#review-form").transition('slide down');
    clickStar(0);
    $("#review-form").form('reset');
    return false;
  },
  onFailure: function() {
    return false;
  }
});


// Submitting Review Form
function submitReview() {
  // preparing data
  var formData = {
    reviewer:         $('#review-form').find('input[name="review-name"]').val(),
    comment:          $('#review-comment').val(),
    stars:            $('#review-form').find('input[name="review-stars"]').val(),
//    enfermedadName:         currentData[currentEnfermedad].name,
//    enfermedadId:           currentData[currentEnfermedad].id,
  };

  // Ajax post
  $.ajax({ type: 'POST', url: '/api/mireviews', data: formData,
    success: function(data) {
      var text = $("#comments").text();
      var imageSize = 500;
      var margintop  =  Math.floor((Math.random() * (imageSize-50)) + 1);
      var marginleft =  Math.floor((Math.random() * (imageSize-50)) + 1);
      var currentTime = new Date();
      text =
      `<div class="comment">
        <div class="avatar" style="height:35px !important;overflow: hidden;">
          <img src="/static/images/avatar.png" style="width:`+imageSize+`px;height:`+imageSize+`px;
                                              margin-top:-`+margintop+`px;margin-left:-`+marginleft+`px">
        </div>
        <div class="content">
          <a class="author">`+formData.reviewer+`</a>
          <div class="metadata">
            <span class="date">`+currentTime.toDateString()+`</span>
          </div>
          <div class="text">
            `+formData.comment+`
          </div>
        </div>
      </div>` + $("#comments").html();
      $("#comments").html(text);
    },
    error: function() {
      saySomething(true, "Ops, something happened!")
  }});
}