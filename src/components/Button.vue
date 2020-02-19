<template>
    <button>{{ btnText }}</button>
</template>

<script>
export default {
    name: 'Button',
    props: {
        btnText: String
    },
    methods: {
        roll: function (table) {
            // this function should roll on given table
            if(table == "wat"){
                alert("hello");
            }
        }
    }
}
</script>

<style scoped>
button {
    color: gold;
    background-color: gray;
    border-radius: 1em;
    font-size: 2em;
    border: .3em solid gray;
}
</style>
