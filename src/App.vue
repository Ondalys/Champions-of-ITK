<template>
  <div id="app">
    <img alt="ITK logo" src="./assets/logo.png">
    <Header msg="Welcome to Champions of ITK"/>
    <EventText eventText=""/>
    <MainMenu startBtn="Start playing"/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import MainMenu from './components/MainMenu.vue'
import EventText from './components/EventText.vue'

export default {
    name: 'app',
    components: {
        Header,
        EventText,
        MainMenu
    },
    methods: {
        startGame: function(){
            // this is when the startbtn is clicked
        },
        roll: function(){
            // this function is for rolling on a table
        }
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
