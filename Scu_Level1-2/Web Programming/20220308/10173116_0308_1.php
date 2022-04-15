<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>16.php</title>
</head>
<body>
<table border="1">
    <tr>
        <th>1~20</th>
        <th>books</th>
    </tr>
<?php
for ($i=1;$i<=20;$i++){
?>

<tr>
    <td><?php echo $i ?></td>
    <td><?php print'book'.$i ?></td>
</tr>

<?php
}
?>

</body>
</html>