<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
</head>
<body>
<?php
$a=$_POST['o'];
if ($a>120) {
print '全票喔'.'<br/>';
}
elseif ($a<=120 && $a>=110) {
$a*=0.5;
print '半票喔'.'<br/>';
}
else {
print '免費喔'.'<br/>';
}

?>
</body>
</html>