<!DOCTYPE html>
<html>
<head>
  <meta charset = "utf-8">
  <meta name="viewpart" content="width = device-width, initial-scale = 1">
  <title></title>
</head>
<body>

<?php
$x = array(1,2,3,4,5,6,7,8,9,10);
$j = 1;
for ($i = 0; $i < 10; $i ++) {
$x[$i] = $j;
$j += 2;
};
$z = 0;
$e = 0;
foreach ($x as $y) {
    echo '索引'.$e.' = '.$y.'<br>';
    $e += 1;
    $z += $y;
};
echo 'Total = '.$z;
?>
</body>
</html>