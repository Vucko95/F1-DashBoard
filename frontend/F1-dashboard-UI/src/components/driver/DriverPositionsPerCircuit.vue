<template>
  <div  v-if="show" class="displayCircuitsByYear" id="style-1">
    <!-- <canvas id="myChart"></canvas> -->
    <canvas id="bar-chart" width="2800" height="4250"></canvas>

<!-- CHART HERE -->


        <table>
            <thead>
                <tr>
                <!-- <th>Circuit ID</th> -->
                <!-- <th>Country</th> -->
                <th>CN</th>
                <th>Circuit Name</th>
                <th>Position</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="circuit in circuitsList" :key="circuit.circuitId">
                    <td>    <img :src="'https://flagsapi.com/' + circuit.countryCode + '/flat/48.png'">
                    </td>
                    <td>{{ circuit.raceName }}</td>
                <!-- <td>{{ circuit.circuitId }}</td> -->
                <!-- <td>{{ circuit.country }}</td> -->
                <td class="position">{{ circuit.position }}</td>


                <!-- <td>{{ circuit.countryCode }}</td> -->
                </tr>
            </tbody>
        </table>
    </div>
    
    </template>
    <style>
        .displayCircuitsByYear {
            margin: 5%;
        
            box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
            border: 1px solid rgba(0, 0, 0, 0.514);
            transition: all 0.3s ease;
            border-radius: 10px;
            background: rgba(7, 1, 1, 0.589);
            padding: 40px;
            /* width: 30%; */
            /* max-height: 30%; */
            max-height: 700px;
            overflow: auto;

            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 20px;
            color: aliceblue;
            font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
            z-index: 9999; 

        }
        .custom-select {
            background-color: black;
            color: white;
            border-radius: 10px;
            width: 100%;
            text-align: center;
            padding: 5px;
            font-size: 20px;
        }
        .position {
            font-weight: 700;
        }
  
    </style>
    
    <script>
    import countryCodes from '../countryCodes.js';
    import { Chart  } from 'chart.js/auto';
    import { EventBus } from '@/eventBus.js';
    export default {
      name: 'SelectYear',

      created() {
        EventBus.$on("toggle-Drivers-Components", () => {
    this.show = !this.show;
    console.log("show:", this.show);
    if (this.show) {
      this.$nextTick(() => {
        console.log("Creating chart");
        this.createChart();
      });
    }
  });

        EventBus.$on('sendDriverId', ({ driverID, selectedYear }) => {
          console.log("sendDriverId event received");

        this.getDriverCircuitResultsByYear(driverID, selectedYear);
});

// this.createChart();









    },

    data() {
    return {
      show: false,
      circuitsList: [],
      countryCodes
    };
  },



      methods: {
        getDriverCircuitResultsByYear(driverID,selectedYear) {


    fetch('http://localhost:8888/circuits/driver', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "year": selectedYear, "driverID" : driverID })
    })
        .then(response => response.json())
        .then(data => {
            this.circuitsList = data;
            console.log('THIS ONE')
            // console.log('BEFORE')
            console.log(this.circuitsList)
            this.circuitsList = data.map(circuit => ({
            ...circuit,
            countryCode: this.countryCodes[circuit.country],
            }));
            console.log('after')

            console.log(this.circuitsList);
            
  
        })
        .catch(error => console.error(error));


    },
    createChart() {






    const ctx = document.getElementById('bar-chart').getContext('2d');
    const chart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
      datasets: [
        {
          label: "Population (millions)",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [2478,5267,734,784,433]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      }
    }
});
  },




        }
        };


    
    </script>
    
