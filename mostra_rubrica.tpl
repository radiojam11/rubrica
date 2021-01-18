<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Template</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<table>
    %for num, elemento in enumerate(mia_rubrica):
    <td>Elemento = {{num}}</td>
    <tr>
        %for key in elemento:
        
        <td>{{key}}</td>
            <td>{{elemento[key]}}</td>
        %end
    </tr>
    %end
</table>


</body>
</html>
