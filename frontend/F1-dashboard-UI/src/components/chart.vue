<template>
    <div>
        <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select>
        
        <canvas id="bar-chart" width="1500" height="1050"></canvas>
    </div>
</template>
<style></style>
<script>
  import { Chart } from 'chart.js/auto';
  export default {
    data() {
      return {
        drivers: [],
        chartInstance: null,
        race_labels: [],
        
      };
    },
    // mounted() {
    //   this.fetchDrivers().then(() => {
    //     this.createChart(this.drivers);
    //   });
    // },
    methods: {
        handleYearChange(event){
            const year = event.target.value;
            const startTime = performance.now();



            fetch('http://localhost:8888/driver_points', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({ "year": year })
            })
              .then(response => response.json())
              .then(data => {
                this.drivers = data.drivers;
                this.race_labels = data.race_labels;
                this.createChart(this.drivers);

                const endTime = performance.now();
                const elapsedTime = endTime - startTime;
                console.log(`Request time: ${elapsedTime} ms`);
          
              })
              .catch(error => console.error(error));



        },
    //   fetchDrivers() {
    //     return fetch('http://localhost:8888/driver_points', {
    //       method: 'GET',
    //       headers: {
    //         'Content-Type': 'application/json',
    //       },
    //     })
    //       .then(response => response.json())
    //       .then(data => {
    //         this.drivers = data.drivers;
    //         this.race_labels = data.race_labels;

    //       })
    //       .catch(error => console.error(error));
    //   },
      createChart(drivers) {
        if (this.chartInstance) {
          this.chartInstance.destroy();
        }
        const colors = ['#3e95cd', '#8e5ea2', '#3cba9f', '#e8c3b9', '#c45850'];
        const ctx = document.getElementById('bar-chart').getContext('2d');
        this.chartInstance  = new Chart(ctx, {
          type: 'line',
          data: {
            // labels: ['Season Start', 'Race 1', 'Race 2', 'Race 3', 'Race 4', 'Race 5'],
            labels: this.race_labels,

            datasets: drivers.map((driver, index) => ({
              label: driver.driver_name,
              borderColor: colors[index % colors.length],
              fill: false,
              data: Object.values(driver.race_points),
            })),
          },
          options: {
            legend: { display: true },
            title: {
              display: true,
              text: 'Formula 1 Drivers Points',
            },
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      },
    },
  };
</script>