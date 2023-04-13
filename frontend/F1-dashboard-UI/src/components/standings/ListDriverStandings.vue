<template>
<div v-if="show" class="driversStandingsMainBox" id="style-1">
    <h1>Driver Standings</h1>
    <div v-if="loading">
      <div class="lds-dual-ring"></div>
    </div>
    <table  v-if="!loading">
      <thead>
        <!-- <th>Driver ID</th> -->
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
      </thead>
      <tbody>
        <tr v-for="driver in driverStandings" :key="driver.driver_id">
          <!-- <td>{{ driver.driverId }}</td> -->
          <td>{{ driver.driver_name }}</td>
          <!-- <td>{{ driver.familyName }}</td> -->
          <td>

          </td>
          <img :src="'/teamlogos/' + driver.constructor_id + '.webp'" class="team-logo"/>
          <td>
            {{ driver.constructor }}</td>
            
            <!-- <td>{{ driver.constructor_id }}</td> -->
            <td>{{ driver.total_points }}</td>
        </tr>
      </tbody>
    </table>
    
</div>

</template>
<style>
.driversStandingsMainBox {
    margin: 5%;
    margin-top: 12.5%;
    /* box-shadow: 0 0 3px rgba(78, 248, 234, 0.808); */
    /* border: 1px solid rgba(0, 0, 0, 0.514); */
    transition: all 0.3s ease;
    /* background: rgba(7, 1, 1, 0.589); */
    /* background: rgb(8, 36, 13); */
    
    padding: 20px;
    /* max-height: 50%;overflow: auto; */
    /* width: 35%; */
    display: flex;
    flex-direction: column;
    align-items: center;
    
    background: rgb(27, 31, 36);
    border-radius: 5%;
    /* max-height: calc(100% - 30%); */
    /* overflow: auto; */


    
}
/* .driversStandingsMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

} */
.driversStandingsMainBox  {
    font-size: 20px;
    color: rgba(179, 199, 216, 0.747);
    /* font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif */
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    /* color: white; */
}

.driversStandingsMainBox table, th, td {
    text-align: center;
    
}



</style>

<script>
import { EventBus } from '@/eventBus.js';

export default {
  name: 'ListDriverStandings',
  methods: {
  fetchDriverstandings() {

    fetch('http://localhost:8888/year/driverstandings', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
      // body: JSON.stringify({ "year": year })
    })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        this.driverStandings = data;
        this.loading = false;

        // console.log(data)
      })
      .catch(error => console.error(error));
  }
},
  data() {
    return {
      loading: true,
      show: false,


      driverStandings: []
    };
  },
//   created() {
//     fetch('http://localhost:8888/players')
//       .then(response => response.json())
//       .then(data => {
//         this.drivers = data;
//       })
//       .catch(error => console.error(error));
//   }
created() {
  EventBus.$on("toggle-Standings-Components", () => {
        this.show = !this.show;
        EventBus.$emit("select-year-toggled", this.show);
        this.fetchDriverstandings(2023);
      });



    

    EventBus.$on('fetchDriverStandings', data => {
      this.driverStandings = data;
    });


    EventBus.$on('fetchDriverStandignsStarted', () => {
      this.loading = true;
    });

    EventBus.$on('fetchDriverStandignsFinished', () => {
      this.loading = false;
    });
  }

  

  
};
</script>