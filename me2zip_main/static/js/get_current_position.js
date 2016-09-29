function getCurrentPosition(onSuccess, onFailure, onNotSupported) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            onSuccess(latitude, longitude)
        }, onFailure);
    } else {
        onNotSupported();
    }
}