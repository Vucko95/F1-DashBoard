<template>
<div v-if="show" class="driversMainBox" id="style-1">
    <!-- <h1>Drivers</h1> -->

    <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select>
        <div v-if="loading">
      <div class="lds-dual-ring"></div>
    </div>
    <table v-if="!loading" class="table-container">
      <thead>
        <!-- <th>Driver ID</th> -->
        <th> </th>
        <th> </th>
        <th></th>
        <!-- <th>Car Number</th> -->
      </thead>
      <tbody>
        <tr v-for="driver in drivers" :key="driver.driverId">
          <!-- <td>{{ driver.driverId }}</td> -->
          <td>          <img :src="'/drivers/' + driver.driverId + '.avif'" class="dirver-icon"/>
</td>
          <td>{{ driver.givenName }}</td>
          
          <td>{{ driver.familyName }}</td>
          <!-- <td>{{ driver.permanentNumber }}</td> -->
          <td><button class="driver-button" v-on:click="sendDriverIdPlusYear(driver.driverId, selectedYear)" >INFO</button></td>
        </tr>
      </tbody>
    </table>
    
</div>

</template>
<style>
.driversMainBox {
    margin: 5%;
    /* margin-top: 12.5%; */
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 20px 20px 0px 20px;
    min-width: 25%;
    /* min-height: 50%; */
    /* max-height: 10%; */
    height: 800px;
    overflow-y: auto;
   
    display: flex;
    flex-direction: column;
    align-items: center;    
}

.driversMainBox h1 {
  padding: 0;
  margin: 0;
}
.driversMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

}
.driversMainBox  {
    font-size: 20px;
    color: aliceblue;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
    /* color: white; */
}
.driversMainBox select {
  margin-bottom: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 100%;
}
.driversMainBox table {
    text-align: center;
    
}
.driversMainBox table th, td {
    padding-left: 15px;
}

.table-container {
    max-height: 300px; 
    overflow-y: auto;
    width: 100%;
}

.dirver-icon {
  width: 60px;
  border-radius: 30%;
  background: rgba(255, 255, 255, 0.26) ;
  /* padding-left: 10px; */
}

.driver-button {
  border: 2px solid white;
  color: white;
  background-color: black;
  padding: 5px 10px 5px 10px;
  border-radius: 10%;
  transition: transform 0.5s ease;


}
.driver-button:hover {
  transform: scale(1.3);
}
</style>

<script>
import { EventBus } from '@/eventBus.js';
// toggle-Circuit-Components
export default {
  name: 'ListDrivers',
  created() {
    EventBus.$on("toggle-Circuit-Components", () => {
        this.show = !this.show;
        // EventBus.$emit("select-year-toggled", this.show);
      });
  this.fetchDrivers(2023);
  // EventBus.$on('fetchConstructorStandignsStarted', () => {
  //     this.loading = true;
  //   });

  //   EventBus.$on('fetchConstructorStandignsFinished', () => {
  //     this.loading = false;
  //   });
  

  EventBus.$on('yearSelected', data => {
    this.drivers = data;
  });
},
  methods: {
    handleYearChange(event) {
  this.selectedYear = event.target.value;
  // console.log('selected')
  // console.log(this.selectedYear)
  this.fetchDrivers(this.selectedYear);
},



  fetchDrivers(selectedYear) {
    this.loading = true;
    fetch('http://localhost:8888/year', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "year": selectedYear })
    })
      .then(response => response.json())
      .then(data => {
        this.drivers = data;
        this.loading = false;
        // console.log(data)
      })
      .catch(error => console.error(error));
  },
  sendDriverIdPlusYear(driverID,selectedYear) {
    // console.log('SENDING >>>')
    // console.log(selectedYear)

    // EventBus.$emit('sendDriverId', driverID, Number(selectedYear));
    EventBus.$emit('sendDriverId', { driverID, selectedYear });

    // console.log(yoyo)
    // console.log(yoyo)
  }
},
  data() {
    return {
      drivers: [],
      selectedYear: '2023',
      show: false,
      loading: true,
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


  
};
</script>