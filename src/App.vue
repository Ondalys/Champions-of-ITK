<template>
  <div id="app">
    <MainMenu @startGame="startGame"/>
    <EventWindow eventText="You and your friends find a mysterious potion, the liquid is light green and slightly glowing, what do you do?" v-bind:visibility="eventVisibility"/>
  </div>
</template>

<script>
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
