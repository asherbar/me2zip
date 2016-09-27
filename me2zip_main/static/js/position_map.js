// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

var DEFAULT_LAT = 32.776800;
var DEFAULT_LONG = 35.023128;

function centerMap(map_elem_id, latitude=null, longitude=null, set_url=false) {
    var errMsg = '';
    if (latitude == null || longitude == null) {
        centerMap(map_elem_id, DEFAULT_LAT, DEFAULT_LONG, false);
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
                centerMap(map_elem_id, latitude, longitude, set_url);
            }, function() {
                alert("Error: The Geolocation service failed.");
                centerMap(map_elem_id, DEFAULT_LAT, DEFAULT_LONG, set_url);
            });
        } else {
            alert("Error: Your browser doesn\'t support geolocation.");
            centerMap(map_elem_id, DEFAULT_LAT, DEFAULT_LONG, set_url);
        }
        return;
    }
    var infoWindowContent = "Location found:" + latitude + "," + longitude;
    var pos = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById(map_elem_id), {
        center: pos,
        zoom: 15
    });
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(pos);
    infoWindow.setContent(infoWindowContent);
    if (set_url) {
        window.location.href = '/lat=' + latitude + '&long=' + longitude;
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                          'Error: The Geolocation service failed.' :
                          'Error: Your browser doesn\'t support geolocation.');
}