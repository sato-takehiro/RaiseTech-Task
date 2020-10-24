//うまく機能していない
$(function() {
	function calcParallax(tileheight, speedratio, scrollposition) {
		//    by Brett Taylor http://inner.geek.nz/
		//    originally published at http://inner.geek.nz/javascript/parallax/
		//    usable under terms of CC-BY 3.0 licence
		//    http://creativecommons.org/licenses/by/3.0/
		return ((tileheight) - (Math.floor(scrollposition / speedratio) % (tileheight+1)));
	  }
	  window.onload = function() {
		  window.onscroll = function() {
			  var posY = (document.documentElement.scrollTop) ? document.documentElement.scrollTop : window.pageYOffset;

			  var ground = document.getElementByClass('c-hero');
			  var groundparallax = calcParallax(900, 8, posY);
			  ground.style.backgroundPosition = "0 " + groundparallax + "px";
		  }
	  }
});
