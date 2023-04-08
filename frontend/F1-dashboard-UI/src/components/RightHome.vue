<template>
    <div class="mainDashboardBox">

        <div class="homeBox">
            
            <img src="/f1MovingLogo.gif" alt="logo"  />
            <h1>Dashboard</h1>
            
        </div>
        <div class="twoBoxes">
           <div class="singleBox">
            <h1>Until Next Race</h1>
            <h2>Next Race at </h2>
           </div>
           <div class="singleBox">
            <p>yo</p>
           </div>
        </div>
    </div>
  </template>
  
<script>
import { EventBus } from "@/eventBus.js";



  export default {

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

