<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>

<script>
function a() {
var x = document.forms['login']['hh'].value;
var x = document.forms['login']['ww'].value;
    if (x == '' || y == '') {
        alert('不能為空值');
        return false;
    }
}
</script>

<body>

<form name='login' method='post' action='10173116_0412_1.php' onsubmit="return a()">
    請輸入你的身高:<input type='text' name='hh' size=15><br>
    請輸入你的體重:<input type='text' name='ww' size=15><br>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>

<?php
if (isset($_POST['hh'],$_POST['ww'])){
$w=$_POST['ww'];
$BMI = function($h) use($w) {
    $h = $h / 100.0;
    return $w/$h/$h;
};
$h=$_POST['hh'];
echo '<br>'."BMI:".$BMI($h);
}
?>
</body>
</html>