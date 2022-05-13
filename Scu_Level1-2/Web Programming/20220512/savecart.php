<?php
session_start();
if (isset($_SESSION['ID'])) {
    $id=$_SESSION['ID'];
    $name=$_SESSION['Name'];
    $price=$_SESSION['Price'];
    $quantity=$_SESSION['Quantity'];
    $q=true;
    //foreach ($_COOKIE as $key => $value) {
        if (isset($_COOKIE[$id]) && is_array($_COOKIE[$id])) {
            foreach ($_COOKIE[$id] as $p => $pv) {
                if ($p == 'Quantity') {
                    setcookie($id.'[Quantity]',$quantity + $pv,time()+3600);
                    $q=false;
                }
            }
        }
    //}
    /*
    foreach ($_COOKIE as $key => $value) {
        foreach ($_COOKIE[$key] as $p => $pv) {
    //foreach ($_COOKIE[$arr] as $i) {
        //list($key,$value)=$i;
        if ($key == $id) {
            foreach ($i as $k=>$v){
                if ($key == 'Quantity') {
                    setcookie($id.'[Quantity]',$quantity + $v,time()+3600);
                    $q=false;
                }
            }
        }
    }   
    */
    if ($q) {
        setcookie($id.'[ID]',$id,time()+3600);
        setcookie($id.'[Name]',$name,time()+3600);
        setcookie($id.'[Price]',$price,time()+3600);
        setcookie($id.'[Quantity]',$quantity,time()+3600);
    }
}
header('Location:shoppingcart.php')
?>