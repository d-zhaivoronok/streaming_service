window.addEventListener('scroll', function() {
  let content = document.getElementById('header');
  let scrollPosition = window.scrollY;

  if (scrollPosition > 0) {
    content.classList.add('header_scroll');
  } else {
    content.classList.remove('header_scroll');
  }
});

function formatTime(seconds) {
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = Math.floor(seconds % 60);

  const formattedMinutes = minutes.toString().padStart(2, '0');
  const formattedSeconds = secs.toString().padStart(2, '0');

  return `${formattedMinutes}:${formattedSeconds}`;
}


const audioPlayer = document.getElementById('audio-player');

$('#current_time').text(formatTime(audioPlayer.currentTime));
$('#from_all_time').text(formatTime(audioPlayer.duration));



$('#play').on({
  'click': function() {
       if($('#play_img').attr('src') === './imgs/play.png'){
        audioPlayer.play();
        $('#play_img').attr('src', './imgs/pause.png');
       }  else{
        audioPlayer.pause();
        $('#play_img').attr('src', './imgs/play.png');
       }
          
  }
});


$('#song_progress').on('input', function(e) {
  let min = e.target.min,
    max = e.target.max,
    val = e.target.value;

  console.log("change event");

  $(e.target).css({
    'backgroundSize': (val - min) * 100 / (max - min) + '% 100%'
  });

  audioPlayer.currentTime = (val / 1000) * audioPlayer.duration;
}).trigger('input');

$('#song_progress').on('change', function() {
  $('#song_progress').trigger('input');
});

$('#audio-player').on('timeupdate', function() {
  $('#song_progress').val((audioPlayer.currentTime / audioPlayer.duration) * 1000);

  $('#song_progress').attr('value', (audioPlayer.currentTime / audioPlayer.duration) * 1000);


  $('#song_progress').css({
    'backgroundSize': ( $('#song_progress').attr('value') -  $('#song_progress').attr('min')) * 100 / ( $('#song_progress').attr('max') -  $('#song_progress').attr('min')) + '% 100%'
  });
  $('#current_time').text(formatTime(audioPlayer.currentTime));
});


$('#show_list').on('click', function() {
  $('#show_list_img').toggleClass("show_list_img_active");
  document.body.style.overflow = $('#show_list_img').hasClass('show_list_img_active') ? "hidden" : "scroll"; 
  $('#played_song').toggleClass("played_song_active");
});

$('#next_songs_list').on('click', function() {
  if($('#next_songs').hasClass("hide_next")){
    $('#next_songs').toggleClass("hide_next");
    $('#text_song').toggleClass("show_text");
  }
});

$('#text_song_list').on('click', function() {
  if(!$('#text_song').hasClass("show_text")){
    $('#next_songs').toggleClass("hide_next");
    $('#text_song').toggleClass("show_text");
  }
});



