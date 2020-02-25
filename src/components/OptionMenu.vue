<template>
    <div>
        <Button btnText="Option"/>
    </div>
</template>

<script>
import Button from "./Button.vue"

export default {
    name: 'OptionMenu',
    components: {
        Button
    },
    props: {
        visible: Boolean
    }
}
</script>

<style scoped>

</style>
