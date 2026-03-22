const getOptionChart1 = (myChart) => {
  // 1. Datos originales (puedes cambiarlos por los tuyos)
  const rawData = [
    [3384248,1260348,2337638,1712042,239428],
    [980318,363199,2337638,502407,64461],
    [1807398,617132,994800,1727701,133853]
  ];

  // 2. Cálculos de totales para porcentajes
  const totalData = [];
  for (let i = 0; i < rawData[0].length; ++i) {
    let sum = 0;
    for (let j = 0; j < rawData.length; ++j) {
      sum += rawData[j][i];
    }
    totalData.push(sum);
  }

  // 3. Configuración del Grid y Dimensiones
  const grid = { left: 100, right: 100, top: 50, bottom: 50 };
  
  // IMPORTANTE: Usamos la instancia myChart pasada por parámetro
  const gridWidth = myChart.getWidth() - grid.left - grid.right;
  const gridHeight = myChart.getHeight() - grid.top - grid.bottom;
  const categoryWidth = gridWidth / rawData[0].length;
  const barWidth = categoryWidth * 0.6;
  const barPadding = (categoryWidth - barWidth) / 2;

  // 4. Preparación de las Series (Barras)
  const series = ['Consumption','Capital formation','Exports'].map((name, sid) => {
    return {
      name,
      type: 'bar',
      stack: 'total',
      barWidth: '60%',
      label: {
        show: true,
        formatter: (params) => Math.round(params.value * 100) + '%'
      },
      data: rawData[sid].map((d, did) => totalData[did] <= 0 ? 0 : d / totalData[did])
    };
  });

  // 5. Generación de Polígonos (Sombras de conexión)
  const color = ['#8da0cb', '#fc8d62', '#66c2a5'];
  const elements = [];
  for (let j = 1; j < rawData[0].length; ++j) {
    const leftX = grid.left + categoryWidth * j - barPadding;
    const rightX = leftX + barPadding * 2;
    let leftY = grid.top + gridHeight;
    let rightY = leftY;

    for (let i = 0; i < series.length; ++i) {
      const leftBarHeight = (rawData[i][j - 1] / totalData[j - 1]) * gridHeight;
      const rightBarHeight = (rawData[i][j] / totalData[j]) * gridHeight;
      const points = [
        [leftX, leftY],
        [leftX, leftY - leftBarHeight],
        [rightX, rightY - rightBarHeight],
        [rightX, rightY],
        [leftX, leftY]
      ];
      leftY -= leftBarHeight;
      rightY -= rightBarHeight;
      elements.push({
        type: 'polygon',
        shape: { points },
        style: { fill: color[i], opacity: 0.25 }
      });
    }
  }

  // 6. Retorno del objeto final
  return {
    legend: {
        show: true, 
        selectedMode: false,
        orient: 'vertical',
        right: '10',
        top: 'center',
        borderWidth: 1,       
        borderColor: '#0e0e0e',  
        padding: 10,          
        backgroundColor: 'rgba(255,255,255,0.8)'
     },
    grid:{
        left: 80, 
        right: 160,
        top: 50,
        bottom: 50 
    },
    yAxis: { type: 'value' },
    xAxis: {
      type: 'category',
      data: ['Germany', 'Spain', 'France', 'Italy', 'Portugal']
    },
    series,
    graphic: { elements }
  };
};

const getOptionChart2=()=>{
    return {
        title: {
            text: 'Stacked Line'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
            saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            name: 'Email',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
            },
            {
            name: 'Union Ads',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310]
            },
            {
            name: 'Video Ads',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410]
            },
            {
            name: 'Direct',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320]
            },
            {
            name: 'Search Engine',
            type: 'line',
            stack: 'Total',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
            }
        ]
        };
};

const initCharts = () => {
    // 1. Inicializamos las instancias
    const chart1 = echarts.init(document.getElementById("chart1"));
    const chart2 = echarts.init(document.getElementById("chart2"));

    // 2. Definimos la función de actualización para que sea responsiva
    const renderCharts = () => {
        // Pasamos 'chart1' como parámetro para que calcule bien los anchos
        chart1.setOption(getOptionChart1(chart1), true); 
        chart2.setOption(getOptionChart2());
        
        chart1.resize();
        chart2.resize();
    };

    // 3. Ejecutamos la primera vez
    renderCharts();

    // 4. Hacemos que sea responsivo
    window.addEventListener('resize', renderCharts);
};

window.addEventListener('load', () => {
    initCharts();
});