// Setup Map
var map = L.map('map').setView([12.9716, 77.5946], 13);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 20
}).addTo(map);

var socket = io("http://localhost:5000");
var busMarkers = {};

function loadRoutes() {
    fetch("/api/routes")
        .then(res => res.json())
        .then(routes => {
            if (routes.length > 0) loadStops(routes[0].id);
        });
}

function loadStops(routeId) {
    fetch("/api/stops/" + routeId)
        .then(res => res.json())
        .then(stops => {
            let coords = [];

            stops.forEach(s => {
                coords.push([s.latitude, s.longitude]);

                L.circleMarker([s.latitude, s.longitude], {
                    radius: 5,
                    color: "red"
                }).addTo(map).bindPopup(s.name);
            });

            L.polyline(coords, { color: "blue" }).addTo(map);
        });
}

// Load route + stops initially
loadRoutes();

// Websocket listener for bus updates
socket.on("bus_location", function(data) {
    let id = data.bus_id;

    if (!busMarkers[id]) {
        busMarkers[id] = L.marker([data.lat, data.lng]).addTo(map);
    }

    busMarkers[id].setLatLng([data.lat, data.lng]);
    updateETA(data.lat, data.lng);
});

// Simple ETA calculation
function updateETA(lat, lng) {
    fetch("/api/stops/1")
        .then(res => res.json())
        .then(stops => {
            let nextStop = stops[0];
            let dist = getDistance(lat, lng, nextStop.latitude, nextStop.longitude);
            let eta = Math.round(dist / 300);

            document.getElementById("eta-content").innerHTML =
                `Next Stop: ${nextStop.name}<br>ETA: ${eta} minutes`;
        });
}

// Haversine formula
function getDistance(lat1, lon1, lat2, lon2) {
    var R = 6371000;
    var dLat = (lat2 - lat1) * Math.PI / 180;
    var dLon = (lon2 - lon1) * Math.PI / 180;

    lat1 = lat1 * Math.PI / 180;
    lat2 = lat2 * Math.PI / 180;

    var a = Math.sin(dLat / 2) ** 2 +
        Math.cos(lat1) * Math.cos(lat2) * Math.sin(dLon / 2) ** 2;

    return R * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
}