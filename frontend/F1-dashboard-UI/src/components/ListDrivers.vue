<template>
<div class="driversMainBox" id="style-1">
    <h1>Drivers</h1>
    <img src="https://flagsapi.com/AR/flat/64.png">

    <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select>
    <table>
      <thead>
        <!-- <th>Driver ID</th> -->
        <th> Name</th>
        <th>Surname</th>
        <th>Car Number</th>
      </thead>
      <tbody>
        <tr v-for="driver in drivers" :key="driver.driverId">
          <!-- <td>{{ driver.driverId }}</td> -->
          <td>{{ driver.givenName }}</td>
          
          <td>{{ driver.familyName }}</td>
          <td>{{ driver.permanentNumber }}</td>
          <td><button v-on:click="printDriverId(driver.driverId, selectedYear)" >CLICK MEEE</button></td>
        </tr>
      </tbody>
    </table>
    
</div>

</template>
<style>
.driversMainBox {
    margin: 5%;
    margin-top: 12.5%;
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 20px;
    /* max-width: 30%; */
    max-height: 50%;
    overflow: auto;
   
    display: flex;
    flex-direction: column;
    align-items: center;



    
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

.driversMainBox table {
    text-align: center;
    
}
.driversMainBox table th, td {
    padding-left: 15px;
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
  name: 'ListDrivers',
  methods: {
    handleYearChange(event) {
  this.selectedYear = event.target.value;
  // console.log('selected')
  // console.log(this.selectedYear)
  this.fetchDrivers(this.selectedYear);
},



  fetchDrivers(selectedYear) {
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
        // console.log(data)
      })
      .catch(error => console.error(error));
  },
  printDriverId(driverID,selectedYear) {
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
      selectedYear: '2023'
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
  
    this.fetchDrivers(2023);

    

    EventBus.$on('yearSelected', data => {
      this.drivers = data;
    });
  }

  
};
</script>