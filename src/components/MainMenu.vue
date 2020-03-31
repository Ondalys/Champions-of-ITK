<template>
    <v-app-bar class="menu">
        <img alt="ITK logo" src="../assets/logo.png">
        <Button btnText="Start Game" @click="$emit('startGame')"/>
        <Header msg="Welcome to Champions of ITK"/>
    </v-app-bar>
</template>

<script>

import Header from './Header.vue'
import Button from './Button.vue'

export default {
    name: 'MainMenu',
    props: {
    },
    components: {
        Header,
        Button
    }
}
</script>

<style scoped>
</style>
