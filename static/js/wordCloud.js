/**
 * Created with PyCharm.
 * User: Felipe
 * Date: 11/07/14
 * Time: 09:32
 * To change this template use File | Settings | File Templates.
 */


var fill = d3.scale.category20c();

  d3.layout.cloud().size([300, 300])
      .words(d3.zip(jWord, jCount).map(function(d) {
        console.log(d[0], d[1]);
        return {text: d[0], size: d[1]};
      }))
      .padding(5)
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("#chart").append("svg")
        .attr("width", 300)
        .attr("height", 300)
        .attr("style", "float:left; width:300px; height:300px; margin-left:calc(50% - 150px);")
      .append("g")
        .attr("transform", "translate(150,150)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }