<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Template</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<table>
    %for elemento in rubrica:
    <tr>
        %for key in elemento:
            <td>{{key}}</td>
        %end
    </tr>
    %end
</table>

<div class="container_bottoni" >
<div class="row">
    <div class="col-12" align="center" id="titolo_pag"><h1 align="center">Benvenuto nel nostro ascensore </h1></div>
	</div>



  <div class="row">
    <div class="col-12" align="center" id="titolo_bottoni"><h2>Scegli il tuo piano</h2></div>
	</div>
	
	<div class="row" id="bottoni">
	<div class="col-6"><a href="piani/piano1.html"><button class="button1" >1</button></a></div>
	<div class="col-6"><a href="piani/piano2.html"><button class="button1" >2</button></a></div>
  </div>
  <div class="row" id="bottoni">
	<div class="col-6"><a href="piani/piano3.html"><button class="button1" >3</button></a></div>
	<div class="col-6"><a href="piani/piano4.html"><button class="button1" >4</button></a></div>
  </div>

<div class="row" id="bottoni">
	<div class="col-6"><a href="piani/piano5.html"><button class="button1" >5</button></a></div>
	<div class="col-6"><a href="piani/piano6.html"><button class="button1" >6</button></a></div>
  </div>
  <div class="row" id="bottoni">
	<div class="col-6"><span style="color: red;"><i class="fas fa-bell"></i></span></div>
	<div class="col-6"><span style="color: Dodgerblue;"><i class="fas fa-phone"></i></div>
  </div>

</div>





</body>
</html>
