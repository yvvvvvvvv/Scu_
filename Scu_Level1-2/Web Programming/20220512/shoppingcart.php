<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title></title>
<?php
function each(&$array) {
    $res=array();
    $key=key($array);
    if ($key!==null) {
        next($array);
        $res[1]=$res['value']=$array[$key];
        $res[0]=$res['key']=$key;
    }else{
        $res=false;
    }
    return $res;
}
?>
</head>
<body bgcolor="C4E1FF" text='408080'>
<table border='0'>
    <tr bgcolor='E0E0E0'>
        <td>功能</td><td>編號</td><td>名稱</td>
        <td>價格</td><td>數量</td>
<?php
$flag=false;
$total=0;

//date_default_timezone_set('Asia/Taipei');
//$date = date('m/d/Y h:i:s a', time());

/*
foreach ($_COOKIE as $key => $value) {
    if (isset($_COOKIE[$key]) && is_array($_COOKIE[$key])) {
        foreach ($_COOKIE[$key] as $p => $pv) {
            echo '<tr><td>'.$p.'</td><td>'.$pv.'</td></tr>';
        }
    }
    //if ($name == 'Price') $price=$value;
    //if ($name == 'Quantity') $quantity=$value;
}
while (list($arr,$value)=each($_COOKIE)) {
    if (isset($_COOKIE[$arr]) && is_array($_COOKIE[$arr])) {
        //unset($_COOKIE[$arr.'[ID]']); 
        //setcookie($arr.'[ID]', "", time()-3600); 
        echo '<tr><td>removed hh '.$arr.'</td><td>'.$date.'</td></tr>';
    }
}
echo '<tr><td>I am here.</td></tr>';
*/

while (list($arr,$value)=each($_COOKIE)) {
    if (isset($_COOKIE[$arr]) && is_array($_COOKIE[$arr])) {
        if ($flag) {
            $flag=false;
            $color='#C4E1E1';
        } else {
            $flag=true;
            $color='#E1C4C4';
        }
        echo '<tr bgcolor="'.$color.'"><td>';
        echo "<a href='delete.php?ID=".$arr."'>";
        echo '刪除</a></td>';
        $price=0;
        $quantity=0;
        $pname='';
        while (list($name,$value)=each($_COOKIE[$arr])) {
            if ($name == 'Price') $price=$value;
            if ($name == 'Quantity') $quantity=$value;
            if ($name == 'Name') $pname=$value;
        }
        echo '<td>'.$arr.'</td><td>'.$pname.'</td><td>'.$price.'</td><td>'.
        '<div class="purchasenum mt25">
            <i class="minus iconfont icon-subtract"></i>
            <input type="number" min="1" step="1" value='.$quantity.'>
            <i class="plus iconfont icon-jiahao"></i>
        </div>'.'</td>'; //這個暫時還有問題 可以更改但更改後數字無法讀取
        $total=$total+$price*$quantity;
        echo '</tr>';
    }
}
if ($total!=0) {
    echo '<tr bgcolor=#E6E6F2><td colspan=5 align=right>';
    echo '總金額=NT$'.$total.'元</td></tr>';
}
?>
</table>
<hr/> | <a href='catalog.php'>商品目錄</a>
| <a href='shoppingcart.php'>檢視購物車</a>
</body>
</html>
