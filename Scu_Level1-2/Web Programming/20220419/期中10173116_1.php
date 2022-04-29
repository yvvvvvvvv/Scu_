<!DOCTYPE html>
<html>
<head>
  <meta charset = "utf-8">
  <meta name="viewpart" content="width = device-width, initial-scale = 1">
  <title></title>
</head>
<body>
<h1>神奇溫度轉換器 (•͈⌔•͈⑅)</h1>
<hr/>
<h4>**不可以不填喔 會出錯的 ヽ(✿ﾟ▽ﾟ)ノ</h4>
<br>
<form name = "number" method = "post">
  請輸入溫度數值 : <input type="text" name = "temperature" size="8"><br/>
  <br/>
  請選擇種類 : <br/>
  <input type = "radio" name = "trans" value = "F" checked>華氏轉攝氏
  <input type = "radio" name = "trans" value = "C">攝氏轉華氏<br/>
  <br/>
  <input type="submit" value = "送出">
  <input type = "reset" value = "取消">
</form>
<br>
<h2>算出來啦 ♫</h2>
<hr/>
<?php
if (isset($_POST["temperature"])){
  $t = $_POST["temperature"];
  if ($_POST["trans"] == "F"){
    $a = 5/9*($t-32);
    print '溫度 = '.$a.' ℃';
  };
  if($_POST["trans"] == "C"){
    $a = 9/5*$t+32;
    print '溫度 = '.$a.' ℉';
  };
}
 ?>
 
</body>
</html>