
$(document).ready(function () {

  $('.text').textillate({
      loop: true,
      sync: true,
      in: {
          effect: "bounceIn",
      },
      out: {
          effect: "bounceOut",
      },

    });
  // Siri configuration
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style:"ios9",
    amplitude:"1",
    speed:"0.30",
    autostart:true
  });

//siri message animation
$('.siri-message').textillate({
  loop: true,
  in: {
      effect: "fadeInUp",
  },
  out: {
    effect: "fadeOutUp",
  },

});
//mic button click event
$("#MicBtn").click(function(e){
  console.log("Mic button clicked")
  eel.playAssistantSound();
  $("#Oval").attr("hidden", true).hide();
  $("#SiriWave").removeAttr("hidden").show();
  eel.allCommands()()
});
function doc_keyUp(e){
  // this test for whichever key is 40 (down arrow) and the ctrl key at the same time
  if(e.key === 'j' && e.metakey){
    eel.playAssistantSound()
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.allCommands()()
  }
}
document.addEventListener('keyup',doc_keyUp,false);

});

