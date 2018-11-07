// --------------------------------Variables + Constants---------------------------------------------
// current dishes results
var currentData;
var currentEnfermedad;
var currentTab;
var values = {'sintomaBB': ['naranja', 'castano', 'oscuro', 'amarillo', 'ninguno'],
              'sintomaAA': ['sintomaAAA', '<del>sintomaAAA</del>'],
              'sintomaCC': ['irregular', 'oval', 'puntos', 'ninguno']//,
//              'sourLevel': ['no sour', 'a bit sour', 'sour', 'super sour'],
//              'sintomaEE': ['en nervadura', 'en cogollo', 'dispersa']
//              'fatLevel': ['low fat', 'normal fat', 'high fat'],
//              'calorieLevel': ['low calorie', 'normal calorie', 'high calorie']//,
//              'fiberLevel': ['low fiber', 'normal fiber', 'high fiber'],
//              'carbLevel': ['low carb', 'normal carb', 'high carb']
            };
var changableData = ['sintomaAA', 'sintomaBB', 'sintomaCC'];
var cardColors = ["grey", "black", "yellow", "olive", "green", "teal", "blue", "violet", "purple", "pink", "brown", "red", "orange"];
var numColors = cardColors.length;



// Preference button clicked
$("#preference-button").on("click", function() {
  $('#outer-box').transition('scale');
})


// Show preference box & preference button
$( document ).ready(function() {
  $("#preference-link").hide();
  $("#preference-button").show();
  $('#outer-box').transition('scale');
  setTimeout(function(){ saySomething(true, "Bienvenido"); }, 500);
});


// Uncheckable Radio buttons
$('.ui.radio').checkbox({
  uncheckable: true
});


// Image slider
$('#left-arr').click(function() {
  currentTab = (currentTab + 1) % currentData[currentEnfermedad].images;
  resetTab(currentTab);
});
$('#right-arr').click(function() {
  console.log("testing")
  currentTab = (currentTab + currentData[currentEnfermedad].images - 1) % currentData[currentEnfermedad].images;
  resetTab(currentTab);
});
function resetTab(index) {
  for (i = 0; i < currentData[currentEnfermedad].images; i++) {
    $('#tab'+i).removeClass('active')
  }
  $('#tab'+index).addClass('active')
}


//----------------------------------- PREFERENCE FORM HANDLER-------------------------------------------

// Preference Form Validation
$("#form-preference").form({
  planta: {
  identifier: 'planta',
  rules: [{
    type    : 'empty',
    prompt  : 'Please choose the planta'
  }]
}}, {
  onSuccess: function() {
    submitForm();
    return false;
  },
  onFailure: function() {
    saySomething(true, "Opss, there are some errors :(")
    return false;
  }
});


// Submiting Preference Form
function submitForm() {
  // set form to loading
  $('#form-preference').addClass("loading");

  // preparing data
  var formData = {
    planta:      $('#form-preference').find('select[name="planta"]').val(),
//    sintomaDD:   filter($('#form-preference').find('input[name="sintoma-dd"]:checked').val()),
    sintomaCC:   filter($('#form-preference').find('input[name="sintoma-cc"]:checked').val()),
//    sourLevel:    filter($('#form-preference').find('input[name="sour-level"]:checked').val()),
//    sintomaEE:   filter($('#form-preference').find('input[name="sintoma-ee"]:checked').val()),
//    fatLevel:     filter($('#form-preference').find('input[name="fat-level"]:checked').val()),
//    calorieLevel: filter($('#form-preference').find('input[name="calorie-level"]:checked').val()),
//    fiberLevel:   filter($('#form-preference').find('input[name="fiber-level"]:checked').val()),
//    carbLevel:    filter($('#form-preference').find('input[name="carb-level"]:checked').val()),
    sintomaBB:      filter($('#form-preference').find('input[name="sintoma-bb"]:checked').val()),
    sintomaAA: filter($('#form-preference').find('input[name="sintoma-aa"]:checked').val()),
  };

  // Ajax post
  $.ajax({ type: 'POST', url: '/api/preferencestriho', data: formData,
    success: function(data) {
      $('#form-preference').removeClass("loading");
      if (data.length == 0) {
        saySomething(true, 'Disculpe, no hay resultados');
      } else {
        $('#outer-box').transition('scale');
        renderCards(data);
      }
    },
    error: function() {
      saySomething(true, "Ocurrió un error, disculpe")
  }});
}


