<?php
	if(isset($_POST['upload'])){
	
	$file_name = $_FILES['file']['name'];
	$file_type = $_FILES['file']['type'];
	$file_size = $_FILES['file']['size'];
	$file_tem_loc = $_FILES['file']['tmp_name'];
	$file_store = "upload/".$file_name;
	move_uploaded_file($file_tem_loc, $file_store);
?>
<!DOCTYPE html>
<html lang='en'>
    <head>
        <meta charset="utf-8"> 
        <title>Document</title>
        <link rel="stylesheet" href="facerecon.css">
	<link rel='stylesheet' href='https://use.fontawesome.com/releases/v5.7.0/css/all.css' integrity='sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ' crossorigin='anonymous'>
    
    </head>
    <body>
	<i style='font-size:30px;' class='fas' id="icn"><a href="index.html"q style="text-decoration: none">&#xf015;</a></i>
        <div class = "frame">
           <video id="video" width="400" height="400"></video> 
           <a id="photo" href=" " download>
        
            <button type="submit" id="capture" class="frame-capture-button">
                Play Music
            </button></a>
	<form action="?" method="post" enctype="multipart/form-data">
	<input type="submit" name="upload" value="upload image"></form>
	<canvas id="canvas" width='400' height='400'></canvas>
        <script type="text/javascript" src="facerecon.js"></script>
</div>
</body>
</html>
