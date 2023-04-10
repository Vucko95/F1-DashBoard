<script setup>
import { RouterLink, RouterView } from 'vue-router'
import LeftSidebar from '@/components/LeftSidebar.vue'
import articles from '@/components/articles.vue'
import chart from '@/components/chart.vue'
import RightHome from '@/components/RightHome.vue'
import ListDriverStandings from '@/components/standings/ListDriverStandings.vue'
import ListConstructorsStandings from '@/components/standings/ListConstructorsStandings.vue'
import SelectYear from '@/components/standings/SelectYear.vue'
import ListDriversByYear from '@/components/driver/ListDriversByYear.vue'
import ListCircuitsByYear from '@/components/circuits/ListCircuitsByYear.vue'
import CircuitResults from '@/components/circuits/CircuitResults.vue'
import DriverPositionsPerCircuit from '@/components/driver/DriverPositionsPerCircuit.vue'

</script>

<template>
  <div class="app-container">
    <LeftSidebar />
    <SelectYear />
    <div class="main-content">
      
      <!-- <RightHome /> -->
      <chart />
      <articles />
      <ListDriversByYear />
      <ListDriverStandings />
      <ListConstructorsStandings />
      <DriverPositionsPerCircuit />
      <ListCircuitsByYear />
      <CircuitResults />

      <RouterView />
    </div>
  </div>
</template>

<style>
.app-container {
  display: flex;
}

.main-content {
  background: rgb(15, 18, 20);
  
  /* flex-grow: 1; */
   display: flex;
  width: 100%;
  /* padding: 20px; */
}
</style>