// ------------------------- CARDS --------------------------------------------
//Rendering cards
function renderCards(data) {
  currentData = data;
  var content = "";
  var index = 0;

  for (i = 0; i < data.length; i++) {
    content += `
      <div id="card-`+i+`" class="enfermedad-card ui `+cardColors[index]+` card" style="display:none" onclick="clickCard(`+i+`)">
        <div class="image">
          <img src="/static/images/dishestriho/`+data[i].id+`_1_square.jpeg">
        </div>
        <div class="content">
          <div class="header left floated">`+data[i].name+`</div>
          <div class="right floated">
            <i class="star icon card-star"></i>`+Math.round(data[i].stars * 100) / 100+`
          </div>
        </div>
      </div>`;
    index = (index + 1) % numColors;
  }
  $("#enfermedad-cards").html(content);
  // show cards
  $('.enfermedad-card').transition({
    animation : 'horizontal flip',
    interval  : 5000
  })
  saySomething(false, "Diagnóstico generado")
}


// Card Clicked - Show detail
function clickCard(id) {
  currentEnfermedad = id;

  // Name
  $("#detail-name").text(currentData[id].name);

  // Description
  $("#detail-description").text(currentData[id].description);

  // Tags
  var index = 0;
  var tags = "";
  tags += `<a class="agro-tag ui `+cardColors[index]+` basic label">`+currentData[id].planta+`</a>`;
  index = (index + 1) % numColors;

  var text = (currentData[id].sintomaAAA == 'TRUE') ? "sintomaAAA" : "<del>sintomaAAA</del>"
  tags += `<a class="agro-tag ui `+cardColors[index]+` basic label" onclick="showSuggestions(this,'`+cardColors[index]+`','`+changableData[0]+`')">`+text+`</a>`;
  index = (index + 1) % numColors;

  for (i = 1; i < changableData.length; i++) {
    tags += `<a class="agro-tag ui `+cardColors[index]+` basic label" onclick="showSuggestions(this,'`+cardColors[index]+`','`+changableData[i]+`')">`+currentData[id][changableData[i]]+`</a>`;
    index = (index + 1) % numColors;
  }
  $("#detail-tags").html(tags);

  // Stars
  $("#detail-rating").text("Rating: "+Math.round(currentData[id].stars * 100) / 100);
  for (i = 1; i <= 5; i ++) {
    if (currentData[id].stars < i-1 + 0.25) {
      $("#header-star-"+i).removeClass("star")
      $("#header-star-"+i).removeClass("empty star")
      $("#header-star-"+i).removeClass("star half empty")
      $("#header-star-"+i).addClass("empty star")
    } else if (currentData[id].stars > i-1 + 0.75) {
      $("#header-star-"+i).removeClass("star")
      $("#header-star-"+i).removeClass("empty star")
      $("#header-star-"+i).removeClass("star half empty")
      $("#header-star-"+i).addClass("star")
    } else {
      $("#header-star-"+i).removeClass("star")
      $("#header-star-"+i).removeClass("empty star")
      $("#header-star-"+i).removeClass("star half empty")
      $("#header-star-"+i).addClass("star half empty")
    }
  }

  // Images
  var imagesText = "";
  for (i = 1; i <= currentData[id].images; i++) {
    if (i == 1) {
      imagesText += `
      <div id="tab`+(i-1)+`" class="ui bottom attached tab active" data-tab="`+(i-1)+`">
        <img src="/static/images/dishestriho/`+currentData[id].id+`_`+i+`_square.jpeg" style="width:100%"/>
      </div>`;
    } else {
      imagesText += `
      <div id="tab`+(i-1)+`" class="ui bottom attached tab" data-tab="`+(i-1)+`">
        <img src="/static/images/dishestriho/`+currentData[id].id+`_`+i+`_square.jpeg" style="width:100%"/>
      </div>`;
    }
  }
  $("#modal-image-tabs").html(imagesText);
  currentTab = 0;
  if (currentData[id].images == 1) {
    $('#left-arr').hide();
    $('#right-arr').hide();
  } else {
    $('#left-arr').show();
    $('#right-arr').show();
  }

  // Comments
  $("#comments").html("");
  $("#comments").addClass("loading");
  $.ajax({ type: 'GET', url: '/api/reviewstriho', data: {"enfermedadId": currentData[id].id},
    success: function(data) {
      $("#comments").removeClass("loading");
      showComments(data);
    },
    error: function() {
      saySomething(true, "Ocurrió un error, disculpe")
  }});
  // Show
  $("#modal-card-detail").modal('show');
}

