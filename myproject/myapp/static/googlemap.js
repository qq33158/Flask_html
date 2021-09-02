let map;
var position = [];
var contentString = [];
var contentString1 =[];
var contentString2 =[];
var contentString3 =[];
var contentString4 =[];
var contentString5 =[];
var contentString6 =[];
var markers = [];

function initMap() {
  $.getJSON( "./static/file3.json", function(json) {
    var x = json[0].zipcode;
    if (x == 98010){
      var lat1 = 47.311403;
      var lng1 = -121.997673;
    }else if (x == 98029){
      var lat1 = 47.555872;
      var lng1 = -122.001514;
    }else if (x == 98092){
      var lat1 = 47.283585;
      var lng1 = -122.128606;
    }else if (x == 98075){
      var lat1 = 47.586461;
      var lng1 = -122.030567;
    }else{ //(x == 98106)
      var lat1 = 47.536346;
      var lng1 = -122.352802;
    }

    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: lat1, lng: lng1 },
      zoom: 12,
      streetViewControl: false,
      mapTypeControl: false,
      // 隱藏商家
      styles: [{
        featureType: 'poi.business',
        stylers: [{
          visibility: 'off'
        }]
      }]
    });
    for(var i = 0; i<json.length;i++){
      contentString.push('預測價格: '+json[i].Predict_price_sqft+' price/sqft');
      contentString6.push(' 實際價格: '+json[i].Actual_price_sqft+' price/sqft');
      contentString1.push('Address: '+json[i].address);
      contentString2.push(' bedroom: '+json[i].bedroom);
      contentString3.push(' bathroom: '+json[i].bathroom);
      contentString4.push(' sqft: '+json[i].sqft)
      position.push({label:'',lat:json[i].lat,lng:json[i].lng});
      contentString5.push("<div id='gm'>"+"<span id='gm2'>"+contentString[i]+"</span>"+"<span id='gm3'>"+contentString6[i]+"</span>"+"</div>"
                        +"<div id='gm1'>"+contentString2[i]+contentString3[i]+contentString4[i]+"</div>"
                        +"<div id='gm1'>"+contentString1[i]+"</div>");
    }
    for (var i = 0; i < position.length; i++) {
      addMarker(i);
    }
  })
}

function addMarker(e) {
    markers[e] = new google.maps.Marker({
      position: {
        lat: position[e].lat,
        lng: position[e].lng,
      },
      map: map,
      label: position[e].label
    });
    const infowindow = new google.maps.InfoWindow({
      content: contentString5[e],
    });
    markers[e].addListener("click", () => {
      infowindow.open({
        anchor: markers[e],
        map,
        shouldFocus: false,
      });
    });
 }
