<template>
    <v-app-bar class="menu">
        <img alt="ITK logo" src="../assets/logo.png">
        <v-btn @click="$emit('startGame')" to="select">Start Game</v-btn>
        <Header msg="Welcome to Champions of ITK"/>
    </v-app-bar>
</template>

<script>

import Header from './Header.vue'

export default {
    name: 'MainMenu',
    props: {
    },
    components: {
        Header
    }
}
</script>

<style scoped>
</style>
