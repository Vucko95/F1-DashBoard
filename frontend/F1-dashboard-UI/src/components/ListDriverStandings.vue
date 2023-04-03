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
        <tr v-for="driver in driverStandings" :key="driver.driverId">
          <!-- <td>{{ driver.driverId }}</td> -->
          <td>{{ driver.givenName }}</td>
          <td>{{ driver.familyName }}</td>
          <td>

          </td>
          <img :src="'/teamlogos/' + driver.constructor_id + '.webp'" class="team-logo"/>
          <td>
            {{ driver.constructor }}</td>
            
            <!-- <td>{{ driver.constructor_id }}</td> -->
            <td>{{ driver.points }}</td>
        </tr>
      </tbody>
    </table>
    
</div>

</template>
<style>
.driversStandingsMainBox {
    margin: 5%;
    margin-top: 12.5%;
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 10px;
    max-height: 50%;
    overflow: auto;
    width: 35%;
    display: flex;
    flex-direction: column;
    align-items: center;



    
}
.driversStandingsMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

}
.driversStandingsMainBox  {
    font-size: 20px;
    color: aliceblue;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
    /* color: white; */
}

.driversStandingsMainBox table {
    text-align: center;
    
}
.driversStandingsMainBox table th, td {
    padding-left: 35px;
}


#style-1::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgb(0, 0, 0);
	border-radius: 15px;
	background-color: #000000;
}

#style-1::-webkit-scrollbar
{
    border-radius: 15px;

	width: 12px;
	background-color: #030202;
}

#style-1::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color:rgba(74, 80, 80, 0.411);
}
</style>

<script>
import { EventBus } from '@/eventBus.js';

export default {
  name: 'ListDriverStandings',
  methods: {
  fetchDriverstandings(year) {

    fetch('http://localhost:8888/year/driverstandings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "year": year })
    })
      .then(response => response.json())
      .then(data => {
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
  EventBus.$on("toggle-select-year", () => {
        this.show = !this.show;
        EventBus.$emit("select-year-toggled", this.show);
      });


    this.fetchDriverstandings(2023);

    

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