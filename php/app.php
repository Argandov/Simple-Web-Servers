<?php 
if (isset($_POST['file'])) {
        $file = fopen("/home/user/reveived_data","w");
        fwrite($file, $_POST['file']);
        fclose($file);
   }
?>
