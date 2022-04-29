<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>
<body>
<h1>結果出爐啦 ≡ω≡</h1>
<hr/>
<?php
$username=$_POST['user'];
print'名字: ' . $username . ' 大佬<br>';
$add=$_POST['address'];
echo nl2br('<br>隱居地 : '.$add);
print '<br>';
$gender = $_POST['gender'];
switch (strtoupper($gender)) {
    case 'MALE':
        print '<br>性別<br> - Male<br>'; break;
    case 'FEMALE':
        print '<br>性別<br> - Female<br>'; break;
}

$computer = $_POST['X'];
switch ($computer) {
    case 'PC':
        print '<br>學歷<br> - 大學<br>'; break;
    case 'MAC':
        print '<br>學歷<br> - 研究所<br>'; break;
}

if (isset($_POST['GC'])) print '<br>興趣<br> - 打電動<br>';
if (isset($_POST['SF'])) print '<br>興趣<br> - 看書<br>';
if (isset($_POST['FF'])) print '<br>興趣<br> - 睡覺<br>';

$webs = $_POST['Webs'];
foreach ($webs as $value) {
    switch (trim($value)) {
        case 'w1':
            print '<br>喜歡的科目<br> - 程設<br>'; break;
        case 'w2':
            print '<br>喜歡的科目<br> - 網設<br>'; break;
        case 'w3':
            print '<br>喜歡的科目<br> - 微積分<br>'; break;
        case 'w4':
            print '<br>喜歡的科目<br> - 國文<br>'; break;        
    }
}
?>
</body>
</html>