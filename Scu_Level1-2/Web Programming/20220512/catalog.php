<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title></title>
<?php
session_start();
if (isset($_POST['Item'])) {
    $_SESSION['Quantity']=$_POST['Quantity'];
    $id=$_POST['Item'];
    $_SESSION['ID']=$id;
    switch (strtoupper($id)) {
        case 'S001':
            $_SESSION['Name']='10吋變形平板';
            $_SESSION['Price']=12000;
            break;
        case 'S002':
            $_SESSION['Name']='15.6吋筆記型電腦';
            $_SESSION['Price']=27000;
            break;
        case 'S003':
            $_SESSION['Name']='iPhone手機';
            $_SESSION['Price']=21000;
            break;
        case 'S004':
            $_SESSION['Name']='iPad平板';
            $_SESSION['Price']=30000;
            break;
        case 'S005':
            $_SESSION['Name']='電視';
            $_SESSION['Price']=50000;
            break;
        case 'S006':
            $_SESSION["Name"]='Sony手機';
            $_SESSION['Price']=15000;
            break;
        case 'S007':
            $_SESSION["Name"]='Samsung手機';
            $_SESSION['Price']=18000;
            break;
        case 'S008':
            $_SESSION['Name']='HTC手機';
            $_SESSION['Price']=12000;
            break;
        case 'S009':
            $_SESSION['Name']='冰箱';
            $_SESSION['Price']=60000;
            break;
        case 'S010':
            $_SESSION['Name']='洗衣機';
            $_SESSION['Price']=45000;
            break;
    }
    header('Location:savecart.php');
}
?>
</head>
<body bgcolor="C4E1FF" text='408080'>
<form ation='catalog.php' method='post'>
選擇商品:
<select name='Item'>
    <option value='S001'>10吋平板電腦-$12000</option>
    <option value='S002'>15.6吋筆記型電腦-$27000</option>
    <option value='S003'>iPhone手機-$21000</option>
    <option value='S004'>iPad平板-$30000</option>
    <option value='S005'>電視-$50000</option>
    <option value='S006'>Sony手機-$15000</option>
    <option value='S007'>Samsung手機-$18000</option>
    <option value='S008'>HTC手機-$12000</option>
    <option value='S009'>冰箱-$60000</option>
    <option value='S010'>洗衣機-$45000</option>
</select>
<input type='text' size='5' name='Quantity' value='1'>
<input type='submit' value='訂購'>
</form>
</body>
<hr/> | <a href='catalog.php'>商品目錄</a>
| <a href='shoppingcart.php'>檢視購物車</a>
</html>