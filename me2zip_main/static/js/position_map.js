// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

var DEFAULT_LAT = 32.776800;
var DEFAULT_LONG = 35.023128;

function centerMap(map_elem_id, latitude=null, longitude=null) {
    if (latitude == null || longitude == null) {
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
            }, function() {
                var errMsg = "Error: The Geolocation service failed.";
            });
        } else {
            var errMsg = "Error: Your browser doesn\'t support geolocation.";
        }
    }
    if (latitude == null || longitude == null) {
        var infoWindowContent = errMsg;
        latitude = DEFAULT_LAT;
        longitude = DEFAULT_LONG;
    } else {
        var infoWindowContent = "Location found.";
    }
    var pos = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById(map_elem_id), {
        center: pos,
        zoom: 6
    });
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(pos);
    infoWindow.setContent(infoWindowContent);


//
//    // Try HTML5 geolocation.
//    if (navigator.geolocation) {
//      navigator.geolocation.getCurrentPosition(function(position) {
//        var pos = {
//          lat: position.coords.latitude,
//          lng: position.coords.longitude
//        };
//
//        infoWindow.setPosition(pos);
//        infoWindow.setContent('Location found.');
//        map.setCenter(pos);
//        window.location.href = '/lat='+pos["lat"]+"&long="+pos["lng"] ; //relative to domain
//      }, function() {
//        handleLocationError(true, infoWindow, map.getCenter());
//      });
//    } else {
//      // Browser doesn't support Geolocation
//      handleLocationError(false, infoWindow, map.getCenter());
//    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                          'Error: The Geolocation service failed.' :
                          'Error: Your browser doesn\'t support geolocation.');
}