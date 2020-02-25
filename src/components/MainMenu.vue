<template>
    <div class="menu">
        <Button :btnText="startBtnText"></Button>
    </div>
</template>

<script>

import Button from './Button.vue'

export default {
    name: 'MainMenu',
    props: {
        startBtnText: String
    },
    components: {
        Button
    }
}
</script>

<style scoped>
</style>
