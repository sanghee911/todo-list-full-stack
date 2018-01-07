<template>
  <div>
    <app-dashboard></app-dashboard>
  </div>
</template>

<script>
  import Dashboard from './components/Dashboard'

  export default {
    components: {
      'app-dashboard': Dashboard,
    },
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
