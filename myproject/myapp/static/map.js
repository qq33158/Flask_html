// 圖表畫布尺寸
const svgSize={ width: 1000,height: 710 };
const margin = { top: 0, right: 0, bottom: 0, left: 0 };
var width = svgSize.width - margin.left - margin.right;
var height = svgSize.height - margin.top - margin.bottom;

// 建立 svg 畫布
var svg = d3
   .select("body")
   .select("svg")
   .attr("width", svgSize.width)
   .attr("height", svgSize.height)
// 建立圖表群組
var chart = svg
   .append("g")
   .attr("transform",`translate(${margin.left},${margin.top})`)
   .attr("class","chart");

// 建立彈出視窗
var tip = d3.select("body")
            .append("div")
            .attr("class", "tip")
            .style("position", "absolute")
            .style("z-index", "10")
            .style("visibility", "hidden");

// 設定投影中心點與縮放倍率
var projection = d3.geoMercator()
                   .center([-121.8, 47.55 ])
                   .scale(33000)
// 建立投影路徑
var path = d3.geoPath()
             .projection(projection);

var x = d3.scaleLinear()
             .domain([0, 390])
             .range([0, 240]);

var color = d3.scaleThreshold()
             .domain([300, 400, 600, 1100,1200])
             .range(["#FFDAC8","#ffcdb5","#ffa57a","#ff5604","#D94600","#b23900"]);

var xAxis = d3.axisBottom()
             .scale(x)
             .tickSize(10)
             .tickValues(color.domain());

chart.call(xAxis)

chart.selectAll("rect")
           .data(color.range().map(function(d, i) {
               return {
                 x0: i ? x(color.domain()[i - 1]) : x.range()[0],
                 x1: i < color.domain().length ? x(color.domain()[i]) : x.range()[1],
                 z: d
               };
             }))
           .enter().append("rect")
           .attr("height", 8)
           .attr("x", function(d) { return d.x0; })
           .attr("width", function(d) { return d.x1 - d.x0; })
           .style("fill", function(d) { return d.z; });

// 匯入資料
d3.json("./static/map.json")
  .then(data => {
    var density = {"98001": 238,"98002": 237,"98003": 235,"98004": 799,"98005": 504,"98006": 448,"98007": 455,"98008": 495,"98010": 224,"98011": 351,"98014": 335,"98019": 278,"98022": 238,"98023": 222,"98024": 369,
      "98027": 373,"98028": 341,"98029": 397,"98030": 235,"98031": 243,"98032": 762,"98033": 585,"98034": 407,"98038": 260,"98039": 1140,"98040": 638,"98042": 232,"98045": 328,"98047": 253,"98051": 302,"98052": 458,
      "98053": 398,"98055": 252,"98056": 355,"98057": 325,"98058": 259,"98059": 315,"98065": 327,"98070": 372,"98072": 359,"98074": 408,"98075": 391,"98077": 363,"98092": 225,"98101": 0,"98102": 628,"98103": 480,
      "98104": 598,"98105": 537,"98106": 362,"98107": 538,"98108": 365,"98109": 601,"98112": 635,"98115": 469,"98116": 457,"98117": 466,"98118": 380,"98119": 579,"98121": 815,"98122": 529,"98125": 408,"98126": 400,
      "98133": 374,"98134": 442,"98136": 425,"98144": 466,"98146": 335,"98148": 269,"98155": 371,"98166": 324,"98168": 264,"98177": 404,"98178": 291,"98188": 270,"98198": 267,"98199": 502,"98224": 307,"98288": 248};
    var color = d3.scaleLinear().domain([300,800]).range(["#FFDAC8","#D94600"]);
    var features = topojson.feature(data, data.objects.Zip_Codes).features;
    for(i=features.length - 1; i >= 0; i-- ) {
      features[i].properties.density = density[features[i].properties.ZIPCODE];
    }

    chart.selectAll("path")
       .data(features)
       .enter()
       .append("path")
       .attr("d", path)
       .attr("fill", function(d) {
              return color(d.properties.density);
       })
      //  地圖的滑鼠事件
       .on("mousemove",(e,d) =>{
      //  改顏色
      //  d3.select(e.currentTarget)
      //    .style("fill","#c58956")
      //  顯示資訊
       tip.text(`Zipcode:${d.properties.ZIPCODE}; Price:${d.properties.density} price/sqft`)
          .style("visibility", "visible")
          .style("top", e.clientY + 40+ "px") 
          .style("left", e.clientX + "px")
       })
      .on("mouseout",e =>{
        d3.select(e.currentTarget)
          //.style("fill","#5692c5")
        tip.style("visibility","hidden");
      })
})
.catch(error => {
    console.log(error);
});