$('#new_playlist').on('click', function() {
    console.log("add class");
    $('#new_playlist_add').toggleClass("new_playlist_add_show");
    document.body.style.overflow =  "hidden"; 
});
  
$('#playlist_create_cancel').on('click', function() {
    $('#new_playlist_add').toggleClass("new_playlist_add_show");
    document.body.style.overflow =  "scroll"; 
});
  