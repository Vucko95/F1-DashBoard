<script setup>
import { RouterLink, RouterView } from 'vue-router'
import LeftSidebar from '@/components/LeftSidebar.vue'
import articles from '@/components/articles.vue'
import ListDriverStandings from '@/components/driver/ListDriverStandings.vue'
import ListConstructorsStandings from '@/components/driver/ListConstructorsStandings.vue'
import SelectYear from '@/components/driver/SelectYear.vue'
import ListDriversByYear from '@/components/circuits/ListDriversByYear.vue'
import DriverPositionsPerCircuit from '@/components/circuits/DriverPositionsPerCircuit.vue'

</script>

<template>
  <div class="app-container">
    <LeftSidebar />
    <SelectYear />
    <div class="main-content">
      <articles />
      
      <ListDriversByYear />
      <ListDriverStandings />
      <ListConstructorsStandings />
      <DriverPositionsPerCircuit />

      <RouterView />
    </div>
  </div>
</template>

<style>
.app-container {
  display: flex;
}

.main-content {
  /* flex-grow: 1; */
   display: flex;
  width: 100%;
  /* padding: 20px; */
}
</style>