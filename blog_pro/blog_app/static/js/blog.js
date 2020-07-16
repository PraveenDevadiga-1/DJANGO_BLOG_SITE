$('#scene').parallax({
  frictionX: 0.1,
  frictionY: 0.1
});

moveBubbles();
setInterval(function(){
  moveBubbles();
}, 8000);

function moveBubbles () {
  $('li div').each(function() {

    var random = Math.ceil(Math.random() * 100);
    var random2 = Math.ceil(Math.random() * 100);

    var whatWay = Math.ceil(Math.random() * 2);

    if(whatWay == 1) {
      $(this).transition({
        x: "+=" + random + "",
        y: "+=" + random2 + ""
      }, 8000, "linear");

    } else {

      $(this).transition({
        x: "-=" + random + "",
        y: "-=" + random2 + ""
      }, 8000, "linear");
    }
  });
}
