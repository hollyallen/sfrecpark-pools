function searchPool() {
	// Declare variables 
	var input, filter, table, tr, td, i;
	input = document.getElementById("inputPool");
	filter = input.value.toUpperCase();
	table = document.getElementById("poolTable");
	tr = table.getElementsByTagName("tr");

	// Clear out other search input fields
	document.getElementById("inputDay").value = "";
	document.getElementById("inputClass").value = "";

	// Loop through all table rows, and hide those who don't match the search query
	for (i = 0; i < tr.length; i++) {
    	td = tr[i].getElementsByTagName("td")[0];
    	if (td) {
      		if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        		tr[i].style.display = "";
		    } else {
        		tr[i].style.display = "none";
	    	}
		} 
	}
}

function searchDay() {
	// Declare variables 
	var input, filter, table, tr, td, i;
	input = document.getElementById("inputDay");
	filter = input.value.toUpperCase();
	table = document.getElementById("poolTable");
	tr = table.getElementsByTagName("tr");

	// Clear out other search input fields
	document.getElementById("inputPool").value = "";
	document.getElementById("inputClass").value = "";

	// Loop through all table rows, and hide those who don't match the search query
	for (i = 0; i < tr.length; i++) {
    	td = tr[i].getElementsByTagName("td")[1];
    	if (td) {
      		if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        		tr[i].style.display = "";
		    } else {
        		tr[i].style.display = "none";
    		}
	    } 
	}
}

function searchClass() {
	// Declare variables 
	var input, filter, table, tr, td, i;
	input = document.getElementById("inputClass");
	filter = input.value.toUpperCase();
	table = document.getElementById("poolTable");
	tr = table.getElementsByTagName("tr");

	// Clear out other search input fields
	document.getElementById("inputPool").value = "";
	document.getElementById("inputDay").value = "";

	// Loop through all table rows, and hide those who don't match the search query
	for (i = 0; i < tr.length; i++) {
    	td = tr[i].getElementsByTagName("td")[2];
    	if (td) {
      		if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        		tr[i].style.display = "";
		    } else {
        		tr[i].style.display = "none";
    		}
	    } 
	}
}