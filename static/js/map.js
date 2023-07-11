
// Harita oluşturma
var harita = L.map('harita').setView([38.9637, 35.2433], 6);

// Harita veri kaynağı olarak kullanılan bir görüntü veya yer sağlayıcısı belirleme
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Harita verileri &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
    maxZoom: 18,
}).addTo(harita);

// Marker verilerini içeren bir dizi oluşturma
var markerData = [
    { koordinat: [40.914, 38.3895], isim: "Giresun", url: "https://www.google.com/maps?q=40.914,38.3895" },
    { koordinat: [36.85386, 30.91784], isim: "Antalya", url: "https://www.google.com/maps?q=36.85386,30.91784" },
    // Diğer marker verileri buraya eklenecek
];

// Her bir marker için döngü oluşturma
for (var i = 0; i < markerData.length; i++) {
    var markerInfo = markerData[i];

    // Marker'ı oluşturma ve haritaya ekleme
    var marker = L.marker(markerInfo.koordinat).addTo(harita);
    marker.bindPopup(markerInfo.isim);

    marker.on('mouseover', function (e) {
        this.openPopup();
    });

    marker.on('mouseout', function (e) {
        this.closePopup();
    });

    // Marker'a tıklandığında yönlendirme yapma
    marker.on('click', createClickHandler(markerInfo));
}

// Kapanış fonksiyonunu oluşturma
function createClickHandler(markerInfo) {
    return function() {
        window.open(markerInfo.url);
    };
}
