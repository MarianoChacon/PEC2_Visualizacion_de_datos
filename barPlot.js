const rawData = [
  [3384248, 980318, 1807398],
  [1260348, 363199, 617132],
  [2337638, 653563, 994800],
  [1712042, 502407, 727701],
  [239428, 64461, 133853]
];
const totalData = [];
for (let i = 0; i < rawData[0].length; ++i) {
  let sum = 0;
  for (let j = 0; j < rawData.length; ++j) {
    sum += rawData[j][i];
  }
  totalData.push(sum);
}
const grid = {
  left: 100,
  right: 100,
  top: 50,
  bottom: 50
};
const gridWidth = myChart.getWidth() - grid.left - grid.right;
const gridHeight = myChart.getHeight() - grid.top - grid.bottom;
const categoryWidth = gridWidth / rawData[0].length;
const barWidth = categoryWidth * 0.6;
const barPadding = (categoryWidth - barWidth) / 2;
const series = [
  'Consumption',
  'capital formation',
  'Exports'
].map((name, sid) => {
  return {
    name,
    type: 'bar',
    stack: 'total',
    barWidth: '60%',
    label: {
      show: true,
      formatter: (params) => Math.round(params.value * 1000) / 10 + '%'
    },
    data: rawData[sid].map((d, did) =>
      totalData[did] <= 0 ? 0 : d / totalData[did]
    )
  };
});
const color = ['#8da0cb', '#fc8d62', '#66c2a5'];
const elements = [];
for (let j = 1, jlen = rawData[0].length; j < jlen; ++j) {
  const leftX = grid.left + categoryWidth * j - barPadding;
  const rightX = leftX + barPadding * 2;
  let leftY = grid.top + gridHeight;
  let rightY = leftY;
  for (let i = 0, len = series.length; i < len; ++i) {
    const points = [];
    const leftBarHeight = (rawData[i][j - 1] / totalData[j - 1]) * gridHeight;
    points.push([leftX, leftY]);
    points.push([leftX, leftY - leftBarHeight]);
    const rightBarHeight = (rawData[i][j] / totalData[j]) * gridHeight;
    points.push([rightX, rightY - rightBarHeight]);
    points.push([rightX, rightY]);
    points.push([leftX, leftY]);
    leftY -= leftBarHeight;
    rightY -= rightBarHeight;
    elements.push({
      type: 'polygon',
      shape: {
        points
      },
      style: {
        fill: color[i],
        opacity: 0.25
      }
    });
  }
}
option = {
  legend: {
    selectedMode: false
  },
  grid,
  yAxis: {
    type: 'value'
  },
  xAxis: {
    type: 'category',
    data: ['Germany', 'Spain', 'France', 'Italy', 'Portugal']
  },
  series,
  graphic: {
    elements
  }
};