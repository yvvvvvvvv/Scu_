<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale = 1">
  <title></title>
</head>

<body>
<h1>Discount!!!</h1>
<hr/>
<form name = "bonus" method = "post">
  請輸入消費金額: <input type = "text" name = "c" size = "8"><br>
  <br>
  <input type = "submit" value = "送出">
  <input type = "reset" value = "取消">
</form>
<br>
<h2>結果.</h2>
<hr/>
<?php
if (isset($_POST["c"])){
  $a = $_POST["c"];
  if ($a >= 1000){
    if ($a >= 3000) $b = 8;
    elseif ($a >= 2000) $b = 8.5;
    elseif ($a >= 1000) $b = 9;
    $d = $a*$b*0.1;
    echo "消費金額: ".$a."<br>折扣:".$b."<br>折扣後的金額:".$d;
  };
  if ($a < 1000) echo "消費金額: ".$a."<br>不打折";
}
 ?>
</body>
</html>
