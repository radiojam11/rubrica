<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Template</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="stile.css" type="text/css" />


</head>
<body>
%ilnome = da_mod["nome"]
%ilcognome = da_mod['cognome']
%ilindirizzo = da_mod['indirizzo']
%iltelefono = da_mod['telefono']
%end
<div class="container_bottoni" >
 
  <div class="row" id="bottoni">
	<div class="col-6"><a href="index.html"><button class="button1" >Home</button></a></div>
  </div>
  
<form action="/msg" method="get" class="form1">

  <div class="form1">
    <label for="Nome">Elem.: </label>
    <input type="text" name="elemento" value= {{elemento}}  >
  </div>
  <div class="form1">
    <label for="Nome">Inserisci il Nome: </label>
    <input type="text" name="nome" value= {{ilnome}}  >
  </div>
  <div class="form1">
    <label for="Cognome">Inserisci il Cognome: </label>
    <input type="text" name="cognome" value= {{ilcognome}} >
  </div>
  <div class="form1">
    <label for="Indirizzo">Inserisci indirizzo: </label>
    <input type="text" name="indirizzo" value= {{ilindirizzo}} >
  </div>
  <div class="form1">
    <label for="Telefono">Inserisci il Telefono: </label>
    <input type="text" name="telefono" value= {{iltelefono}} >
  </div>
  <div class="form1">
    <input type="submit" name="azione" value="modifica">
  </div>


</form>
  </div>



</body>
</html>
