<template>
    <div>
        <img alt="ITK logo" src="../assets/logo.png">
        <Header msg="Welcome to Champions of ITK"/>
        <v-btn to="select" color="#aa1">Start Game</v-btn>
        <v-btn @click="$emit('rulesToggle')" color="#aa1">Rules</v-btn>
    </div>
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
div {
    background-color: #9ecfff;
}
</style>
