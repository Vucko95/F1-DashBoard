<script setup>
import { RouterLink, RouterView } from 'vue-router'
import LeftSidebar from '@/components/LeftSidebar.vue'
import ListDrivers from '@/components/ListDrivers.vue'
import ListDriverStandings from '@/components/ListDriverStandings.vue'
import ListConstructorsStandings from '@/components/ListConstructorsStandings.vue'
import SelectYear from '@/components/SelectYear.vue'

</script>

<template>
  <div class="app-container">
    <LeftSidebar />
    <SelectYear />
    <div class="main-content">
      <!-- <ListDrivers /> -->
      <ListDriverStandings />
      <ListConstructorsStandings />
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