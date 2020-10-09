<template>
    <div>
        <CreateEntryForm tableTags="tableTags"/>
    </div>
</template>

<script>
import CreateEntryForm from "../components/CreateEntryForm.vue"

export default {
    name: "CreateEntry.vue",
    components: {
        CreateEntryForm
    }
}
</script>

<style scoped>
</style>
