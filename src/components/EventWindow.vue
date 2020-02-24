<template>
    <div class="main-event">
        <p> {{ eventText }} </p>
        <OptionMenu/>
    </div>
</template>

<script>
import OptionMenu from './OptionMenu.vue'

export default {
    name: 'EventWindow',
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
