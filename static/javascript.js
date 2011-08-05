
	$(document).ready(function(){ 
	    var location_tree = window.location.pathname.split("/");
	    var page = location_tree[2];
	    if (page === undefined || location_tree[1] == "post") page = "blog";
	    console.log(page);
	    $("#navbar-" + page).css('background', "#eee");
	  })
