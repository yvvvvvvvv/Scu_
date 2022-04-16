<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title>test1</title>
</head>
<body>
<?php

$gender = $_POST['Gender'];
switch (strtoupper($gender)) {
    case 'MALE':
        print 'Gender<br> - Male<br>'; break;
    case 'FEMALE':
        print 'Gender<br> - Female<br>'; break;
}

$computer = $_POST['Computer'];
switch ($computer) {
    case 'PC':
        print 'Computer<br> - Using PC<br>'; break;
    case 'MAC':
        print 'Computer<br> - Using MAC<br>'; break;
}

if (isset($_POST['GC'])) print 'Brower<br> - Using Google Chrome<br>';
if (isset($_POST['SF'])) print 'Brower<br> - Using Safari<br>';
if (isset($_POST['FF'])) print 'Brower<br> - Using Firefox<br>';

$webs = $_POST['Webs'];
foreach ($webs as $value) {
    switch (trim($value)) {
        case 'w1':
            print 'Web site<br> - Yahoo!<br>'; break;
        case 'w2':
            print 'Web site<br> - PChome<br>'; break;
        case 'w3':
            print 'Web site<br> - Hinet<br>'; break;
        case 'w4':
            print 'Web site<br> - Google<br>'; break;        
    }
}

?>
</body>
</html>