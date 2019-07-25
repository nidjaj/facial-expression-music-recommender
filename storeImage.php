<?php
    header('location: Sentiment.html');
    $img = $_POST['image'];
    $folderPath1 = "/var/www/cgi-bin/";
    $folderPath2 = "/var/www/html/";
  
    $image_parts = explode(";base64,", $img);
    $image_type_aux = explode("image/", $image_parts[0]);
    $image_type = $image_type_aux[1];
  
    $image_base64 = base64_decode($image_parts[1]);
    $fileName = 'image' . '.jpeg';
  
    $file1 = $folderPath1 . $fileName;
    file_put_contents($file1, $image_base64);

    $file2 = $folderPath2 . $fileName;
    file_put_contents($file2, $image_base64);
  
    echo "successfully saved snap. Snap id : ";
    print_r($fileName);

    $namefile = "imageid.txt";
    $fp = fopen($namefile, "w");
    fwrite($fp,$fileName);
    fclose($fp)
    
  
?>
