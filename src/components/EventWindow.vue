<template>
    <div class="main-event" v-if="visibility === true">
        <p> {{ eventText }} </p>
        <OptionMenu/>
    </div>
</template>

<script>
import OptionMenu from './OptionMenu.vue'

export default {
    name: 'EventWindow',
    props: {
        eventText: String,
        visibility: Boolean
    },
    components: {
        OptionMenu
    }
}
</script>

<style scoped>
</style>
