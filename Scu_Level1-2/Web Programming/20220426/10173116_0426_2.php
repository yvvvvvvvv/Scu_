<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
</head>
<body>

<?php
$row0 = array('Joe', 88, 58);
$row1 = array('Jane', 75, 67);
$row2 = array('Mary', 46, 94);
$grades = array($row0, $row1, $row2); 
for ($i = 0; $i < 3; $i ++) {
    $x = 0;
    for ($j = 0; $j < 3; $j ++) {
        if ($j == 0) {        
            echo $grades[$i][$j].':<br>';
        }
        $x += (int)$grades[$i][$j];
        $y = $x / 2;
    }
    echo ' - 加總 = '.$x.'<br> - 平均 = '.(int)$y.'<br>';
}
?>
<?php
$x = array('Joe'=>[88,58],'Jane'=>[75,67],'Mary'=>[46,94]);
//print_r($x);
foreach ($x as $key=>$val) {
    $s = 0;
    foreach ($val as $a) {
        $s += (int)$a;
    };
    echo $key.':<br> - 加總 = '.$s.'<br> - 平均 = '.((int)$s/2).'<br>';
}
?>

</body>     
</html>