const xValues = [2018,2019,2020,2021,2022];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
        label: "Fatality",
      data: [157593,158984,138383,153972,168491],
      borderColor: "red",
      fill: false
    },{
        label: "Accident",
      data: [470403,456959,372181,412432,461312],
      borderColor: "black",
      fill: false
    },{
        label: "People Injured",
      data: [464715,449360,346747,384448,443366],
      borderColor: "blue",
      fill: false
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: false },
      tooltip: { backgroundColor: '#ffffff' } ,
      chartArea: {
        backgroundColor: 'lightblue' // Change the chart area background color
      }
    }
  }
  });
