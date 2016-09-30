
var DEFAULT_LAT = 32.776800;
var DEFAULT_LONG = 35.023128;

function centerMap(mapElemId, latitude=DEFAULT_LAT, longitude=DEFAULT_LONG, onMapCentered=null) {
    var pos = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById(mapElemId), {
        center: pos,
        zoom: 15
    });
    // Place a draggable marker on the map
    var marker = new google.maps.Marker({
        position: pos,
        map: map,
        animation: google.maps.Animation.DROP,
        draggable: true,
        title: "Drag me!"
    });

    marker.addListener('dragend', function() {
          pos = marker.getPosition();
          window.location.href = '/mapcoords=' + pos.lat() + ',' + pos.lng();
    });

    if (onMapCentered) {
        onMapCentered(latitude, longitude)
    }
}