// Show comments
function showComments(data) {
  var text = "";
  for (i = 0; i < data.length; i++) {
    var imageSize = 500;
    var margintop  =  Math.floor((Math.random() * (imageSize-50)) + 1);
    var marginleft =  Math.floor((Math.random() * (imageSize-50)) + 1);;
    text +=
    `<div class="comment">
      <div class="avatar" style="height:35px !important;overflow: hidden;">
        <img src="/static/images/avatar.png" style="width:`+imageSize+`px;height:`+imageSize+`px;
                                            margin-top:-`+margintop+`px;margin-left:-`+marginleft+`px">
      </div>
      <div class="content">
        <a class="author">`+data[i].reviewer+`</a>
        <div class="metadata">
          <span class="date">`+(new Date(data[i].createdTime)).toDateString()+`</span>
        </div>
        <div class="text">
          `+data[i].comment+`
        </div>
      </div>
    </div>`;
  }
  $("#comments").html(text);
}


//---------------------------------REVIEWSSSSS----------------------------------

// Show the new review form
$("#review-new-button").click(function() {
  $("#review-form").transition('scale');
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
//    reviewName: {
//      identifier: 'review-name',
//      rules: [{
//        type   : 'empty',
//        prompt : 'Please enter name'
//      }]
//    },
//    reviewComment: {
//      identifier: 'review-comment',
//      rules: [{
//        type    : 'empty',
//        prompt  : 'Please give some comment'
//      }]
//    },
    reviewStars: {
      identifier: 'review-stars',
      rules: [{
        type    : 'empty',
        prompt  : 'Por favor, califica el diagnóstico'
      }]
    }
}, {
  onSuccess: function() {
    submitReview();
    // Reset Form
    $("#review-form").transition('scale');
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
    enfermedadName:         currentData[currentEnfermedad].name,
    enfermedadId:           currentData[currentEnfermedad].id,
  };

  // Ajax post
  $.ajax({ type: 'POST', url: '/api/reviewstriho', data: formData,
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


// ------------------------------------Suggestions------------------------------
// User's Suggestions
var countdown;
function showSuggestions(e, color, key) {
  var content = `
  <div id="suggestion">`
  for (i = 0; i < values[key].length; i++)
    content += `<button class="mini ui `+color+` basic button"
                onclick="newSuggestion('`+key+`','`+values[key][i]+`')">`+values[key][i]+`</button>`;
  content += `</div>`;
  $('#suggestion-box').html(content);

  var box = $('#suggestion')
  box.css({top: $(e).position().top + 36, left: $(e).position().left});
  box.transition('swing down');

  countdown = setTimeout(function() {
    if (box.is(':visible')) {box.transition('fade');}
  }, 1500);
  box.mouseenter(function() {
    clearTimeout(countdown);
    countdown = undefined;
  });
  box.mouseleave(function() {
    if (countdown == undefined) {
      countdown = setTimeout(function() {
        if (box.is(':visible')) {box.transition('fade');}
    }, 1500);
    }
  });
}

function newSuggestion(key, value) {
  if (key == 'sintomaAA') {
    value = (value == 'sintomaAAA') ? 'TRUE' : 'FALSE';
  }

  clearTimeout(countdown);
  $('#suggestion').transition('vertical flip');

  $("#modal-message").transition({
    animation: 'vertical flip',
    onComplete: function() {
      thanksCountDown = setTimeout(function() {
        $("#modal-message").transition('vertical flip');
      }, 500);
    }
  });

  // Send to server
  // Ajax post
  $.ajax({ type: 'POST', url: '/api/modifications', data: {
      key: key,
      value: value,
      enfermedadName:         currentData[currentEnfermedad].name,
      enfermedadId:           currentData[currentEnfermedad].id,
    },
    success: function(data) {
    },
    error: function() {
    }});
}


// Utilities
function filter(text) {
  return (text == undefined) ? "?" : text;
}



// ------------------------ SCRET FLAVOR --------------------------------------
var fakeData = [{"comment": "Best dish ever", "stars": "5"},
                {"comment": "Not a bad choice", "stars": "4"},
                {"comment": "I really like this dish", "stars": "4"},
                {"comment": "I love this dish", "stars": "5"},
                {"comment": "The taste is ok but I do not like the smell", "stars": "3"},
                {"comment": "Smelly ..", "stars": "2"},
                {"comment": "Very freshy", "stars": "5"},
                {"comment": "Best dish for hungry ones :))", "stars": "5"},
                {"comment": "I cannot finish the dish", "stars": "1"},
                {"comment": "Nice taste", "stars": "4"},
                {"comment": "Smell good!", "stars": "4"},
                {"comment": "So so", "stars": "3"},
                {"comment": "Good tast good smell", "stars": "5"},
                {"comment": "Fulling my stomach well", "stars": "4"},
                {"comment": "I will definately try this dish again", "stars": "5"},
                {"comment": "Nice dish", "stars": "4"},
                {"comment": "I love the taste", "stars": "5"},
                {"comment": "I want to learn how to make this dish", "stars": "5"},
                {"comment": "Good! May try again", "stars": "4"},
                {"comment": "Thumb up!", "stars": "5"},
                {"comment": "Thumb down!", "stars": "1"}
              ];
var fakeNames = ["Jack", "Jill", "Jarvis", "Tony", "Trung", "Trang", "Mint", "Cindy", "Thanh",
                 "Stark", "Captain America", "Captain Singapore", "Hulk", "Thor", "Doraemon",
                 "Nobita", "Shizuka", "Jaian", "Mr.Pusheen", "Koko", "Jonathan", "Gennady", "Nathan",
                 "Grey", "Maria", "Songoku", "Naruto", "Luffy", "Zoro", "Nami", "Robin", "Chopper", "Franky",
                 "Ussop", "Yasoop", "Gol .D Roger"]

// Create random review
function createRandomReview(num) {
  var x = 1;

  var intervalId = setInterval(function() {
    if (++ x >= num) {
       window.clearInterval(intervalId);
    }
    console.log(x);
    // preparing data
    enfermedadId = Math.floor((Math.random() * currentData.length));
    name = fakeNames[Math.floor((Math.random() * fakeNames.length))]
    data = fakeData[Math.floor((Math.random() * fakeData.length))]
    var formData = {
      reviewer:         name,
      comment:          data["comment"],
      stars:            data["stars"],
      enfermedadName:         currentData[enfermedadId].name,
      enfermedadId:           currentData[enfermedadId].id,
    };

    // Ajax post
    $.ajax({ type: 'POST', url: '/api/reviewstriho', data: formData,
      success: function(data) {
        console.log(data);
      },
      error: function() {
        console.log("error")
    }});
  }, 300);

}

function createRandomSuggestions(num) {
  var x = 1;

  var intervalId2 = setInterval(function() {
    if (++ x >= num) {
       window.clearInterval(intervalId2);
    }
    console.log(x);
    // preparing data
    enfermedadId = Math.floor((Math.random() * currentData.length));
    key = changableData[Math.floor((Math.random() * changableData.length))];
    if (key != "sintomaAA") {
      pro = Math.floor((Math.random() * 7));
      value = currentData[enfermedadId][key];
      if (pro == 0) {
        value = values[key][Math.floor((Math.random() * (values[key].length)))];
      }

      // Ajax post
      $.ajax({ type: 'POST', url: '/api/modifications', data: {
          key: key,
          value: value,
          enfermedadName:         currentData[enfermedadId].name,
          enfermedadId:           currentData[enfermedadId].id,
        },
        success: function(data) {
        },
        error: function() {
        }});
    }
  }, 300);
}
