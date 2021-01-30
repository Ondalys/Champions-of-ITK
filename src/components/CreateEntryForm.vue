<template>
    <div>
        <div>
            <label for="entryDescription">Write what happens, something about {{ tableTags }}</label>
            <input id="entryDescription" type="textarea"/>
            <v-btn id="addEventOption">Add Option</v-btn>
            <EventOptions/>
        </div>
        <div>
            <v-btn color="#0f0">Submit</v-btn>
            <v-btn to="select" color="#aa1">Cancel</v-btn>
        </div>
    </div>
</template>

<script>
import EventOptions from "./EventOptions"

export default {
    name: "CreateEntryForm.vue",
    components: {
        EventOptions
    },
    props: {
        tableTags: String
    }
}
</script>

<style scoped>
</style>
