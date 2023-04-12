<template>
    <div class="mainDashboardBox">

        <div class="homeBox">


            
            <img src="/f1MovingLogo.gif" alt="logo"  />
            <h1>Dashboard</h1>
        </div>
        <div class="twoBoxes">

           <div class="singleBox" >
            <h2>Comming soon</h2>  
            <!-- <h2>Next Race at </h2> -->
            <h3>{{ timeLeft }}</h3>
        <!-- <h3>Next Race at {{ nextRace.raceName }}</h3> -->
           </div>


           <div class="singleBox" >
            <!-- <h1>Until Next Race</h1> -->
            
            <!-- <h2>Next Race at </h2> -->
            <!-- <h2>{{ timeLeft }}</h2> -->
            <img :src="'https://flagsapi.com/' + nextRace.countryCode + '/flat/48.png'">
        <h3> 
          {{ nextRace.country }} {{ nextRace.raceName }}</h3>
        <h3>Round {{ nextRace.round }} / 23 </h3>
        <h3>{{ nextRace.first_practice_date }}  - {{ nextRace.race_date }} </h3>
          <button>Pick Timezone</button>

          <p>Practice 2    FRI  {{ nextRace.startFP1 }}   </p>
          <p>Practice 2    FRI    {{ nextRace.startFP2 }}     </p>
          <p>Qualifing     SAT    {{ nextRace.startQualy }}    </p>
          <p>Sprint        SAT    {{ nextRace.startSprint }}    </p>
          <p>Race          SUN      {{ nextRace.startRace }}    </p>



           </div>




           <div class="singleBox" >
            <!-- <h1>Until Next Race</h1> -->
            
            <h2>Previous Event </h2>
            <!-- <h2>{{ timeLeft }}</h2> -->
            <img :src="'https://flagsapi.com/' + pastRace.countryCode + '/flat/48.png'">
        <h3> 
          {{ pastRace.country }} {{ pastRace.raceName }}</h3>
        <h3>Round {{ pastRace.round }} / 23 </h3>
        <h3> {{ pastRace.race_date }} </h3>

              <h1>TOP DRIVERS </h1>

        <table >
          <thead>
            <th>Driver </th>
            <th>Time</th>
            <th>Points</th>
          </thead>
          <tbody>
            <tr v-for="(driver, index) in topDrivers" :key="index">
              <td> {{ index + 1 }}  {{ driver.driver_name }}  {{ driver.driver_surname }} </td>
              <td>{{ driver.driver_time }}</td>
              <td> {{ driver.driver_points }}</td>
            </tr>
          </tbody>
        </table>

           </div>
        </div>
    </div>
  </template>
  
<script>
import { EventBus } from "@/eventBus.js";
import countryCodes from '../countryCodes.js';



  export default {
    data() {
    return {
      // nextRace: null,
      timeLeft: "",
      nextRace: {
      season: '',
      round: '',
      country: '',
      url: '',
      raceName: '',
      circuitId: '',
      first_practice_date: '',
      race_date: '',
      date: '',
      time: '',
      countryCode: '',
    },
    pastRace : [],
    topDrivers: []

    };
  },
  created() {
    this.fetchNextRace();
    this.fetchPastRace();
    this.fetchTopDrivers();
    // this.timer = setInterval(this.calculateTimeLeft, 1000);

  },
  methods: {
    fetchNextRace() {
      fetch("http://localhost:8888/race/next")
        .then((response) => response.json())
        .then((data) => {
          this.nextRace = data;
          // console.log(this.nextRace)
          this.nextRace = {
        ...data,
        countryCode: countryCodes[data.country] || 'XX',
      };
          this.calculateTimeLeft();
        })
        .catch((error) => console.error(error));
    },

    calculateTimeLeft() {
        const currentDate = new Date();
        const nextRaceDate = new Date(this.nextRace.date);
        const timeDifference = nextRaceDate - currentDate;
        const daysLeft = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
        const hoursLeft = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutesLeft = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
        const secondsLeft = Math.floor((timeDifference % (1000 * 60)) / 1000);

        this.timeLeft = `${daysLeft} days ${hoursLeft} hours ${minutesLeft} minutes ${secondsLeft} seconds`;
    //   console.log(this.timeLeft)
    //   console.log(this.timeLeft)
    },


    fetchPastRace() {
      fetch("http://localhost:8888/race/last")
        .then((response) => response.json())
        .then((data) => {
          this.pastRace = data;
          // console.log(this.pastRace)
          this.pastRace = {
        ...data,
        countryCode: countryCodes[data.country] || 'XX',
      };
        })
        .catch((error) => console.error(error));
    },
    fetchTopDrivers() {
      fetch("http://localhost:8888/topdrivers")
        .then((response) => response.json())
        .then((data) => {
          this.topDrivers = data;

        })
        .catch((error) => console.error(error));
    },
  },



  };
  </script>
  
  <style scoped>

  .mainDashboardBox {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
    .homeBox{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 30%;
        height: 150px;
        margin-left: 30%;
        margin-top: 20px;

    }
    .homeBox img {
        width: 80%;
    }
    .homeBox h1 {
        color: white;
        margin-top: -60px;
        font-weight: bold;
        font-size: 3.5rem;
        font-family:cursive;
        font-style: italic;
        
    }

    .twoBoxes{
        margin-top: 5%;
        margin-left: 5%;
        width: 90%;
        height: 60%;
        /* background: wheat; */
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5%;
    }
    .singleBox {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        /* background-color: aqua; */
        /* color: rgba(179, 199, 216, 0.747); */
        background: rgb(27, 31, 36);

        width: 40%;
        height: 70%;

    }

  </style>

