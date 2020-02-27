<template>
    <div class="menu">
        <Button btnText="Start Game" @click="$emit('startGame')"/>
    </div>
</template>

<script>

import Button from './Button.vue'

export default {
    name: 'MainMenu',
    props: {
    },
    components: {
        Button
    }
}
</script>

<style scoped>
</style>
