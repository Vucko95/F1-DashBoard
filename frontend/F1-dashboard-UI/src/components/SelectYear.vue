<template>
    <div class="displayYearBox" id="style-1">
        <!-- <h1 > Year</h1> -->
        <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select>
        
       
    </div>
    
    </template>
    <style>
        .displayYearBox {
            position: absolute;
            left: 35%;
            top: 2.5%;
            box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
            border: 1px solid rgba(0, 0, 0, 0.514);
            transition: all 0.3s ease;
            border-radius: 10px;
            background: rgba(7, 1, 1, 0.589);
            padding: 20px;
            width: 30%;
            max-height: 50%;
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
import { EventBus } from '@/eventBus.js';
    export default {
      name: 'SelectYear',
      methods: {


        handleYearChange(event) {
  const year = event.target.value;
            


  // Fetch driver standings for year
  EventBus.$emit('fetchDriverStandignsStarted');

  fetch('http://localhost:8888/year/driverstandings', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "year": year })
  })
    .then(response => response.json())
    .then(data => {
      EventBus.$emit('fetchDriverStandings', data);
      EventBus.$emit('fetchDriverStandignsFinished');

    })
    .catch(error => console.error(error));

  // Fetch constructor standings for year
  EventBus.$emit('fetchConstructorStandignsStarted');

  fetch('http://localhost:8888/year/constructorstandings', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "year": year })
  })
    .then(response => response.json())
    .then(data => {
      EventBus.$emit('fetchConstructorsStandings', data);
      EventBus.$emit('fetchConstructorStandignsFinished');

    })
    .catch(error => console.error(error));
}
      }
    };
    </script>
    
