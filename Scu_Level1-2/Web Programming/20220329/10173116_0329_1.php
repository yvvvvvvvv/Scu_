<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
<?php
function ave($x,$y,$z){
    $r=($x+$y+$z)/3;
    return $r;
}
function sum($x,$y,$z){
    $r=$x+$y+$z;
    return $r;
}
function ma($x,$y,$z){
    if ($x>$y && $x>$z){
        $m=$x;
    }
    elseif ($y>$x && $y>$z){
        $m=$y;
    }
    elseif ($z>$x &&$z>$y){
        $m=$z;
    }
    return $m;
}
function mi($x,$y,$z){
    if ($x<$y && $x<$z){
        $m=$x;
    }
    elseif ($y<$x && $y<$z){
        $m=$y;
    }
    elseif ($z<$x &&$z<$y){
        $m=$z;
    }
    return $m;
}
?>
</head>
<body>
<?php
    $a=ave(77,88,56);
    $b=sum(77,88,56);
    $c=ma(77,88,56);
    $d=mi(77,88,56);
    echo "平均:".$a.'<br>'."總和:".$b.'<br>'."最大:".$c.'<br>'."最小:".$d.'<br>';
?>
<br>
<?php
//$stamps=mktime(0,0,0,12,3,6);
//print $stamps;
date_default_timezone_set('Asia/Taipei');
$today=getdate();
$month=$today["month"];
$day=$today["mday"];
$year=$today["year"];
$time=$today["hours"].":".$today["minutes"].":".$today["seconds"];
print $year.'/'.$month.'/'.$day.'/'.$time;
?>
</body>
</html>