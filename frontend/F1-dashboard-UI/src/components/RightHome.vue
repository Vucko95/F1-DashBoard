<template>
    <div class="mainDashboardBox">

        <div class="homeBox">
            
            <img src="/f1MovingLogo.gif" alt="logo"  />
            <h1>Dashboard</h1>
            
        </div>
        <div class="twoBoxes" v-if="nextRace">
           <div class="singleBox" >
            <h1>Until Next Race</h1>
            <h2>Next Race at </h2>
            <h2>{{ timeLeft }}</h2>
        <h3>Next Race at {{ nextRace.raceName }}</h3>
           </div>
           <div class="singleBox">
            <p>Calendar</p>
           </div>
        </div>
    </div>
  </template>
  
<script>
import { EventBus } from "@/eventBus.js";



  export default {
    data() {
    return {
      nextRace: null,
      timeLeft: "",
    };
  },
  created() {
    this.fetchNextRace();
    // this.timer = setInterval(this.calculateTimeLeft, 1000);

  },
  methods: {
    fetchNextRace() {
      fetch("http://localhost:8888/next_race")
        .then((response) => response.json())
        .then((data) => {
          this.nextRace = data;
          console.log(this.nextRace)
          console.log(this.nextRace.date)
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

        this.timeLeft = `${daysLeft} days ${hoursLeft} hours ${minutesLeft} minutes ${secondsLeft} seconds left till next race`;
    //   console.log(this.timeLeft)
    //   console.log(this.timeLeft)
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
        width: 100%;
        height: 60%;
        background: wheat;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10%;
    }
    .singleBox {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        background-color: aqua;
        width: 40%;
        height: 70%;

    }
  </style>

