$(document).ready(function () {
  //Display Speak Message
  eel.expose(DisplayMessage);
  function DisplayMessage(message) {
    $(".siri-message li:first").text(message);
    $(".siri-message").textillate("start");
  }
  //Display hool
  eel.expose(ShowHood);
  function ShowHood() {
    $("#Oval").removeAttr("hidden").show();
    $("#SiriWave").attr("hidden", true).hide();
  }
});
