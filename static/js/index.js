function leftmenu() {
    document.getElementById("leftbox").style.display = "block";
    document.getElementById("leftclose").style.display = "block";  
}

function leftclose() {
    document.getElementById("leftbox").style.display = "none";
    document.getElementById("leftclose").style.display = "none";  
}

function rightmenu() {
    document.getElementById("rightbox").style.display = "block";
    document.getElementById("rightclose").style.display = "block"; 
}

function rightclose() {
    document.getElementById("rightbox").style.display = "none";
    document.getElementById("rightclose").style.display = "none";  
}


// This example creates circles on the map, representing populations in North
// America.

// First, create an object containing LatLng and population for each city.
var citymap = {
    chicago: {
      center: { lat: -7.7520, lng: 110.4915 },
      population: 2714856
    }
    
  };
  
  function initMap() {
    // Create the map.
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 11,
      center: { lat: -7.7520, lng: 110.4915 },
      mapTypeId: "terrain"
    });
  
    // Construct the circle for each value in citymap.
    // Note: We scale the area of the circle based on the population.
    for (var city in citymap) {
      // Add the circle for this city to the map.
      var cityCircle = new google.maps.Circle({
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
        map: map,
        center: citymap[city].center,
        radius: 2000
      });
    }
  }