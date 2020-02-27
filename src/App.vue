<template>
  <div id="app">
    <img alt="ITK logo" src="./assets/logo.png">
    <Header msg="Welcome to Champions of ITK"/>
        <MainMenu @startGame="startGame"/>
    <EventWindow eventText="You and your friends find a mysterious potion, the liquid is light green and slightly glowing, what do you do?" v-bind:visibility="eventVisibility"/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import MainMenu from './components/MainMenu.vue'
import EventWindow from './components/EventWindow.vue'

export default {
    name: 'app',
    data(){
        return {
            eventVisibility: false
        }
    },
    components: {
        Header,
        EventWindow,
        MainMenu
    },
    methods: {
        startGame: function(){
            this.eventVisibility = true;
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
