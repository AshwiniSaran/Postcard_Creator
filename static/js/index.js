//index.js

var selectedImage;
var pos;
function allowDrop(ev) {
    ev.preventDefault();
}
function get_pos(ev) {
    pos = [ev.pageX, ev.pageY];
    console.log(ev);
}
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var offset = ev.dataTransfer.getData("text/plain").split(',');
    var data = ev.dataTransfer.getData("text");

    var img = document.getElementById(data);
    selectedImage = new Image();
    selectedImage.src = img.src;

    selectedImage.onload = function () {
        fill_canvas(selectedImage);

    }
    submitImg();
}
function loadImage(input) {

    if (input.files[0]) {
        var reader = new FileReader();
        reader.onloadend = function (e) {
            selectedImage = new Image();
            selectedImage.src = e.target.result;

            selectedImage.onload = function () {
                fill_canvas(selectedImage);
            }
        }
        reader.readAsDataURL(input.files[0]);
    }
    clearMessage();
    submitImg();


}
function clearMessage() {
    var greetingtext = document.getElementById('greetingMsg');
    greetingtext.value = "";

}
function resetImage() {
    var resetImg = new Image();
    if (selectedImage) {
        resetImg.src = selectedImage.src;
        resetImg.onload = function () {
            fill_canvas(resetImg);
        }
    }
    submitImg();


}
function fill_canvas(img) {
    var canvas = document.getElementById("postCardCanvas");
    var ctx = canvas.getContext('2d');
    canvas.width = img.width;
    canvas.height = img.height;
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    clearMessage();


}

function fillText(txt) {
    var canvas = document.getElementById("postCardCanvas");
    var ctx = canvas.getContext('2d');

    ctx.font = "20px Verdana";
    var gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
    gradient.addColorStop("0.20", "white");
    gradient.addColorStop("0.40", "yellow");
    gradient.addColorStop("0.60", "red");
    gradient.addColorStop("0.80", "white");
    gradient.addColorStop("1.0", "magenta");
    ctx.fillStyle = gradient;
    ctx.fillText(txt.value, 10, (canvas.height * .85));
    submitImg();

}

function validateemailadd() {
    var senderemailadd = document.forms["frmUpload"]["senderEmail"].value;
    var recipientemailadd = document.forms["frmUpload"]["recipientEmail"].value;
    var atpos = senderemailadd.indexOf("@");
    var dotpos = senderemailadd.lastIndexOf(".");
    if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= x.length) {
        alert("Invalid email address");

    }
    var atpos = recipientemailadd.indexOf("@");
    var dotpos = recipientemailadd.lastIndexOf(".");
    if (atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= x.length) {
        alert("Invalid email address");

    }
}

function submitImg() {

    var canvas = document.getElementById('postCardCanvas');
    document.getElementById('inp_img').value = canvas.toDataURL();
    console.log("canvas loaded to input")

}

window.onload = function () {

    var resetImg = document.getElementById('dragAndDropId');
    var baseimage = new Image();
    baseimage.src = resetImg.src;
    fill_canvas(baseimage);
    submitImg();
}
function triggermodal() {
    var modalbtn = document.getElementById('modalbtn');
    console.log('modal trigger');
    modalbtn.click();
}