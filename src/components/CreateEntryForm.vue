<template>
    <div>
        <div>
            <label for="entryDescription">Write what happens, something about {{ tableTags }}</label>
            <input id="entryDescription" type="textarea"/>
        </div>
        <div>
            <v-btn color="#0f0">Submit</v-btn>
            <v-btn to="select" color="#aa1">Cancel</v-btn>
        </div>
    </div>
</template>

<script>
export default {
    name: "CreateEntryForm.vue",
    components: {

    },
    props: {
        tableTags: String
    }
}
</script>

<style scoped>
</style>
