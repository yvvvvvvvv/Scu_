<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>
<body>
<?php
$username=$_POST['user'];
print'姓名:' . $username . '<br>';
$add=$_POST['address'];
echo nl2br($add);
?>
</body>
</html>