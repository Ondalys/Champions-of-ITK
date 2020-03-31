<style scoped>
.container {
    display: flex;
    flex-direction: column;
}
.button-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.button-container > a,
button {
    width: 50%;
    align-self: center;
    margin: 10px 0px;
}
</style>
<template>
    <div class="container">
        <div>Your adventure starts here!</div>
        <div class="button-container">
            <v-btn dark large color="#8e24aa" to="decision"
                >Start new adventure</v-btn
            >
            <v-btn large disabled>Load game</v-btn>
        </div>
    </div>
</template>

<script>
export default {
    name: 'select',
    components: {}
};
</script>
