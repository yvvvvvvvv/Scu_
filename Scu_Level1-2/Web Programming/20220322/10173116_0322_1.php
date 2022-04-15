<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
</head>
<body>

<form name='login' method='post' action='10173116_0322_2.php'>
    請輸入原價:<input type='text' name='o' size=15>(過1000打85折)<br>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>
<br>
<form name='login' method='post' action='10173116_0322_3.php'>
    請輸入身高:<input type='text' name='o' size=15>(過120全票,110-120半票,110以下免費喔)<br>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>
<br>
<?php
$a = 0;
for ( $i = 1; $i <= 100; $i++ ) {
    if ( $i >= 35 && $i <= 57 ) {
        if ( $i % 2 != 0 ) {
            $a += $i;
        }
    }
}
print '35-57奇數總和='. $a
?>
<br><br>
<?php
$a = 250;
$n = 0;
while ( $a > 20 ) {
    $a /= 2;
    $n += 1;

}
$n - 1;
print '繩長成'. $a. ',需對折'. $n. '次'
?>
<br><br>
<?php
for ( $s = 4; $s <= 100; $s++ ) {
    if ( $s % 4 == 0 ) {
        print $s. ' ';
    }
}
?>

</body>
</html>
