
var DEFAULT_LAT = 32.776800;
var DEFAULT_LONG = 35.023128;

function centerMap(mapElemId, latitude=DEFAULT_LAT, longitude=DEFAULT_LONG, onMapCentered=null) {
    var infoWindowContent = "Location found: " + latitude + ", " + longitude;
    var pos = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById(mapElemId), {
        center: pos,
        zoom: 15
    });
    var infoWindow = new google.maps.InfoWindow({map: map});
    infoWindow.setPosition(pos);
    infoWindow.setContent(infoWindowContent);
    if (onMapCentered) {
        onMapCentered(latitude, longitude)
    }
}