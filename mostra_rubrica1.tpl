<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Template</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<table>
<tr>
    %for num, elemento in enumerate(mia_rubrica):
        <td>Elem. = {{num+1}}</td>
        <td>Nome = {{elemento['nome']}}</td>
        <td>Cognome = {{elemento['cognome']}}</td>
        <td>Indirizzo = {{elemento['indirizzo']}}</td>
        % for n, num_tel in enumerate(elemento['telefono']):
            <td>Telefono {{n+1}} = {{num_tel}}</td>
        %end
</tr>
    %end
</table>


</body>
</html>
