const getOptionChart1 = () => {
return {
    
    title: {
      text: 'Cumplimiento objetivo de Inflación anual - Argentina 2026',
      subtext: 'Valor aprobado en Ley de Presupuesto',
      left: '2%',
      top: '4%', 
      textStyle: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#333'
      },
      subtextStyle: {
        fontSize: 16,
        color: '#666'
      }
    },
  series: [
    {
      type: 'gauge',
      startAngle: 180,
      endAngle: 0,
      center: ['50%', '85%'],
      radius: '90%',
      min: 0,
      max: 0.101,
      splitNumber: 8,
      axisLine: {
        lineStyle: {
          width: 6,
          color: [
            [0.25, '#7CFFB2'],
            [0.5, '#FDDD60'],
            [0.75, '#FD9803'],
            [1, '#FF434C']
          ]
        }
      },
      pointer: {
        icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
        length: '12%',
        width: 20,
        offsetCenter: [0, '-60%'],
        itemStyle: {
          color: 'auto'
        }
      },
      axisTick: {
        length: 12,
        lineStyle: {
          color: 'auto',
          width: 2
        }
      },
      splitLine: {
        length: 20,
        lineStyle: {
          color: 'auto',
          width: 5
        }
      },
        axisLabel: {
          distance: -60, 
          rotate: function (value) {
            return value === 0.101 ? 0 : 'tangential'; 
          },
          formatter: function (value) {
            if (value === 0.101) return '{rojo|Objetivo: 10.1%}';
            
           
            if (value === 0.088375) return '{estiloIncumplido|Incumplido}'; 
            if (value === 0.063125) return '{estiloExcedido|Excedido}';
            if (value === 0.037875) return 'Desviado';
            if (value === 0.012625) return '{estiloControlado|Controlado}';
            return '';
          },
          rich: {
            rojo: {
              color: '#FF434C',
              fontSize: 16,
              fontWeight: 'bold',
              padding: [0, -10, -40, 0] 
            },
            estiloIncumplido: {
              fontSize: 12,
              color: '#464646',
              padding: [0, -50, 0, 0] 
            },
            estiloControlado: {
              fontSize: 12,
              color: '#464646',
              padding: [0, 0, 0, -50]
            },
            estiloExcedido: {
              fontSize: 18,
              color: '#FD9803',
              fontWeight: 'bold',
              padding: [0, 0, 0, 20]
            }
          }
        },
      title: {
        offsetCenter: [0, '-10%'],
        fontSize: 20
      },
      detail: {
        fontSize: 30,
        offsetCenter: [0, '-35%'],
        valueAnimation: true,
        formatter: function (value) {
          return (value * 100).toFixed(2)+ '%';
        },
        color: 'inherit'
      },
      data: [
        {
          value: 0.0588,
          name: 'Inflación acumulada'
        },
        {
        value: 0.0588,
        name: '(Febrero 2026)', 
        
        title: { offsetCenter: [0, '5%'], fontSize: 12 }
      }
      ]
    }
  ]
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
    const chartDom1 = document.getElementById("chart1");
    const chartDom2 = document.getElementById("chart2");

    // Verificación de seguridad para evitar el error de 'null'
    if (chartDom1) {
        const chart1 = echarts.init(chartDom1);
        chart1.setOption(getOptionChart1());
        
        // Hacer que chart1 sea responsivo
        window.addEventListener('resize', () => chart1.resize());
    }

    if (chartDom2) {
        const chart2 = echarts.init(chartDom2);
        chart2.setOption(getOptionChart2());
        
        // Hacer que chart2 sea responsivo
        window.addEventListener('resize', () => chart2.resize());
    }
};

window.addEventListener('load', initCharts);