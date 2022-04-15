<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
<?php
function bmi($X,$Y){
    $Y1=$Y/100;
    $b=$X/($Y1*$Y1);
    return $b;
}
?>
</head>
<body>
<form name='login' method='post' action='10173116_0329_02.php'>
    請輸入你的身高:<input type='text' name='hh' size=15><br>
    請輸入你的體重:<input type='text' name='ww' size=15><br>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>
<?php
if (isset($_POST['hh'],$_POST['ww'])){
    $h=$_POST['hh'];
    $w=$_POST['ww'];
    $BMI=bmi($w,$h);
    print "BMI:".$BMI;
}
?>
</body>
</html>