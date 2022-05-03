<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
<form name='login' method='post' action='10173116_0503_1.php' >
	請輸入字串:<input type='text' name='strr' size=15><br>
	<input type="submit" value="送出" >
</form>
	

<?php
if (isset($_POST['strr'])) {
	$str=$_POST['strr'];
	print($str."<br/>");
    print("strlen(\$str)=".strlen($str)."<br/>");
    print("strpos(\$str)=".strpos($str,"r")."<br/>");
    print("strrev(\$str)=".strrev($str)."<br/>");
    print("substr(\$str)=".substr($str,3,6)."<br/>");

}
?>



</body>
</html>