<template>
<div class="constructorStandingsMainBox" id="style-1">
    <h1>Constructors Standings</h1>
    <table>
      <thead>
        <!-- <th>Driver ID</th> -->
        <th> Name</th>
        <th>Surname</th>
        <th>Total Points</th>
        <!-- <th>Team</th> -->
      </thead>
      <tbody>
        <tr v-for="team in constructorStandings" :key="team.constructorId">
          <!-- <td>{{ driver.driverId }}</td> -->
          <td>{{ team.position }}</td>
          <td>{{ team.name }}</td>
          <td>{{ team.points }}</td>
          <!-- <td>{{ driver.constructor }}</td> -->
        </tr>
      </tbody>
    </table>
    
</div>

</template>
<style>
.constructorStandingsMainBox {
    margin: 5%;
    margin-top: 12.5%;
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 20px;
    max-height: 50%;
    overflow: auto;
    width: 35%;
    display: flex;
    flex-direction: column;
    align-items: center;



    
}
.constructorStandingsMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

}
.constructorStandingsMainBox  {
    font-size: 20px;
    color: aliceblue;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
    /* color: white; */
}

.constructorStandingsMainBox table {
    text-align: center;
    
}
.constructorStandingsMainBox table th, td {
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
  name: 'ListConstructorsStandings',
  methods: {
  fetchConstructorstandings(year) {
    console.log(year)
    console.log(year)
    fetch('http://localhost:8888/year/constructorstandings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "year": year })
    })
      .then(response => response.json())
      .then(data => {
        this.constructorStandings = data;
        console.log(data)
      })
      .catch(error => console.error(error));
  }
},
  data() {
    return {
      constructorStandings: []
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
    this.fetchConstructorstandings(2023);

    

    EventBus.$on('yearSelectedConstructorsStandings', data => {
      this.constructorStandings = data;
    });
  }

  
};
</script>