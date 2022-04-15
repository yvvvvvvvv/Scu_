<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
</head>
<body>
<?php
$a=$_POST['o'];
if ($a>=1000) $a*=0.85;
print '付款金額:'.$a.'<br/>';
?>
</body>
</html>