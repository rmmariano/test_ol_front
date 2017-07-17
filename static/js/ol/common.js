
$(document).ready(function(){
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()  //  Spherical Mercator (EPSG:3857), with meters as map units.
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([37.41, 8.82]),  // it's a point in (EPSG: 4326)
            zoom: 4                                     // and zoom level
        })
    });
});