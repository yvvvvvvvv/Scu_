<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'/>
    <title>Form_test1</title>
</head>
<body>
<form name='info' method='post' action='test1.php'>    
Gender:<br/>
<input type='radio' name="Gender" value='male' checked/>Male
<input type='radio' name="Gender" value='female'/>Female<br/>
<br/>

Computer System:<br/>
<select name='Computer'>
    <option value='PC' selected>PC</option>
    <option value='MAC'>MAC</option>
</select><br/>
<br/>

Browser:<br/>
<input type='checkbox' name='GC' checked/>Chrome
<input type='checkbox' name='SF'/>Safari
<input type='checkbox' name='FF'/>Firefox<br/>
<br/>

Recommended site:<br/>
<select name='Webs[]' size='4' multiple='True'>
    <option value='w1' selected='True'>Yahoo!</option>
    <option value='w2'>PChome</option>
    <option value='w3'>Hinet</option>
    <option value='w4'>Google</option>
</select><br/>
<br/>

<input type='submit' value='Submit'/>
<input type='reset' value='Reset'/>
</form>
</body>