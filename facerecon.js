(function(){
    var video = document.getElementById("video"),
        canvas= document.getElementById("canvas"),
        context= canvas.getContext("2d"),
        photo = document.getElementById("photo"),
	my=document.getElementById("my")
        vendorURL= window.URL || window.webkitURL;
    
    navigator.getUserMedia = (navigator.getUserMedia || navigator.webkitUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia);

    navigator.getUserMedia({video: {width:400, height: 400},audio: false}, function(stream) {video.srcObject=stream; video.play();}, function(err) {console.log("The following error occoured "+err.name)}	);  

document.getElementById("capture").addEventListener("click", function() { context.drawImage(video,0,0,400, 400);photo.setAttribute("href", canvas.toDataURL("image/jpg"))});

}) ();
