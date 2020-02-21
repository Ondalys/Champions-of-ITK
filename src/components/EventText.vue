<template>
    <div class="main-event">
        <p> {{ eventText }} </p>
    </div>
</template>

<script>
import OptionMenu from './OptionMenu.vue'

export default {
    name: 'EventText',
    props: {
        eventText: String
    },
    components: {
        OptionMenu
    }
}
</script>

<style scoped>
</style>
