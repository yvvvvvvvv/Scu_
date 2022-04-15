<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title>表單16</title>
</head>
<body>
<form name='login' method='post' action='h1.php'>
    請輸入你的名稱:<input type='text' name='user' size=15><br>
    請輸入你的密碼:<input type='password' name='pass' size=15><br>
    請輸入你的地址:<textarea name='address' rows=5 cols=50></textarea><br>
    請選擇性別:<input type=radio name='gender' value='male' checked>男
              <input type=radio name='gender' value='female'>女<br>
    <input type='submit' value='送出'>
</form>
</body>
</html>