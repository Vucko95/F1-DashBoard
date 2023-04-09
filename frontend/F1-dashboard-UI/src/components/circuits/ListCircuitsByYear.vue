<template>
    <div  v-if="show"  class="circuitsMainBox" id="style-1">
        <select class="custom-select" name="year" id="year" @change="handleYearChange">
            <option value="2023">2023</option>
            <option value="2022">2022</option>
            <option value="2021">2021</option>
            <option value="2020">2020</option>
            <option value="2019">2019</option>
            <option value="2018">2018</option>
    
        </select>
        <table class="table-container">
            <thead>
                <tr>
                <!-- <th>Circuit ID</th> -->
                <!-- <th>Country</th> -->
                <!-- <th>CN</th> -->
                <th></th>
                <th></th>
                <th></th>
                <th></th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="circuit in circuits" :key="circuit.circuitId">
                    <td>    <img :src="'https://flagsapi.com/' + circuit.countryCode + '/flat/48.png'">
                    </td>
                    <td>{{ circuit.circuitName }}</td>
                <!-- <td>{{ circuit.circuitId }}</td> -->
                <!-- <td>{{ circuit.country }}</td> -->
                <!-- <td class="position">{{ circuit.country }}</td> -->
                <!-- <td class="position">{{ circuit.circuitId }}</td> -->
                <td><button class="driver-button" v-on:click="sendCircuitId(circuit.circuitId, selectedYear)" >INFO</button></td>



                <!-- <td>{{ circuit.countryCode }}</td> -->
                </tr>
            </tbody>
        </table>


    </div>
</template>
<script>
        import countryCodes from '../countryCodes.js';
        import { EventBus } from '@/eventBus.js';

export default {
  name: 'ListConstructorsStandings',
  methods: {
    handleYearChange(event) {
      this.selectedYear = event.target.value;
      this.fetchCircuits(this.selectedYear);
    },
    
    
    
    fetchCircuits(selectedYear) {
      this.loading = true;
      fetch('http://localhost:8888/circuits/year', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "year": selectedYear })
    })
    .then(response => response.json())
    .then(data => {
      this.circuits = data;
      
      this.circuits = data.map(circuit => ({
        ...circuit,
        countryCode: this.countryCodes[circuit.country],
      }));
      //     this.circuits = data.map(circuit => {
        //       const countryCode = this.countryCodes[circuit.country] || 'N/A';
        //       return {
          //         ...circuit,
          //         countryCode: countryCode,
          //       };
          //   });
          this.loading = false;
          // console.log(data)
        })
        .catch(error => console.error(error));
      },
      
      sendCircuitId(circuitId,selectedYear) {
        EventBus.$emit('sendCircuitId', { circuitId, selectedYear });
      },
      
      
    },
    created() {
      EventBus.$on("toggle-Circuits-Components", () => {
        this.show = !this.show;
        // EventBus.$emit("select-year-toggled", this.show);
      });
      this.fetchCircuits(2023);
      
    },
    data(){
      return {
        show: false,
        circuits: [],
        countryCodes,
        selectedYear: '2023',
        
      };
    },
    
    
    
    
  }
  
</script>
<style>
.circuitsMainBox {
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

.circuitsMainBox h1 {
  padding: 0;
  margin: 0;
}
.circuitsMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

}
.circuitsMainBox  {
    font-size: 20px;
    color: aliceblue;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
    /* color: white; */
}
.circuitsMainBox select {
  margin-bottom: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
  width: 100%;
}
.circuitsMainBox table {
    text-align: center;
    
}
.circuitsMainBox table th, td {
    padding-left: 15px;
}

.table-container {
    max-height: 300px; 
    overflow-y: auto;
    width: 100%;
}
</style>