<style scoped>
.button-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.button-container > a,
button {
    margin: 10px 0px;
}
</style>
<template>
    <div class="container">
        <div>Your adventure starts here!</div>
        <div class="button-container">
            <v-btn to="decision">Start new adventure</v-btn>
            <v-btn disabled>Load game</v-btn>
        </div>
    </div>
</template>

<script>
export default {
    name: 'select',
    components: {}
};
</script>
