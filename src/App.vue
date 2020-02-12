<template>
  <div id="app">
    <img alt="ITK logo" src="./assets/logo.png">
    <Welcome msg="Welcome to Champions of ITK"/>
    <MainMenu startBtn="Start playing"/>
  </div>
</template>

<script>
import Welcome from './components/HelloWorld.vue'
import MainMenu from './components/MainMenu.vue'

export default {
  name: 'app',
  components: {
    Welcome,
    MainMenu
  }
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
  font-size: 50px;
}
</style>
