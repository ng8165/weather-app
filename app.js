if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(receivedCoor);
} else {
    alert("The weather app is not supported in this browser.");
}

function receivedCoor(position) {
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    document.getElementById("loading").style = "display: none;";
    // document.getElementById("coor").innerHTML = "lat: " + lat + ", long: " + long;

    fetch("https://api.weather.gov/points/" + lat + "," + long)
    .then(res => res.json())
    .then(val => {
        fetch(val.properties.forecast)
        .then(res => res.json())
        .then(val => {
            let forecast = document.getElementById("forecast");
            for (let i=0; i<14; i++) {
                day = val.properties.periods[i];
                forecast.innerHTML += day.name + ": " + day.temperature + "°" + day.temperatureUnit + ", " + day.shortForecast + "<br>";
            }
        });
    });
}