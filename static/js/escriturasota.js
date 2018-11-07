// --------------------------------Variables + Constants---------------------------------------------
// current dishes results

// Preference button clicked
$("#preference-button").on("click", function() {
  $('#outer-box').transition('slide down');

})


// Show preference box & preference button
$( document ).ready(function() {
  $("#preference-link").hide();
  $("#preference-button").show();
  $('#outer-box').transition('slide down');
  setTimeout(function(){ saySomething(true, "Bienvenido"); }, 500);
});
