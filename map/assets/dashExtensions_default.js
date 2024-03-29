window.country = Object.assign({}, window.country, {
    assign_marker: {
        pointToLayer: function(feature, latlng) {
            const flag = L.icon({
                iconUrl: `https://flagcdn.com/64x48/${feature.properties.iso2}.png`,
                iconSize: [64, 48]
            });
            return L.marker(latlng, {
                icon: flag
            });
        }
    }
});

