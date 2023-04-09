<template>
    <div  v-if="show" class="circuitResultsMainBox" id="style-1">
        <h1>CIRCUIT RESULTS</h1>
        <table>
            <thead>
                <tr>
                    <th>Driver Name</th>
                    <th>Position</th>
                    <th>Points</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="result in circuitsResultsList" :key="result.driverName + '-' + result.position">
                    <td>{{ result.driverName }}</td>
                    <td>{{ result.position }}</td>
                    <td>{{ result.points }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    
</template>


<script>
        import countryCodes from '../countryCodes.js';
        import { EventBus } from '@/eventBus.js';

export default {
    name: 'CircuitResults',
    methods: {

        
        
        getCircuitsResults(circuitId,selectedYear) {
            fetch('http://localhost:8888/circuits/track/result', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ "year": selectedYear, "circuitId" : circuitId })
            })
            .then(response => response.json())
            .then(data => {
                this.circuitsResultsList = data;
                
                
                
                console.log(this.circuitsResultsList);
                
                
            })
            .catch(error => console.error(error));
        },
        
        
    },
    created() {
        EventBus.$on("toggle-Circuits-Components", () => {
        this.show = !this.show;
        // EventBus.$emit("select-year-toggled", this.show);
      });





        EventBus.$on('sendCircuitId', ({ circuitId, selectedYear }) => {
            // this.getDriverCircuitResultsByYear(circuitId, selectedYear);
            console.log('RECIVER')
            this.getCircuitsResults(circuitId, selectedYear);
            console.log(circuitId, selectedYear)
            console.log(circuitId, selectedYear)
        });
    },
    data(){
        return {
            show: false,
            circuits: [],
            countryCodes,
            circuitsResultsList : [],
        };
    },
    
    
    
    
}

</script>

<style>
.circuitResultsMainBox {
    margin: 5%;
    /* margin-top: 12.5%; */
    box-shadow: 0 0 3px rgba(78, 248, 234, 0.808);
    border: 1px solid rgba(0, 0, 0, 0.514);
    transition: all 0.3s ease;
    border-radius: 10px;
    background: rgba(7, 1, 1, 0.589);
    padding: 10px;
    max-height: 50%;
    overflow: auto;
    /* width: 35%; */
    display: flex;
    flex-direction: column;
    align-items: center;



    
}
.circuitResultsMainBox:hover {
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.562);
    border: 1px solid rgba(255, 0, 0, 0.726);
    

}
.circuitResultsMainBox  {
    font-size: 20px;
    color: aliceblue;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
    /* color: white; */
}

.circuitResultsMainBox table {
    text-align: center;
    
}
.circuitResultsMainBox table th, td {
    padding-left: 35px;
}

</style>