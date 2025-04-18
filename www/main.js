
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


//siri message animation
$('.siri-message').textillate({
  loop: true,
  sync: true,
  in: {
      effect: "fadeInUp",
      sync:true,
  },
  out: {
    effect: "fadeOutUp",
    sync:true,
  },

});
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