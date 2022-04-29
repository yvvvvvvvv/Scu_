<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>
<body>
<form name='tem' method='post' action='10173116_0419_1.php'>
溫度:
<input type='text' name='t' size=8><br>
轉換方式:<br/>
<input type='radio' name="trans" value='cf' checked/>攝氏轉華氏
<input type='radio' name="trans" value='fc'/>華氏轉攝氏
<br/>
<input type='submit' value='計算'/>
<input type='reset' value='重來'/>

<?php
if (isset($_POST['tem'],$_POST['trans'])){
$tem = $_POST['tem'];
$trans = $_POST['trans'];
$fc = 5/9*($tem-32);
$cf = 9/5*$tem+32;
if ($trans == 'cf') {
    print '溫度'.$cf.'℉';
}
else {
    print '溫度'.$fc.'℃';
}
}
?>

</form>
</body>
</html>
