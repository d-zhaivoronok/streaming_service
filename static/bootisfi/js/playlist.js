$('#upload_song').on('click', function() {
    console.log("add class");
    $('#new_song_add').toggleClass("new_song_add_show");
    $('#album_info').toggleClass("album_info_active");
    document.body.style.overflow =  "hidden";
});

$('#album_create_cancel').on('click', function() {
    $('#new_song_add').toggleClass("new_song_add_show");
    $('#album_info').toggleClass("album_info_active");
    document.body.style.overflow =  "scroll";
});