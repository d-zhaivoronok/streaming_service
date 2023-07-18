function handleImageInput(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function() {
        const previewImage = document.getElementById("previewImage");
        previewImage.src = reader.result;
      };
      reader.readAsDataURL(file);
    }
}

const imageInput = document.getElementById("imageInput");
imageInput.addEventListener("change", handleImageInput);