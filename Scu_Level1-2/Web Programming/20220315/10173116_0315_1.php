<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title></title>
</head>
<body>
<?php

$n='myName';
$$n='y';

echo $n.'<br>';
echo $myName.'<br>';
echo ${$n}.'<br>';
//用$$n要用print
print $$n.'<br>';

?>

<form name='login' method='post' action='0315.php'>
    請輸入第一個值:<input type='text' name='o' size=15><br>
    請輸入第二個值:<input type='text' name='t' size=15><br>
    請輸入第三個值:<input type='text' name='h' size=15><br>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>

</body>
</html>