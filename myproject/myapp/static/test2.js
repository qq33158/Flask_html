window.onload = function() {

// 長條圖
var dataPoints = [];

var chart = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	theme: "light2",
	title: {
		text: "人口"
	},
	axisY: {
		title: "People",
		titleFontSize: 24,
		includeZero: true
	},
	data: [{
		type: "column",
		yValueFormatString: "#,### People",
		dataPoints: dataPoints
	}]
});

function addData(data) {
	for (var i = 0; i < data.length; i++) {
		dataPoints.push({
			label : data[i].country,
			y: data[i].population
		});
	}
	chart.render();
}

$.getJSON("static/file.json", addData);

// 橫向長條圖
var dataPoints2 = [];

var chart2 = new CanvasJS.Chart("chartContainer", {
    theme: "light2", // "light1", "dark1", "dark2",
    animationEnabled: true,
    exportEnabled: true,
    title: {
        text: "Top 10 Zipcode Houseprice"
    },
    axisX: {
        margin: 10,
        labelPlacement: "inside",
        tickPlacement: "inside"
    },
    axisY2: {
        title: "(Price/sqft)",
        titleFontSize: 14,
        includeZero: true,
        suffix: ""
    },
    data: [{
        type: "bar",
        axisYType: "secondary",
        yValueFormatString: "#,###.##Price/sqft",
        indexLabel: "{y}",
        dataPoints: dataPoints2
    }]
});

function addData2(data) {
    for (var i = data.length-1; i > -1; i--) {
        dataPoints2.push({
            label : data[i].country,
            y: data[i].population
        });
    }
    chart2.render();
}
$.getJSON("static/file.json", addData2);  

// 比較長條圖
var dataPoints3 = [];
var dataPoints4 = [];
var x ;
var y ;

$.getJSON( "./static/file1.json", function(json){
	$.getJSON( "./static/file2.json", function(json1){
		x = json[0].population.toString();
		y = json1[0].population.toString();
		var chart3 = new CanvasJS.Chart("chartContainer2", {
			exportEnabled: true,
			animationEnabled: true,
			title:{
				text: "Zipcodes Compare"
			},
			subtitles: [{
				text: ""
			}], 
			axisX: {
				title: ""
			},
			axisY: {
				title: "",
				titleFontColor: "#4F81BC",
				lineColor: "#4F81BC",
				labelFontColor: "#4F81BC",
				tickColor: "#4F81BC",
				includeZero: true
			},
			axisY2: {
				title: "",
				titleFontColor: "#C0504E",
				lineColor: "#C0504E",
				labelFontColor: "#C0504E",
				tickColor: "#C0504E",
				includeZero: true
			},
			toolTip: {
				shared: true
			},
			legend: {
				cursor: "pointer",
				itemclick: toggleDataSeries
			},
			data: [{
				type: "column",
				name:x,
				showInLegend: true,      
				yValueFormatString: "#,##0.##",
				dataPoints: dataPoints3,
			},
			{
				type: "column",
				name: y,
				// axisYType: "secondary",
				showInLegend: true,
				yValueFormatString: "#,##0.##",
				dataPoints: dataPoints4,
			}]
		});
		function addData3(data) {
			for (var i = 1; i < data.length; i++) {
				dataPoints3.push({
					label : data[i].country,
					y: data[i].population,
					name: data[0].population,
				});
			}
			chart3.render();
		}
		function addData4(data) {
			for (var i = 1; i < data.length; i++) {
				dataPoints4.push({
					label : data[i].country,
					y: data[i].population,
					name: data[0].population,
				});
			}
			chart3.render();
		}
		$.getJSON("static/file1.json", addData3);
		$.getJSON("static/file2.json", addData4);

		function toggleDataSeries(e) {
			if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
				e.dataSeries.visible = false;
			} else {
				e.dataSeries.visible = true;
			}
			e.chart.render();
	}
	});
});
}
