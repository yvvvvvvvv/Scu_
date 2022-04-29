<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title></title>
</head>
<script>
function a() {
var x = document.forms['login']['user'].value;
var x = document.forms['login']['pass'].value;
    if (x == '' || y == '') {
        alert('姓名或密碼不能為空值');
        return false;
    }
}
</script>
<body>
<h1>會員註冊表單單</h1>
<hr/>
<form name='login' method='post' action='期中10173116_3_2.php' onsubmit="return a()">
    <vu>
    姓名:<input type='text' name='user' size=15><br>
    密碼:<input type='password' name='pass' size=15><br><br>
    地址:<textarea name='address' rows=5 cols=50></textarea><br><br>
    性別:<input type=radio name='gender' value='male' checked>男
        <input type=radio name='gender' value='female'>女<br><br>
    學歷:<br/>
    <select name='X'>
    <option value='PC' selected>大學</option>
    <option value='MAC'>研究所</option>
    <br/>
    </select><br/>
    <br/>
    興趣:<br/>
    <input type='checkbox' name='GC' checked/>打電動
    <input type='checkbox' name='SF'/>看書
    <input type='checkbox' name='FF'/>睡覺<br/>
    <br/>
    喜歡的課程:<br/>
    <select name='Webs[]' size='4' multiple='True'>
    <option value='w1' selected='True'>程設</option>
    <option value='w2'>網設</option>
    <option value='w3'>微積分</option>
    <option value='w4'>國文</option>
    </select><br/>
    <br/>
    <input type='submit' value='送出'>
    <input type='reset' value='取消'>
</form>
</body>
</html>