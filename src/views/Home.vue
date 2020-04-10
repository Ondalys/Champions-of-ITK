<template>
    <div>
        <MainMenu @rulesToggle="rulesToggle"></MainMenu>
        <UpdatesWindow></UpdatesWindow>
        <RulesDrawer v-bind:class="{ noDisplay:isVisible }"></RulesDrawer>
    </div>
</template>

<script>
import MainMenu from '../components/MainMenu.vue'
import RulesDrawer from '../components/RulesDrawer.vue'
import UpdatesWindow from '../components/UpdatesWindow.vue'

export default {
    name: 'Home.vue',
    data() {
        return {
            isVisible: true
        }
    },
    components: {
        MainMenu,
        RulesDrawer,
        UpdatesWindow
    },
    methods: {
        rulesToggle: function() {
            if(this.isVisible == false){
                this.isVisible = true;
            } else {
                this.isVisible = false;
            }
        }
    }
}
</script>
<style scoped>
.noDisplay {
    display: none;
}
</style>
