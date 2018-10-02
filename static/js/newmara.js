// Variables to store file uploaded.
var allFiles = [];
var numberOfValidatedFile = 0;

// Show form
$( document ).ready(function() {
  $('#preference-box').transition('scale'); //Antes era slide down
  setTimeout(function(){ saySomething(false, "Gracias por enriquecer a AgroEX"); }, 500);
});

// Fake file-upload-button clicked
$("#file-upload").on("click", function() {
   $('#hidden-file-upload').click();
});

// Uploading a new file
$("#hidden-file-upload").on("change", function(e) {
  var files = e.target.files;
  var f = files[0];

  if (f.type.match('image.*') && numberOfValidatedFile <= 4) {
    // update necessary things
    numberOfValidatedFile ++;
    $('#images').val('ok');

    // render to view
    var id = allFiles.length;
    var reader = new FileReader();
    reader.onload = (function(theFile) {
      return function(e) {
        allFiles.push(e.target.result);
        var text = '<div class="thumb" id="image-'+id+'" style="display: none">' +
          '<img src="'+e.target.result+'">' +
          '<i class="remove circle icon red big remove-button" onclick="removeFile('+id+')"></i>' +
        '</div>';

        $("#list").append(text);
        $("#image-"+id).transition('scale');
      };
    })(f);
    reader.readAsDataURL(f);
  } else {
    saySomething(true, "Disculpe, no puede publicar tantas imágenes")
  }
})

// Delete an uploaded image
function removeFile(id) {
  $("#image-"+id).transition('scale');
  allFiles[id] = 'null';
  numberOfValidatedFile --;
  if (numberOfValidatedFile == 0) {
    $('#images').val('');
  }
}
function removeAllFiles() {
  numberOfValidatedFile = 0;
  allFiles = [];
  $('#images').val('');
  $('#list').html('');
}

// Submit Form Handling
$("#submit-button").on("click", function() {
  // $("#submit-button").addClass("loading");
});

// Form Validation
$("#form-nuevo-enfermedad").form({
    enfermedadname: {
      identifier: 'enfermedad-name',
      rules: [{
        type   : 'empty',
        prompt : 'Por favor, ingrese el nombre de la enfermedad de la planta'
      }]
    },
    planta: {
      identifier: 'planta',
      rules: [{
        type    : 'empty',
        prompt  : 'Please choose the planta'
      }]
    },
    sintomaAAA: {
      identifier: 'sintoma-aa',
      rules: [{
        type    : 'checked',
        prompt  : '¿Hay perforaciones en la hoja?'
      }]
    },
 //   sintomaAAA: {
 //     identifier: 'sintoma-aa',
 //     rules: [{
 //       type    : 'checked',
 //       prompt  : 'Please specify if the food is vegetarian'
 //     }]
 //   },
    sintomacc: {
      identifier: 'sintoma-cc',
      rules: [{
        type    : 'checked',
        prompt  : '¿Qué formas tienen las manchas?'
      }]
    },
    //sour: {
      //identifier: 'sour-level',
     // rules: [{
     //   type    : 'checked',
     //   prompt  : 'Please specify the sour level'
    //  }]
    //},
    sintomadd: {
      identifier: 'sintoma-dd',
      rules: [{
        type    : 'checked',
        prompt  : '¿Se presenta acame?'
      }]
    },
    sintomaee: {
      identifier: 'sintoma-ee',
      rules: [{
        type    : 'checked',
        prompt  : '¿¿Dónde están distribuidas las lesiones??'
      }]
    },
//    fat: {
  //    identifier: 'fat-level',
    //  rules: [{
     //   type    : 'checked',
       // prompt  : 'Please specify the fat level'
    //  }]
//    },
//    fiber: {
//      identifier: 'fiber-level',
//      rules: [{
//        type    : 'checked',
//        prompt  : 'Please specify the fiber level'
//      }]
//    },
//    calorie: {
//      identifier: 'calorie-level',
//      rules: [{
//        type    : 'checked',
//        prompt  : 'Please specify the calorie level'
//      }]
//    },
    description: {
      identifier: 'description',
      rules: [{
        type    : 'empty',
        prompt  : 'Por favor, agrega un tratamiento para la cura de la planta'
      }]
    },
    images: {
      identifier: 'images',
      rules: [{
        type    : 'empty',
        prompt  : 'Por favor, publica una imagen de la planta'
      }]
    }
}, {
  onSuccess: function() {
    submitForm();
    return false;
  },
  onFailure: function() {
    saySomething(true, "Ocurrió un error, disculpe")
    return false;
  }
});

// Submitting Form
function submitForm() {
  // preparing data
  var formData = {
    name:         $('#form-nuevo-enfermedad').find('input[name="enfermedad-name"]').val(),
    planta:      $('#form-nuevo-enfermedad').find('select[name="planta"]').val(),
    sintomaDD:   $('#form-nuevo-enfermedad').find('input[name="sintoma-dd"]:checked').val(),
    sintomaCC:   $('#form-nuevo-enfermedad').find('input[name="sintoma-cc"]:checked').val(),
//    sourLevel:    $('#form-nuevo-enfermedad').find('input[name="sour-level"]:checked').val(),
    sintomaEE:   $('#form-nuevo-enfermedad').find('input[name="sintoma-ee"]:checked').val(),
//    fatLevel:     $('#form-nuevo-enfermedad').find('input[name="fat-level"]:checked').val(),
//    carbLevel:    $('#form-new-dish').find('input[name="carb-level"]:checked').val(),
//    calorieLevel: $('#form-new-dish').find('input[name="calorie-level"]:checked').val(),
//    fiberLevel:   $('#form-new-dish').find('input[name="fiber-level"]:checked').val(),
    sintomaAA: $('#form-nuevo-enfermedad').find('input[name="sintoma-aa"]:checked').val(),
    sintomaBB:      $('#form-nuevo-enfermedad').find('input[name="sintoma-bb"]:checked').val(),
    description:  $('#description').val(),
    images:       JSON.stringify(allFiles),
  };

  $("#form-nuevo-enfermedad").addClass("loading");

  // Ajax post
  $.ajax({ type: 'POST', url: '/api/dishesmara', data: formData,
    success: function(data) {
      console.log(data);
      removeAllFiles();
      $("#form-nuevo-enfermedad").form("reset");
      $("#form-nuevo-enfermedad").removeClass("loading");
      saySomething(true, "Gracias por enriquecer a AgroEX");
    },
    error: function() {

  }});
}
