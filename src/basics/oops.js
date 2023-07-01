// OOPS Javascript

<!DOCTYPE html>
<html>
<body>

<p id="demo"></p>

<script>
########################
//******Parent function******
########################
//Constructor version
function myobj(){
this.name = "venu";
var private = 97;
this.id = "273"
this.rec_fun = function(){
    alert("im your dad");
};
};
//-------creating parent obj--------
var newObj = new myobj();
newObj.prototype.nationality = "Indian"; // adding attributes externally
alert(newObj.id);// 273 
alert(newObj.name); // venu
alert(newObj.nationality);// 
########################
//******child function******
########################
function childobj(){
this.name = "Santosh";
this.id = "45"
var private = 87;
this.rec_fun = function(){
    alert("Im your son");
};
};

//#######creating child obj########
var cobj = new childobj();
//#####################
// inheritance 
//#####################
cobj.prototype = new myobj(); //inheriting parent from child()
//#####################

    alert("im here-1"+ newObj.rec_fun());//undefined & "im your son"
    alert("im here-2"+cobj.rec_fun()); // undefined
    
    alert("im here-3"+newObj.private) //undefined
    alert("im here-4"+cobj.private) //undefined
//----------------------
//Literal Version
var ajaxObj = {
  age : '67'
}
//Literal way of function creation,doing in our dashboard
alert(ajaxObj.age); // 67
ajaxObj.age = "78";
alert(ajaxObj.age); // 78 ,overriding taken place

</script>

</body>
</html>


