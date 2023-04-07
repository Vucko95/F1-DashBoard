<template>
    <!-- <div v-if="show" class="displayYearBox" id="style-1"> -->
    <div  class="displayCircuitsByYear" id="style-1">
        <!-- <h1 > Year</h1> -->
        <!-- <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select> -->
        <!-- <ul v-for="circuit in circuitsList" :key="circuit.circuitId">
            <li> 
                {{ circuit.circuitName }}
                {{ circuit.country }}
            </li>
        </ul> -->
        <table>
            <thead>
                <tr>
                <th>Circuit ID</th>
                <th>Circuit Name</th>
                <th>Country</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="circuit in circuitsList" :key="circuit.circuitId">
                <td>{{ circuit.circuitId }}</td>
                <td>{{ circuit.raceName }}</td>
                <td>{{ circuit.country }}</td>
                <td>{{ circuit.position }}</td>
                <td>    <img :src="'https://flagsapi.com/' + circuit.countryCode + '/flat/64.png'">

</td>
                <td>{{ circuit.countryCode }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    
    </template>
    <style>
        .displayCircuitsByYear {
            margin: 5%;
         
    /* margin-top: 12.5%; */
            box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
            border: 1px solid rgba(0, 0, 0, 0.514);
            transition: all 0.3s ease;
            border-radius: 10px;
            background: rgba(7, 1, 1, 0.589);
            padding: 20px;
            width: 30%;
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

  
    </style>
    
    <script>
    import countryCodes from './countryCodes.js';

import { EventBus } from '@/eventBus.js';
    export default {
      name: 'SelectYear',

      created() {
            console.log(countryCodes.Bahrain)
        // EventBus.$on('sendDriverId', (driverID, selectedYear) => {
        EventBus.$on('sendDriverId', ({ driverID, selectedYear }) => {

        // console.log('Data Received');
        console.log(driverID);
        console.log(selectedYear);
        this.getDriverCircuitResultsByYear(driverID, selectedYear);
});
    //   EventBus.$on("toggle-select-year", () => {
    //     this.show = !this.show;
    //     EventBus.$emit("select-year-toggled", this.show);
    //   });
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
    // const year = event.target.value;
        // const year = 2023
        // console.log('Right side')
        //     console.log(selectedYear)
        //     console.log(driverID)
        //     console.log(driverID)
        //     console.log(driverID)

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

            console.log('BEFORE')
            console.log(this.circuitsList)
            this.circuitsList = data.map(circuit => ({
            ...circuit,
            countryCode: this.countryCodes[circuit.country],
            }));
            console.log('after')

            console.log(this.circuitsList);
            
  
        })
        .catch(error => console.error(error));


    }
        }
        };


    
    </script>
    
