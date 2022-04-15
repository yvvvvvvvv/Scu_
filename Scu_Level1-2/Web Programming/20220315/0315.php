<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>
<body>
<?php

$a=$_POST['o'];
$b=$_POST['t'];
$c=$_POST['h'];

echo "\$a*\$b+\$c=[".$a*$b+$c."]<br>";
echo "\$c/\$a=[".$c/$a."]<br>";
echo "\$a<\$b=[".($a<$b)."]<br>";
echo "\$a===\$b=[".($a===$b)."]<br>";
echo "\$a>\$c && \$a<\$b=[".($a>$c&&$a<$b)."]<br>";
echo "\$a<=\$b||\$b>\$c=[".($a<=$b||$b>$c)."]<br>";
echo "\$a >> 1=[".($a >> 1 )."]<br>";
echo "\$c << \$a=[".($c << $a)."]<br>";

?>
</body>
</html>