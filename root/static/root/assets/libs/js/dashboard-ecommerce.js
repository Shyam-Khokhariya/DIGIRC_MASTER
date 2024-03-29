$(function() {
    new Chartist.Bar('.ct-chart-product', {
        labels: ['Ghost', 'Wraith', 'Dawn', 'Phantom'],
        series: [
            [800000, 1200000, 1400000, 1300000],
            [200000, 400000, 500000, 300000],
            [100000, 200000, 400000, 600000]
        ]
    }, {
    stackBars: true,
        axisY: {
            labelInterpolationFnc: function(value) {
                return (value / 1000) + 'k';
            }
        }
    }).on('draw', function(data) {
        if (data.type === 'bar') {
            data.element.attr({
                style: 'stroke-width: 40px'
            });
        }
    });
});

var chart = new Chartist.Pie('.ct-chart-category', {
 series: [60, 30, 30],
 labels: ['Bananas', 'Apples', 'Grapes']
}, {
 donut: true,
 showLabel: false,
 donutWidth: 40
});

chart.on('draw', function(data) {
 if (data.type === 'slice') {
     var pathLength = data.element._node.getTotalLength();
     data.element.attr({
         'stroke-dasharray': pathLength + 'px ' + pathLength + 'px'
     });
     var animationDefinition = {
         'stroke-dashoffset': {
             id: 'anim' + data.index,
             dur: 1000,
             from: -pathLength + 'px',
             to: '0px',
             easing: Chartist.Svg.Easing.easeOutQuint,
             fill: 'freeze'
         }
     };
     if (data.index !== 0) {
         animationDefinition['stroke-dashoffset'].begin = 'anim' + (data.index - 1) + '.end';
     }
     data.element.attr({
         'stroke-dashoffset': -pathLength + 'px'
     });
     data.element.animate(animationDefinition, false);
 }
});

var chart = new Chartist.Line('.ct-chart', {
 labels: ['Mon', 'Tue', 'Wed'],
 series: [
     [1, 5, 2, 5],
     [2, 3, 4, 8]

 ]
}, {
 low: 0,
 showArea: true,
 showPoint: false,
 fullWidth: true
});

chart.on('draw', function(data) {
 if (data.type === 'line' || data.type === 'area') {
     data.element.animate({
         d: {
             begin: 2000 * data.index,
             dur: 2000,
             from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
             to: data.path.clone().stringify(),
             easing: Chartist.Svg.Easing.easeOutQuint
         }
     });
 }
});

$("#sparkline-revenue").sparkline([5, 5, 7, 7, 9, 5, 3, 5, 2, 4, 6, 7], {
 type: 'line',
 width: '99.5%',
 height: '100',
 lineColor: '#5969ff',
 fillColor: '#dbdeff',
 lineWidth: 2,
 spotColor: undefined,
 minSpotColor: undefined,
 maxSpotColor: undefined,
 highlightSpotColor: undefined,
 highlightLineColor: undefined,
 resize: true
});

$("#sparkline-revenue2").sparkline([3, 7, 6, 4, 5, 4, 3, 5, 5, 2, 3, 1], {
 type: 'line',
 width: '99.5%',
 height: '100',
 lineColor: '#ff407b',
 fillColor: '#ffdbe6',
 lineWidth: 2,
 spotColor: undefined,
 minSpotColor: undefined,
 maxSpotColor: undefined,
 highlightSpotColor: undefined,
 highlightLineColor: undefined,
 resize: true
});

$("#sparkline-revenue3").sparkline([5, 3, 4, 6, 5, 7, 9, 4, 3, 5, 6, 1], {
 type: 'line',
 width: '99.5%',
 height: '100',
 lineColor: '#25d5f2',
 fillColor: '#dffaff',
 lineWidth: 2,
 spotColor: undefined,
 minSpotColor: undefined,
 maxSpotColor: undefined,
 highlightSpotColor: undefined,
 highlightLineColor: undefined,
 resize: true
});

$("#sparkline-revenue4").sparkline([6, 5, 3, 4, 2, 5, 3, 8, 6, 4, 5, 1], {
 type: 'line',
 width: '99.5%',
 height: '100',
 lineColor: '#fec957',
 fillColor: '#fff2d5',
 lineWidth: 2,
 spotColor: undefined,
 minSpotColor: undefined,
 maxSpotColor: undefined,
 highlightSpotColor: undefined,
 highlightLineColor: undefined,
 resize: true,
});

Morris.Area({
 element: 'morris_totalrevenue',
 behaveLikeLine: true,
 data: [
     { x: '2016 Q1', y: 0, },
     { x: '2016 Q2', y: 2000, },
     { x: '2017 Q3', y: 4000, },
     { x: '2017 Q4', y: 5000, },
     { x: '2018 Q5', y: 8000, },
     { x: '2018 Q6', y: 9000, }
 ],
 xkey: 'x',
 ykeys: ['y'],
 labels: ['Y'],
 lineColors: ['#5969ff'],
 resize: true
});

var chart = c3.generate({
 bindto: "#c3chart_category",
 data: {
     columns: [
         ['Dawn', 100],
         ['Ghost', 80],
         ['Phantom', 50],
         ['Wraith', 40],
     ],
     type: 'donut',
     onclick: function(d, i) { console.log("onclick", d, i); },
     onmouseover: function(d, i) { console.log("onmouseover", d, i); },
     onmouseout: function(d, i) { console.log("onmouseout", d, i); },
     colors: {
         Dawn: '#5969ff',
         Ghost: '#ff407b',
         Phantom: '#25d5f2',
         Wraith: '#ffc750',
     }
 },
 donut: {
     label: {
         show: false
     }
 },
});