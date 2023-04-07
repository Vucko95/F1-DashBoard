<script setup>
import { RouterLink, RouterView } from 'vue-router'
import LeftSidebar from '@/components/LeftSidebar.vue'
import ListDriverStandings from '@/components/driver/ListDriverStandings.vue'
import ListConstructorsStandings from '@/components/driver/ListConstructorsStandings.vue'
import SelectYear from '@/components/driver/SelectYear.vue'
import ListDrivers from '@/components/circuits/ListDrivers.vue'
import ListTracksByYear from '@/components/circuits/ListTracksByYear.vue'

</script>

<template>
  <div class="app-container">
    <LeftSidebar />
    <SelectYear />
    <div class="main-content">
      <ListDrivers />
      <ListDriverStandings />
      <ListConstructorsStandings />
      <ListTracksByYear />

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