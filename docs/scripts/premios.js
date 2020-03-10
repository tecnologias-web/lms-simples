function esconderPremios() {
	var premios = document.getElementsByTagName("article");
	for (var i = 0; i < premios.length; i++) {
		premios[i].style.display = "none";
	}
}

esconderPremios();

var link1 = document.getElementById("link-premio1");
link1.onclick = function(){
	esconderPremios();
	document.getElementById("premio1").style.display = "block";
}
link1.onmouseover = function(){
	this.style.background = "green";
}
link1.onmouseout = function(){
	this.style.background = "transparent";
}

var link2 = document.getElementById("link-premio2");
link2.onclick = function(){
	esconderPremios();
	document.getElementById("premio2").style.display = "block";
}
link2.onmouseover = function(){
	this.style.background = "yellow";
}
link2.onmouseout = function(){
	this.style.background = "transparent";
}

var link3 = document.getElementById("link-premio3");
link3.onclick = function(){
	esconderPremios();
	document.getElementById("premio3").style.display = "block";
}
link3.onmouseover = function(){
	this.style.background = "black";
}
link3.onmouseout = function(){
	this.style.background = "transparent";
}

var link4 = document.getElementById("link-premio4");
link4.onclick = function(){
	esconderPremios();
	document.getElementById("premio4").style.display = "block";
}
link4.onmouseover = function(){
	this.style.background = "red";
}
link4.onmouseout = function(){
	this.style.background = "transparent";
}