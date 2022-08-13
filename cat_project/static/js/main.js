/*
var container = document.getElementById('map');
var options = {
    center: new kakao.maps.LatLng(37.638596384798, 127.10767285991),
    level: 3 //지도 최초 표시될 때 확대 정도
};
var map = new kakao.maps.Map(container, options);


var positions = [];
var images = [];

$.ajax({
    url: "{% url 'getApi' %}",
    dataType: "json",
    success: function (data) {
        for (var i = 0; i < data.length; i++) {
            const data1 = $.trim(data[i].fields.photo);
            positions.push({
                title: data[i].fields.name,
                latlng: new kakao.maps.LatLng(data[i].fields.latitude, data[i].fields.longitude)
            });
            if (data[i].fields.photo.length != 0)
                images.push("{% static 'media/' %}" + data[i].fields.photo);
            else
                images.push("https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png");
        }
    },
    error: function (request, status, error) {
        console.log('실패');
    },
    async: false
});
*/

var markers = [];
var level = map.getLevel();

// 마커 클러스터러를 생성합니다 
var clusterer = new kakao.maps.MarkerClusterer({
    map: map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
    averageCenter: true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
    minLevel: 1, // 클러스터 할 최소 지도 레벨 
    gridSize: 40
});
for (var i = 0; i < positions.length; i++) {

    var imageSize = new kakao.maps.Size(33, 33); // 마커 이미지의 이미지 크기 입니다

    var markerImage = new kakao.maps.MarkerImage(images[i], imageSize);// 마커 이미지를 생성합니다  

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image: markerImage // 마커 이미지 
    });
    markers.push(marker)
}
clusterer.addMarkers(markers);